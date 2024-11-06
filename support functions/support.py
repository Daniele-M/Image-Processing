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
    
    for i in range(m//2, M):
        for j in range(n//2, N):
            a = mat[i:i+m, j:j+n]
            result = (np.sum(np.multiply(a, ker)))//ker_size
            im[i-m//2, j-n//2] = result
    
    return im
        


mat = convMatrix(np.zeros((100, 100)), np.ones((3,3)))
print(np.shape(mat))
