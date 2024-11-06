from PIL import Image
import numpy as np

def convMatrix(im, ker, padding="zeros"):
    #Takes an np array as the image and applies the kernel matrix to the image
    M, N = np.shape(im)
    m, n = np.shape(ker)
    ker_size = m*n
    if padding == "zeros":
        mat = np.pad(im, ((m//2, m//2), (n//2, n//2)), 'constant', constant_values=(0, 0))
    if padding == "edge":
        mat = np.pad(im, ((m//2, m//2), (n//2, n//2)), 'edge')
    if padding == "wrap":
        mat = np.pad(im, ((m//2, m//2), (n//2, n//2)), 'wrap')
    
    im_edge = np.zeros((M, N))
    
    for i in range(M):
        for j in range(N):
            a = mat[i:i+m, j:j+n]
            result = (np.multiply(a, ker)).sum()
            im_edge[i, j] = result
    
    return im_edge

image = Image.open("img/moon.tif")
image = image.convert('L')
im = np.array(image)
#ker = np.array([[0, 0, 0], [0, -1, 0], [0, 1, 0]])
ker = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
#ker = np.ones((9, 9))

edge = convMatrix(im.copy(), ker)  

im = im + edge
im = (im/np.max(im))*255
#np.savetxt("log.txt", edge, fmt="%i")

image_edge = Image.fromarray(edge)
image_edge.show()

image = Image.fromarray(im)
image.show()
