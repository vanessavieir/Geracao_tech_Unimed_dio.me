from skimage.io import imread,imsave
from sqlalchemy import false

def read_image(path,is_gray=False):
    image=imread(path,as_gray=is_gray)
    return image

def save_images(image,path):
    imsave(path,image)