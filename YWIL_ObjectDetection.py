import os
import tempfile
import numpy as np
import cv2
import onnxruntime
import onnx
from YWIL_Classes import Detection

class ObjectDetection():

    PROB_THRESHOLD = 0.5
    MAX_DETECTIONS = 5

    ANCHOR_BOXES = np.array([[0.573, 0.677], [1.87, 2.06], [3.34, 5.47], [7.88, 3.53], [9.77, 9.17]])
    IOU_THRESHOLD = 0.5

    def __init__(self):
        model_path = 'ObjectDetection/model'
        model_onnx = model_path + '.onnx'
        model_labels = model_path + '.labels'

        with open(model_labels, 'r') as io:
            self.labels = [x.split(sep=' ', maxsplit=1)[-1].strip() for x in io]

        model = onnx.load(model_onnx)

        with tempfile.TemporaryDirectory() as dirpath:
            temp = os.path.join(dirpath, os.path.basename(model_onnx))
            model.graph.input[0].type.tensor_type.shape.dim[-1].dim_param = 'dim1'
            model.graph.input[0].type.tensor_type.shape.dim[-2].dim_param = 'dim2'
            onnx.save(model, temp)
            options = onnxruntime.SessionOptions()
            options.graph_optimization_level = onnxruntime.GraphOptimizationLevel.ORT_DISABLE_ALL
            self.session = onnxruntime.InferenceSession(temp, options)

        self.input_name = self.session.get_inputs()[0].name

    def Infer(self, image):
        crop_image = image[0:480, 80:560]
        resized_image = cv2.resize(crop_image, (416, 416), interpolation=cv2.INTER_AREA)

        inputs = np.array(resized_image, dtype=np.float32)[np.newaxis,:,:,(2,1,0)]
        inputs = np.ascontiguousarray(np.rollaxis(inputs, 3, 1))

        input_data = self.session.run(None, {self.input_name: inputs})

        outputs = np.squeeze(input_data).transpose((1,2,0)).astype(np.float32)
        results = self._postprocess(outputs)

        return results

    def _postprocess(self, outputs):
        boxes, class_probs = self._extract_bounding_boxes(outputs)

        max_probs = np.amax(class_probs, axis=1)
        index, = np.where(max_probs > self.PROB_THRESHOLD)
        index = index[(-max_probs[index]).argsort()]

        selected_boxes, selected_classes, selected_probs = self._non_maximum_suppression(
            boxes[index], class_probs[index])

        predictions = list()

        for i in range(len(selected_boxes)):
            label = self.labels[selected_classes[i]]
            probability = selected_probs[i] * 100
            left = round(float(selected_boxes[i][0]), 8)
            top = round(float(selected_boxes[i][1]), 8)
            width = round(float(selected_boxes[i][2]), 8)
            height = round(float(selected_boxes[i][3]), 3)
            prediction = Detection(label, probability, left, top, width, height)
            predictions.append(prediction)

        return predictions

    def _extract_bounding_boxes(self, output):
        num_anchor = self.ANCHOR_BOXES.shape[0]
        height, width, channels = output.shape
        num_class = int(channels / num_anchor) - 5

        outputs = output.reshape((height, width, num_anchor, -1))

        x = (self._logistic(outputs[..., 0]) + np.arange(width)[np.newaxis, :, np.newaxis]) / width
        y = (self._logistic(outputs[..., 1]) + np.arange(height)[:, np.newaxis, np.newaxis]) / height
        w = np.exp(outputs[..., 2]) * self.ANCHOR_BOXES[:, 0][np.newaxis, np.newaxis, :] / width
        h = np.exp(outputs[..., 3]) * self.ANCHOR_BOXES[:, 1][np.newaxis, np.newaxis, :] / height

        x = x - w / 2
        y = y - h / 2
        boxes = np.stack((x, y, w, h), axis=-1).reshape(-1, 4)

        objectness = self._logistic(outputs[..., 4])

        class_probs = outputs[..., 5:]
        class_probs = np.exp(class_probs - np.amax(class_probs, axis=3)[..., np.newaxis])
        class_probs = class_probs / np.sum(class_probs, axis=3)[..., np.newaxis] * objectness[..., np.newaxis]
        class_probs = class_probs.reshape(-1, num_class)

        return (boxes, class_probs)

    def _logistic(self, x):
        return np.where(x > 0, 1 / (1 + np.exp(-x)), np.exp(x) / (1 + np.exp(x)))

    def _non_maximum_suppression(self, boxes, class_probs):
        max_detections = min(self.MAX_DETECTIONS, len(boxes))
        max_probs = np.amax(class_probs, axis=1)
        max_classes = np.argmax(class_probs, axis=1)

        areas = boxes[:, 2] * boxes[:, 3]

        selected_boxes = []
        selected_classes = []
        selected_probs = []

        while len(selected_boxes) < max_detections:
            i = np.argmax(max_probs)
            if max_probs[i] < self.PROB_THRESHOLD:
                break

            selected_boxes.append(boxes[i])
            selected_classes.append(max_classes[i])
            selected_probs.append(max_probs[i])

            box = boxes[i]
            other_indices = np.concatenate((np.arange(i), np.arange(i + 1, len(boxes))))
            other_boxes = boxes[other_indices]

            x1 = np.maximum(box[0], other_boxes[:, 0])
            y1 = np.maximum(box[1], other_boxes[:, 1])
            x2 = np.minimum(box[0] + box[2], other_boxes[:, 0] + other_boxes[:, 2])
            y2 = np.minimum(box[1] + box[3], other_boxes[:, 1] + other_boxes[:, 3])
            w = np.maximum(0, x2 - x1)
            h = np.maximum(0, y2 - y1)

            overlap_area = w * h
            iou = overlap_area / (areas[i] + areas[other_indices] - overlap_area)

            overlapping_indices = other_indices[np.where(iou > self.IOU_THRESHOLD)[0]]
            overlapping_indices = np.append(overlapping_indices, i)

            class_probs[overlapping_indices, max_classes[i]] = 0
            max_probs[overlapping_indices] = np.amax(class_probs[overlapping_indices], axis=1)
            max_classes[overlapping_indices] = np.argmax(class_probs[overlapping_indices], axis=1)

        return selected_boxes, selected_classes, selected_probs