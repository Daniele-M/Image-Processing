from PIL import Image
import keyboard

def im_bw(im_dir, save_name):
    step = 120
    with Image.open(im_dir) as im:
        gim = im.convert("L")
        for x in range(gim.size[0]):
            for y in range(gim.size[1]):
                if gim.getpixel([x,y]) < step:
                    gim.putpixel((x, y), 0)
                else:
                    gim.putpixel([x,y], 255)
        gim.save(save_name)
        
def im_invert_color(im_dir, save_name):
    with Image.open(im_dir) as im:
        gim = im.convert("L")
        for x in range(gim.size[0]):
            for y in range(gim.size[1]):
                gim.putpixel([x,y], 255 - gim.getpixel([x,y]))
        gim.save(save_name)
                    
im_invert_color("img/rabbit_doodle.png", "img/rabbit_inverted.png")
im_bw("img/rabbit_doodle.png", "img/rabbit_bw.png")
im_invert_color("img/rabbit_bw.png", "img/rabbit_bw_inverted.png")
