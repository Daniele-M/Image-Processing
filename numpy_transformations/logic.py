import numpy as np
import struct

def rgb_to_grey(color):
    return color[0]*0.58 + color[1]*0.17 + color[2]*0.8

def hex_to_rgb(value):
    return struct.unpack('BBB',bytes.fromhex(value))

def matrix_rgb_to_hex(np_array):
    hexarray = np.vectorize('{:02x}'.format)
    np_array = hexarray(np_array)
    np_array = np_array.view('U6')
    return np_array.reshape(np_array.shape[0], np_array.shape[1])

def matrix_hex_to_rgb(np_iarray, np_oarray):
    for xid in range(np_iarray.shape[0]):
        for yid in range(np_iarray.shape[1]):
            np_oarray[xid, yid] = hex_to_rgb(np_iarray[xid, yid])
    return np_oarray

def scale_to_grey(np_array):
    for xid in range(np_array.shape[0]):    
        for yid in range(np_array.shape[1]):
            grey_color = rgb_to_grey(np_array[xid, yid, :])
            np_array[xid, yid, :] = [grey_color, grey_color, grey_color]
    return np_array

def matrix_to_hex(np_array):
    shape = np_array.shape
    np_array = np_array.flatten()
    np_array = np.array([int(x, 16) for x in np_array])
    return np_array.reshape(shape)

def matrix_add_hex_prefix(np_array):
    shape = np_array.shape
    np_array = np_array.flatten()
    return np.array([int('0x' + x, 16) for x in np_array]).reshape(shape)

def matrix_strip_hex(np_array):
    shape = np_array.shape
    np_array = np_array.flatten()
    return np.array([x[2:] for x in np_array]).reshape(shape)

def matrix_format_to_hex(np_array):
    return np.vectorize('{:06x}'.format)(np_array)
        

def view_matrix(np_array):
    shape = np_array.shape
    np_array = np_array.flatten()
    print(np_array)
    print(shape)

def color_invert(np_array):
    white_matrix = matrix_to_hex(np.ones(np_array.shape, dtype='<U6'))*0xffffff
    return white_matrix - np_array

def color_contrast(np_array):
    for xid in range(np_array.shape[0]):
        for yid in range(np_array.shape[1]):
            if np_array[xid, yid] < 0x7fffff:
                np_array[xid, yid] = 0x0
            else:
                np_array[xid, yid] = 0xffffff
    return np_array

def color_4mean(np_array):
    for xid in range(np_array.shape[0]):
        for yid in range(np_array.shape[1]):
            neighbors = get_4neighbors(np_array, xid, yid)
            np_array[xid, yid] = get_mean(neighbors)
    return np_array

def color_8mean(np_array):
    for xid in range(np_array.shape[0]):
        for yid in range(np_array.shape[1]):
            neighbors = get_8neighbors(np_array, xid, yid)
            np_array[xid, yid] = get_mean(neighbors)
    return np_array

def get_4neighbors(np_array, i, j):
    neighbors = np.zeros((5,1))
    try:
        neighbors[0] = np_array[i+1, j]
    except IndexError:
        pass
    try:
        neighbors[1] = np_array[i-1, j]
    except IndexError:
        pass
    try:
        neighbors[2] = np_array[i, j+1]
    except IndexError:
        pass
    try:
        neighbors[3] = np_array[i, j-1]
    except IndexError:
        pass
    neighbors[4] = np_array[i, j]
    neighbors = neighbors[neighbors!=0]
    return neighbors

def get_8neighbors(np_array, i, j):
    neighbors = np.zeros((9,1))
    try:
        neighbors[0] = np_array[i+1, j]
    except IndexError:
        pass
    try:
        neighbors[1] = np_array[i-1, j]
    except IndexError:
        pass
    try:
        neighbors[2] = np_array[i, j+1]
    except IndexError:
        pass
    try:
        neighbors[3] = np_array[i, j-1]
    except IndexError:
        pass
    try:
        neighbors[4] = np_array[i+1, j+1]
    except IndexError:
        pass
    try:
        neighbors[5] = np_array[i-1, j+1]
    except IndexError:
        pass
    try:
        neighbors[6] = np_array[i+1, j-1]
    except IndexError:
        pass
    try:
        neighbors[7] = np_array[i-1, j-1]
    except IndexError:
        pass
    neighbors[8] = np_array[i, j]
    neighbors = neighbors[neighbors!=0]
    return neighbors

def get_mean(pixels):
    return np.mean(pixels)
