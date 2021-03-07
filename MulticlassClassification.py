import cv2
import numpy as np
from openvino.inference_engine import IECore
from Classes import Classification

class MulticlassClassification:

    PROB_THRESHOLD = 0.7
    MAX_DETECTIONS = 1

    def __init__(self, inference_engine, device_name):
        model_path = 'MulticlassClassification/model'
        model_xml = model_path + '.xml'
        model_bin = model_path + '.bin'
        model_labels = model_path + '.labels'

        with open(model_labels, 'r') as io:
            self.labels = [x.split(sep=' ', maxsplit=1)[-1].strip() for x in io]

        network = inference_engine.read_network(model=model_xml, weights=model_bin)

        network.batch_size = 1

        self.input_blob = next(iter(network.inputs))
        self.output_blob = next(iter(network.outputs))

        n, c, h, w = network.inputs[self.input_blob].shape

        self.exec_network = inference_engine.load_network(network=network, device_name=device_name)

        self.images = np.ndarray(shape=(n, c, h, w))

    def Infer(self, image):
        self.images[0] = self._preprocess(image)

        result = self.exec_network.infer(inputs={self.input_blob: self.images})

        outputs = result[self.output_blob]

        return self._postprocess(outputs)

    def _preprocess(self, image):
        resized_image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

        input_image = resized_image.transpose((2, 0, 1))

        return input_image

    def _postprocess(self, outputs):
        predictions = list()
        
        for probs in outputs:
            probs = np.squeeze(probs)
            top_ind = np.argsort(probs)[-self.MAX_DETECTIONS:][::-1]
            for id in top_ind:
                if probs[id] > self.PROB_THRESHOLD:
                    prob = probs[id] * 100
                    prediction = Classification(self.labels[id], prob)
                    predictions.append(prediction)

        return predictions