# welcome message before starting
welcome = "YWIL - YOU WORK, IT LOOKS. LET'S START THE ASSEMBLY!"

# validation and detection box colors
colors_hex = {
    'yes': '#0ea84b',
    'no': '#ec1f24',
    'aux': '#868686'}
colors_bgr = {
    'yes': (75, 168, 14),
    'no': (36, 31, 236),
    'aux': (255, 255, 255)}

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
    "MULTILABEL CLASSIF. MODEL FOR STEPS 0 TO 4 READY",
    "WAITING FOR THE WHITE BASE TO BE PLACED...",
    "PLACE THE FIRST PART IN THE RECTANGULAR HOLE",
    "PLACE THE RED PART AS SHOWN IN THE HELP IMAGE",
    "PLACE THE PINK PART WITH THE HOLE FACING UP",
    "PLACE THE GRAY ROTOR ON TOP OF THE PINK PART",
    "WELL DONE! LET'S CONTINUE WITH THE NEXT STEPS"]
multilabel_error = [
    "FLIP THE PINK PART, IT IS PLACED BACKWARDS",
    "REMOVE THE PREVIOUS ASSEMBLY FROM THE BASE"]

# object detection steps constants
detection_labels = [
    "Step5.hole",
    "Step5.part",
    "Step5.error",
    "Step6.hole",
    "Step6.part"]
detection_help = [
    "OBJECT DETECTION MODEL FOR STEPS 5 AND 6 READY",
    "PLACE THE GREEN PARTS IN THE FOUR SQUARE HOLES",
    "PLACE THE ORANGE PART IN THE CENTRAL ROUND HOLE",
    "CONGRATULATIONS! LET'S MOVE ON TO THE LAST STEP"]
detection_error = [
    "REMOVE THE MARKED PART, IT IS IN THE WRONG HOLE"]

# classification multiclass steps constants
multiclass_labels = [
    "Step7.start",
    "Step7.true",
    "Step7.false.A",
    "Step7.false.B"]
multiclass_help = [
    "MULTICLASS CLASSIF. MODEL FOR LAST STEP 7 READY",
    "PLACE THE GRAY GEAR ON TOP OF THE MECHANISM",
    "VERY GOOD JOB, HUMAN! ASSEMBLY COMPLETED!"]
multiclass_error = [
    "FLIP THE GRAY GEAR, IT IS PLACED BACKWARDS",
    "ROTATE THE GEAR A BIT UNTIL IT FITS PROPERLY"]