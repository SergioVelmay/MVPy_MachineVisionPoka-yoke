import cv2
import numpy as np
from openvino.inference_engine import IECore
from YWIL_Classes import Classification

class MultilabelClassification:

    PROB_THRESHOLD = 0.7
    MAX_DETECTIONS = 2

    def __init__(self):
        model_path = 'MultilabelClassification/model'
        model_xml = model_path + '.xml'
        model_bin = model_path + '.bin'
        model_labels = model_path + '.labels'
        device_name = 'CPU'

        with open(model_labels, 'r') as io:
            self.labels = [x.split(sep=' ', maxsplit=1)[-1].strip() for x in io]

        inference_engine = IECore()

        network = inference_engine.read_network(model=model_xml, weights=model_bin)

        network.batch_size = 1

        self.input_blob = next(iter(network.input_info))
        self.output_blob = next(iter(network.outputs))

        n, c, h, w = network.input_info[self.input_blob].input_data.shape

        self.exec_network = inference_engine.load_network(network=network, device_name=device_name)

        self.images = np.ndarray(shape=(n, c, h, w))

    def Infer(self, image):
        crop_image = image[0:480, 80:560]
        resized_image = cv2.resize(crop_image, (224, 224), interpolation=cv2.INTER_AREA)
        input_image = resized_image.transpose((2, 0, 1))

        self.images[0] = input_image

        ml_result = self.exec_network.infer(inputs={self.input_blob: self.images})
        ml_output = ml_result[self.output_blob]

        predictions = list()
        
        for probs in ml_output:
            probs = np.squeeze(probs)
            top_ind = np.argsort(probs)[-self.MAX_DETECTIONS:][::-1]
            for id in top_ind:
                if probs[id] > self.PROB_THRESHOLD:
                    prob = probs[id] * 100
                    prediction = Classification(self.labels[id], prob)
                    predictions.append(prediction)

        return predictions