from tkinter import Tk, Label
from PIL import ImageTk, Image
import cv2

root = Tk()
root.wm_title('YWIL - You Work, It Looks')
root.geometry('960x540')
root.resizable(False, False)

import YWIL_Constants
from YWIL_Constants import colors

import YWIL_Images
from YWIL_Images import alpha_images, bar_images, progress_images
from YWIL_Images import help_images, validation_images
from YWIL_Images import completed_image, completed_mask

streaming = Label(root, borderwidth = 0, bg='white')
instruction = Label(root, borderwidth = 0, bg='black')
validation = Label(root, borderwidth = 0, bg=colors['gray'])
help_image = Label(root, borderwidth = 0, bg=colors['gray'])
detections = Label(root, borderwidth = 0, bg='black')

streaming.place(x=0,   y=0,   width=640, height=480)
validation.place(x=640, y=100, width=160, height=160)
instruction.place(x=640, y=0,   width=320, height=100)
help_image.place(x=800, y=100, width=160, height=160)
detections.place(x=640, y=260, width=320, height=220)

bar_images = []
bar_progress = []

for n in range(8):
    bar_images.append(Label(root, borderwidth=0))
    bar_images[n].config(bg=colors['gray'], image=alpha_images[n])
    bar_images[n].place(x=60*(2*n), y=480, width=60, height=60)
    bar_progress.append(Label(root, borderwidth=0))
    bar_progress[n].config(bg=colors['gray'])
    bar_progress[n].place(x=60*(2*n+1), y=480, width=60, height=60)

video_capture = cv2.VideoCapture(0)

assembly_completed = True

def video_streaming():
    _, frame = video_capture.read()
    resized_frame = cv2.resize(frame, (640, 480), interpolation=cv2.INTER_AREA)

    if assembly_completed:
        completed = cv2.imread(completed_image)
        mask = cv2.imread(completed_mask, cv2.IMREAD_GRAYSCALE)
        background = cv2.bitwise_or(resized_frame, resized_frame, mask = mask)
        added_image = cv2.bitwise_or(background, completed)
        cv2_array = cv2.cvtColor(added_image, cv2.COLOR_BGR2RGBA)
    else:
        cv2_array = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGBA)

    pil_image = Image.fromarray(cv2_array)
    image_tk = ImageTk.PhotoImage(image=pil_image)
    streaming.image_tk = image_tk
    streaming.config(image=image_tk)
    streaming.after(10, video_streaming) 

video_streaming()

root.mainloop()