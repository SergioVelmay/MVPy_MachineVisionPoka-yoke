# welcome message before starting
welcome = "YWIL - YOU WORK, IT LOOKS. LET'S START THE ASSEMBLY!"

# validation and detection box colors
colors_hex = {
    'green': '#0ea84b',
    'red': '#ec1f24',
    'gray': '#868686'}
colors_rgb = {
    'green': (14, 168, 75),
    'red': (236, 31, 36),
    'white': (255, 255, 255)}

# classification multilabel steps constants
multilabel_labels = [
    "Step0",
    "Step1",
    "Step2",
    "Step3",
    "true",
    "false",
    "Step4",
    "front",
    "back",
    "Step7",
    "right",
    "wrong"]
multilabel_help = [
    "Multilabel classification from 0 to 4 ready",
    "Waiting for the white base to be placed...",
    "Place the first part in the rectangular hole",
    "Place the red part as shown in the help image",
    "Place the pink part with the hole facing up",
    "Place the gray rotor on top of the pink part",
    "Well done! Let's continue with the next steps"]
multilabel_error = [
    "Flip the pink part, it is placed backwards",
    "Remove the previous assembly from the base"]

# object detection steps constants
detection_labels = [
    "Step5.hole",
    "Step5.part",
    "Step5.error",
    "Step6.hole",
    "Step6.part"]
detection_help = [
    "Object Detection model for steps 5 and 6 ready",
    "Place the green parts in the four square holes",
    "Place the orange part in the central round hole",
    "Congratulations! Let's move on to the last step"]
detection_error = [
    "Remove the marked part, it is in the wrong hole"]

# classification multiclass steps constants
multiclass_labels = [
    "Step7.start",
    "Step7.true",
    "Step7.false.A",
    "Step7.false.B"]
multiclass_help = [
    "Multiclass classification for step 7 ready",
    "Place the gray gear on top of the mechanism",
    "Very good job, human! Assembly completed!"]
multiclass_error = [
    "Flip the gray gear, it is placed backwards",
    "Rotate the gear a bit until it fits properly"]