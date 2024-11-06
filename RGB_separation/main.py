from PIL import Image
import numpy as np

im = np.array(Image.open("img/rabbit_doodle.png"))
im = np.delete(im, [3], axis=2)
    
def color_splitter(im, color1, color2):
    for i in range(np.shape(im)[0]):
        for j in range(np.shape(im)[1]):
            im[i][j][color1] = 0
            im[i][j][color2] = 0
    return im

r = color_splitter(im.copy(), 1, 2)
g = color_splitter(im.copy(), 0, 2)
b = color_splitter(im.copy(), 0, 1)

    
Image.fromarray(r).save("img/r_channel.png")
Image.fromarray(g).save("img/g_channel.png")
Image.fromarray(b).save("img/b_channel.png")

