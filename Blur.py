'''
EN.640.635 Software Carpentry
Lab 3 - PIL Image Blurring and Luminance

In this lab assignment, we want to write two functions that can manipulate
images: one to blur the image and one to set the luminance (or brightness) of
the image.
'''
from PIL import Image
import numpy as np

def blur(fptr, mask=3):
    '''
    Apply a blur to an image. Saves both the original image and the
    newly-blurred image.

    **Parameters**

        fptr: *str*
            The name of an image file, with its extension
            (ex. spring.jpg, cat.png).
        mask: *int, optional*
            The size of our kernel mask.

    **Returns**

        None

    For extra info:

        *https://www.youtube.com/watch?v=C_zFhWdM4ic
    '''

    # We can open two images seperately, and only change img (thus, keeping
    # the original image unchanged for calculation purposes).
    # Note - we convert to RGB to circumvent some issues with different
    # file formats.
    original_img = Image.open(fptr).convert("RGB")
    img = Image.open(fptr).convert("RGB")

    width, height = img.size
    imgpxls = np.array(img)
    a = mask // 2

    for x in range(width):
        for y in range(height):
            pxl = img.getpixel((x, y))
            x_init = max(x - a, 0)
            y_init = max(y - a, 0)

            x_end = min(x + a + 1, width)
            y_end = min(y + a + 1, height)

            window = imgpxls[y_init:y_end, x_init:x_end]

            r, g, b = window.mean(axis=(0,1))
            
            blur = (int(r),int(g), int(b))
            if not blur:
                raise Exception("Blurred pxl must still be calculated.")

            img.putpixel((x, y), blur)
    # Save both images so we can verify if we changed the correct one.
    base_name = '.'.join(fptr.split(".")[0:-1])
    fptr_2 = base_name + "_blurred.png"
    img.save(fptr_2)
    fptr_2 = base_name + "_original.png"
    original_img.save(fptr_2)


def set_luminance(fptr, l_val):
    '''
    Luminance is a method of determining how "bright" the image is. It can
    be easily calculated per pixel with the following formula:

        l_pxl = 0.299 * R + 0.587 * G + 0.114 * B

    Now, for an entire image we can calculate either the total luminance, or
    the average luminance over the whole image:

        l_avg = sum(l_pxl) / N_pxl

    We want to set the luminance of an image to a user specified value,
    allowing us to essentially set how bright our image is. We can use the
    get_pxl_luminance() and get_luminance() functions below to help us.

    **Parameters**

        fptr: *str*
            The name of an image file, with its extension
            (ex. spring.jpg, cat.png).
        l_val: *float*
            The desired luminance to set the image to.

    **Returns**

        None
    '''

    original_img = Image.open(fptr).convert("RGB")
    img = Image.open(fptr).convert("RGB")
    lum_avg = get_luminance(img)
    delta = l_val - lum_avg
    width, height = img.size
    imgpxls = np.array(img)

    for x in range(width):
        for y in range(height):
           img.putpixel((x, y), tuple(x+delta in imgpxls))

    base_name = '.'.join(fptr.split(".")[0:-1])
    fptr_3 = base_name + "_lum.png"
    img.save(fptr_3)


def get_pxl_luminance(pxl):
    '''
    Given a pixel, this function will calculate its luminance.

    **Parameters**

        pxl: *tuple, int*
            A tuple of integers holding RGB values.

    **Returns**

        l_val: *float*
            The pixel luminance.
    '''
    l_pxl = 0.299 * pxl[0] + 0.587 * pxl[1] + 0.114 * pxl[2]
    if not l_pxl:
        raise Exception("Function still needs to be defined.")
    return l_pxl


def get_luminance(img):
    '''
    Returns the average luminance of an image.

    **Parameters**

        img: *PIL.Image*
            A PIL image object.

    **Returns**

        l_val: *float*
            The image luminance.
    '''
    width, height = img.size
    imgpxls = np.array(img)
    l_pxl = []
    
    for x in range(width):
        for y in range(height):
            l_pxl.append(get_pxl_luminance(imgpxls(x,y)))
    l_avg = sum(l_pxl) / (width*height)
    if not l_avg:
        raise Exception("Function still needs to be defined.")
    return l_avg


if __name__ == "__main__":
    fptr = "cat.jpg"
    fptrlum = "cat_lum.jpg"
    blur(fptr)
    set_luminance(fptr, 150.0)
    print(get_luminance(ftpr), get_luminance(fptrlum))
    
