from PIL import Image, ImageFilter

def roll(im, delta):
    """Roll an image sideways."""
    xsize, ysize = im.size

    delta = delta % xsize
    if delta == 0:
        return im

    part1 = im.crop((0, 0, delta, ysize))
    part2 = im.crop((delta, 0, xsize, ysize))
    im.paste(part1, (xsize - delta, 0, xsize, ysize))
    im.paste(part2, (0, 0, xsize - delta, ysize))

    return im

def swap_bands(im):
    r, g, b = im.split()
    im = Image.merge("RGB", (b, r, g))
    return im

im = Image.open("img/rabbit.png").convert("RGB")

out = im.filter(ImageFilter.EMBOSS)
#out = im.point(lambda i: i*100)

out.show()

