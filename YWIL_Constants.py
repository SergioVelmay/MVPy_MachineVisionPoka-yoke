# validation and detection box colors
colors = {
    'red': '#ec1f24',
    'green': '#0ea84b',
    'gray': '#868686'}

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
multilabel_help_messages = [
    "Multilabel classification from 0 to 4 ready",
    "Waiting for the white base to be placed...",
    "Place the first part in the rectangular hole",
    "Place the red part as shown in the help image",
    "Place the pink part with the hole facing up",
    "Place the gray rotor on top of the pink part",
    "Well done! Let's continue with the next steps"]
multilabel_error_messages = [
    "Flip the pink part, it is placed backwards",
    "Remove the previous assembly from the base"]

# object detection steps constants
detection_labels = [
    "Step5.hole",
    "Step5.part",
    "Step5.error",
    "Step6.hole",
    "Step6.part"]
detection_help_messages = [
    "Object Detection model for steps 5 and 6 ready",
    "Place the green parts in the four square holes",
    "Place the orange part in the central round hole",
    "Congratulations! Let's move on to the last step"]
detection_error_messages = [
    "Remove the marked part, it is in the wrong hole"]

# classification multiclass steps constants
multiclass_labels = [
    "Step7.start",
    "Step7.true",
    "Step7.false.A",
    "Step7.false.B"]
multiclass_help_messages = [
    "Multiclass classification for step 7 ready",
    "Place the gray gear on top of the mechanism",
    "Very good job, human! Assembly completed!"]
multiclass_error_messages = [
    "Flip the gray gear, it is placed backwards",
    "Rotate the gear a bit until it fits properly"]