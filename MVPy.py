from tkinter import Tk, Label
from PIL import ImageTk, Image
from numpy import median
import cv2
from datetime import datetime
import time

print('[ MVPy ] OpenCV', cv2.__version__)

from Interface import Window

window = Window()

import Constants
from Constants import colors_hex, colors_bgr
from Constants import multilabel_labels, multilabel_help, multilabel_error
from Constants import detection_labels, detection_help, detection_error
from Constants import multiclass_labels, multiclass_help, multiclass_error

import Images
from Images import color_images, progress_images
from Images import assembly_images, validation_images
from Images import completed_image, completed_mask

from openvino.inference_engine import IECore

inference_engine = IECore()
print('[ MVPy ] OpenVINO inference engine created')

from MultilabelClassification import MultilabelClassification
from ObjectDetection import ObjectDetection
from MulticlassClassification import MulticlassClassification

multilabel = MultilabelClassification(inference_engine)
print('[ MVPy ] Multilabel Classification model loaded')
detection = ObjectDetection(inference_engine)
print('[ MVPy ] Object Detection model loaded')
multiclass = MulticlassClassification(inference_engine)
print('[ MVPy ] Multiclass Classification model loaded')

number_of_models = 3
number_of_steps = 8
number_of_messages = [
    len(multilabel_help), len(detection_help), len(multiclass_help)]

step_validations = {}
for step in range(number_of_steps):
    step_validations[str(step)] = 0

message_waitings = {}
for model in range(number_of_models):
    for message in range(number_of_messages[model]):
        message_waitings[str(model) + str(message)] = 0

waiting_millis = 40
waiting_frames = 25
min_validations = 25

welcome_waiting = 0
current_step = 0
current_model = 0
current_message = 0

assembly_completed = False

infer_times = []

def video_streaming():
    global welcome_waiting
    global video_capture
    global current_step
    global assembly_completed
    _, frame = video_capture.read()
    image = cv2.resize(frame, (640, 480), interpolation=cv2.INTER_AREA)
    if welcome_waiting > waiting_frames:
        start = datetime.now().microsecond
        predictions = []
        if current_model == 0:
            predictions = multilabel.Infer(image)
        elif current_model == 1:
            predictions = detection.Infer(image)
        elif current_model == 2:
            predictions = multiclass.Infer(image)
        end = datetime.now().microsecond
        window.assembly.config(image=assembly_images[current_step])
        print_currently(len(predictions))
        print_detections(predictions)
        print_inference(start, end)
        if current_model == 0:
            process_multilabel(predictions)
        elif current_model == 1:
            detections = process_detection(predictions)
            image = draw_detections(image, detections)
        elif current_model == 2:
            process_multiclass(predictions)
    else:
        welcome_waiting = welcome_waiting + 1
    if assembly_completed:
        cv2_array = draw_completed(image)
    else:
        cv2_array = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
    pil_image = Image.fromarray(cv2_array)
    image_tk = ImageTk.PhotoImage(image=pil_image)
    window.streaming.image_tk = image_tk
    window.streaming.config(image=image_tk)
    window.streaming.after(waiting_millis, video_streaming)

def process_multilabel(predictions):
    global current_message
    message = multilabel_help[current_message]
    checking_value = 'aux'
    detected_labels = []
    for prediction in predictions:
            detected_labels.append(prediction.Label)
    if current_message != 0:
        if multilabel_labels[5] in detected_labels:
            checking_value = 'no'
            message = multilabel_error[0]
        elif current_message == 1 and (
            multilabel_labels[6] in detected_labels or 
            multilabel_labels[9] in detected_labels):
            checking_value = 'no'
            message = multilabel_error[1]
        elif len(detected_labels) > 0:
            checking_value = 'yes'
            if current_step == 3:
                condition_1 = multilabel_labels[3] in detected_labels
                condition_2 = multilabel_labels[4] in detected_labels
                if condition_1 and condition_2:
                    update_message()
                    update_progress()
                elif condition_1:
                    checking_value = 'aux'
            for label in detected_labels:
                if str(current_step) in label:
                    update_message()
                    update_progress()
                    break
    draw_validation(checking_value)
    write_instruction(message)
    if current_message == 0:
        update_message()
        window.bar_images[0].config(image=color_images[0])
        window.bar_progress[0].config(image=progress_images['aux'])
    if current_message == len(multilabel_help) - 1:
        update_model()

def process_detection(predictions):
    global current_message
    message = detection_help[current_message]
    if len(predictions) > 0:
        checking_value = 'yes'
    else:
        checking_value = 'aux'
    selected_predictions = []
    for prediction in predictions:
        if str(current_step) in prediction.Label:
            selected_predictions.append(prediction)
    selected_labels = []
    for prediction in selected_predictions:
            selected_labels.append(prediction.Label)
    if current_message != 0:
        if detection_labels[2] in selected_labels:
            error_predictions = []
            for prediction in selected_predictions:
                if prediction.Label == detection_labels[2]:
                    error_predictions.append(prediction)
                    break
            selected_predictions = error_predictions
            checking_value = 'no'
            message = detection_error[0]
        if current_step == 5:
            part_labels = 0
            for label in selected_labels:
                if label == detection_labels[1]:
                    part_labels = part_labels + 1
            if part_labels == 4:
                update_message()
                update_progress()
        if current_step == 6:
            if detection_labels[4] in selected_labels:
                update_message()
                update_progress()
    draw_validation(checking_value)
    write_instruction(message)
    if current_message == 0:
        update_message()
    if current_message == len(detection_help) - 1:
        update_model()
    return selected_predictions

def process_multiclass(predictions):
    global current_message
    global current_step
    global current_model
    global assembly_completed
    checking_value = 'yes'
    if current_message == len(multiclass_help):
        current_message = len(multiclass_help) - 1
        current_step = 7
        current_model = 2
        assembly_completed = True
    message = multiclass_help[current_message]
    detected_labels = []
    for prediction in predictions:
            detected_labels.append(prediction.Label)
    if current_message != 0 and current_message != len(multiclass_help) - 1:
        if len(detected_labels) > 0:
            if multiclass_labels[2] in detected_labels:
                checking_value = 'no'
                message = multiclass_error[0]
            elif multiclass_labels[3] in detected_labels:
                checking_value = 'no'
                message = multiclass_error[1]
            elif multiclass_labels[1] in detected_labels:
                checking_value = 'yes'
                update_message()
            else:
                checking_value = 'yes'
        else:
            checking_value = 'aux'
    draw_validation(checking_value)
    write_instruction(message)
    if current_message == 0:
        update_message()
    if current_message == len(multiclass_help) - 1:
        window.bar_images[current_step].config(
            image=color_images[current_step], bg=colors_hex['yes'])
        window.bar_progress[current_step].config(
            image=progress_images['yes'], bg=colors_hex['yes'])
        update_message()

def validate_step():
    global current_step
    global step_validations
    current = str(current_step)
    step_validations[current] = step_validations[current] + 1
    return current

def update_progress():
    global current_step
    global step_validations
    current = validate_step()
    if step_validations[current] == min_validations:
        window.bar_images[current_step].config(
            image=color_images[current_step], bg=colors_hex['yes'])
        window.bar_progress[current_step].config(
            image=progress_images['yes'], bg=colors_hex['yes'])
        current_step = current_step + 1
        window.bar_images[current_step].config(
            image=color_images[current_step])
        window.bar_progress[current_step].config(
            image=progress_images['aux'], bg=colors_hex['aux'])

def wait_message():
    global current_model
    global current_message
    global message_waitings
    current = str(current_model) + str(current_message)
    message_waitings[current] = message_waitings[current] + 1
    return current

def update_message():
    global message_waitings
    global current_message
    current = wait_message()
    if message_waitings[current] == waiting_frames:
        current_message = current_message + 1

def update_model():
    global message_waitings
    global current_message
    global current_model
    global infer_times
    current = wait_message()
    if message_waitings[current] == waiting_frames:
        current_message = 0
        current_model = current_model + 1
        infer_times = []

def print_currently(count):
    if count > 0:
        text = 'Current detections in Step #%s:' % current_step
    else:
        text = 'No objects detected in Step #%s.' % current_step
    window.currently.config(text=text)

def print_detections(predictions):
    text = ''
    for prediction in predictions:
        text += prediction.__str__() + '\n'
    window.detections.config(text=text)

def print_inference(start, end):
    if infer_times.count == waiting_frames:
        infer_times.pop(0)
    infer_times.append((end-start)/1000)
    ms = median(infer_times)
    text = 'Last inference time: {:.3f}ms'.format(ms)
    window.inference.config(text=text)

def write_instruction(message):
    window.instruction.config(text=message)

def draw_detections(image, predictions):
    for prediction in predictions:
        if 'hole' in prediction.Label:
            image = draw_rectangle(image, prediction.Box, colors_bgr['aux'], 2)
        elif 'part' in prediction.Label:
            image = draw_rectangle(image, prediction.Box, colors_bgr['yes'], 4)
        elif 'error' in prediction.Label:
            image = draw_rectangle(image, prediction.Box, colors_bgr['no'], 6)
    return image

def draw_validation(checking_value):
    window.validation.config(
        image=validation_images[checking_value], bg=colors_hex[checking_value])
    window.assembly.config(bg=colors_hex[checking_value])

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

# video_capture = cv2.VideoCapture(0)
# video_capture = cv2.VideoCapture(1)
# video_capture = cv2.VideoCapture(2)
video_capture = cv2.VideoCapture('Videos/MVPy_Assembly_640x480.mp4')

video_streaming()

window.root.mainloop()