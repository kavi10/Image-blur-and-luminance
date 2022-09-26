'''
EN.640.635 Software Carpentry
Lab 3 - PIL Image Blurring and Luminance

In this lab assignment, we want to write two functions that can manipulate
images: one to blur the image and one to set the luminance (or brightness) of
the image.
'''
from PIL import Image


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

    for x in range(width):
        for y in range(height):
            pxl = img.getpixel((x, y))

            ### INSERT YOUR CODE HERE
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

    ### INSERT YOUR CODE HERE
    raise Exception("Function still needs to be defined.")


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

    ### INSERT YOUR CODE HERE
    raise Exception("Function still needs to be defined.")


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

    ### INSERT YOUR CODE HERE
    raise Exception("Function still needs to be defined.")


if __name__ == "__main__":
    fptr = "cat.jpg"
    blur(fptr)
    set_luminance(fptr, 150.0)
