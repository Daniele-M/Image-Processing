from PIL import Image
import numpy as np
import struct

from logic import *
    
im = np.array(Image.open("img/rabbit.png"))

im = np.delete(im, [3], axis=2)
im_final = im
im = scale_to_grey(im)      
im_hex = matrix_rgb_to_hex(im)
inverted_matrix = matrix_format_to_hex(color_invert(matrix_add_hex_prefix(im_hex)))
contrast_matrix = matrix_format_to_hex(color_contrast(matrix_add_hex_prefix(im_hex)))
mean4_matrix = matrix_format_to_hex(color_4mean(matrix_add_hex_prefix(im_hex)))
mean8_matrix = matrix_format_to_hex(color_8mean(matrix_add_hex_prefix(im_hex)))

im_final = matrix_hex_to_rgb(inverted_matrix, im_final)

#im_final = scale_to_grey(im_final)

Image.fromarray(im_final).show()
Image.fromarray(im_final).save("img/final_rabbit.png")


