from PIL import ImageTk, Image

url_route = 'Resources/'
url_prefix = url_route + 'Step'

bar_images = []

for n in range(8):
    image_url = url_prefix + str(n) + '_50.jpg'
    bar_images.append(ImageTk.PhotoImage(Image.open(image_url)))

alpha_images = []

for n in range(8):
    image_url = url_prefix + str(n) + '_50_alpha.png'
    alpha_images.append(ImageTk.PhotoImage(Image.open(image_url)))

progress_names = ['No', 'Yes', 'Arrow']

progress_images = {}

for progress_name in progress_names:
    image_url = url_prefix + progress_name + '_60.png'
    progress_images[progress_name] = ImageTk.PhotoImage(Image.open(image_url))

help_images = []

for n in range(8):
    image_url = url_prefix + str(n) + '.jpg'
    help_images.append(ImageTk.PhotoImage(Image.open(image_url)))

validation_names = progress_names
validation_names.append('Pause')

validation_images = {}

for validation_name in validation_names:
    image_url = url_prefix + validation_name + '.png'
    validation_images[validation_name] = ImageTk.PhotoImage(Image.open(image_url))

assembly_name = 'AssemblyCompleted'

completed_image = url_route + assembly_name + '.png'
completed_mask = url_route + assembly_name + '_mask.png'