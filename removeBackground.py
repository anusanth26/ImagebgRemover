from rembg import remove
from PIL import Image

input_path = "image2.png"
output_path = "output2.png"

input_image = Image.open(input_path)

output_image = remove(input_image)

output_image.save(output_path)