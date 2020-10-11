from tkinter import Tk, Label
from PIL import ImageTk, Image
from datetime import datetime
from numpy import median
import cv2

from YWIL_Window import Window

window = Window()

import YWIL_Constants
from YWIL_Constants import colors_hex, colors_rgb
from YWIL_Constants import multilabel_labels, multilabel_help, multilabel_error
from YWIL_Constants import detection_labels, detection_help, detection_error
from YWIL_Constants import multiclass_labels, multiclass_help, multiclass_error

import YWIL_Images
from YWIL_Images import color_images, progress_images
from YWIL_Images import assembly_images, validation_images
from YWIL_Images import completed_image, completed_mask

from YWIL_MultilabelClassification import MultilabelClassification
from YWIL_ObjectDetection import ObjectDetection
from YWIL_MulticlassClassification import MulticlassClassification

multilabel = MultilabelClassification()
detection = ObjectDetection()
multiclass = MulticlassClassification()

current_step = 0
current_model = 0
current_message = 0

assembly_completed = False

times = []

def video_streaming():
    _, frame = video_capture.read()
    image = cv2.resize(frame, (640, 480), interpolation=cv2.INTER_AREA)

    start = datetime.now().microsecond

    #predictions = multilabel.Infer(image)
    #predictions = multiclass.Infer(image)
    predictions = detection.Infer(image)

    end = datetime.now().microsecond

    print_currently()
    print_detections(predictions)
    print_inference(start, end)

    for prediction in predictions:
        draw_rectangle(image, prediction.Box, colors_rgb['white'], 2)

    if assembly_completed:
        cv2_array = draw_completed(image)
    else:
        cv2_array = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)

    pil_image = Image.fromarray(cv2_array)
    image_tk = ImageTk.PhotoImage(image=pil_image)
    window.streaming.image_tk = image_tk
    window.streaming.config(image=image_tk)
    window.streaming.after(40, video_streaming)

def print_currently():
    text = 'Current Detections in Step #%s:' % current_step
    window.currently.config(text=text)

def print_detections(predictions):
    text = ''
    for prediction in predictions:
        text += prediction.__str__() + '\n'
    window.detections.config(text=text)

def print_inference(start, end):
    if times.count == 25:
        times.pop(0)
    times.append((end-start)/1000)
    ms = median(times)
    text = 'Last Inference Time: {:.3f}ms'.format(ms)
    window.inference.config(text=text)

def draw_rectangle(image, box, color, thick):
    x1 = int(round(box.Left * 480 + 80))
    y1 = int(round(box.Top * 480))
    x2 = x1 + int(round(box.Width * 480))
    y2 = y1 + int(round(box.Height * 480))
    cv2.rectangle(image, (x1, y1), (x2, y2), color, thick)
    return image

def draw_completed(image):
    completed = cv2.imread(completed_image)
    mask = cv2.imread(completed_mask, cv2.IMREAD_GRAYSCALE)
    background = cv2.bitwise_or(image, image, mask = mask)
    added_image = cv2.bitwise_or(background, completed)
    cv2_array = cv2.cvtColor(added_image, cv2.COLOR_BGR2RGBA)
    return cv2_array

window.bar_images[3].config(image=color_images[3])
window.bar_progress[3].config(image=progress_images['aux'])

window.bar_images[4].config(image=color_images[4], bg=colors_hex['red'])
window.bar_progress[4].config(image=progress_images['no'], bg=colors_hex['red'])

window.bar_images[5].config(image=color_images[5], bg=colors_hex['green'])
window.bar_progress[5].config(image=progress_images['yes'], bg=colors_hex['green'])

window.validation.config(image=validation_images['no'], bg=colors_hex['red'])
window.assembly.config(image=assembly_images[6], bg=colors_hex['red'])

video_capture = cv2.VideoCapture(0)

video_streaming()

window.root.mainloop()