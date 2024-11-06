from PIL import Image
import numpy as np

"Creates an image with random colored pixels"

im = np.random.randint(0, 255, size=(500, 500))
im_r = np.random.randint(0, 255, size=(500, 500))
im_g = np.random.randint(0, 255, size=(500, 500))
im_b = np.random.randint(0, 255, size=(500, 500))

im_rgb = np.array((im_r, im_g, im_b)).T

image = Image.fromarray(im)
image_rgb = Image.fromarray(im_rgb.astype(np.uint8))
image_rgb.show()
image.convert('L').save("img/random_noise_grey.png")
image_rgb.save("img/random_noise_rgb.png")
