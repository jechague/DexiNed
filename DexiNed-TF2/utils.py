#import numpy as np
import tensorflow as tf

def image_normalization(img, img_min=0, img_max=255):
    """This is a typical image normalization function
    where the minimum and maximum of the image is needed
    source: https://en.wikipedia.org/wiki/Normalization_(image_processing)
    :param img: an image could be gray scale or color
    :param img_min:  for default is 0
    :param img_max: for default is 255
    :return: a normalized image, if max is 255 the dtype is uint8
    """
    #img = np.float32(img)
    img = tf.cast(img, tf.float32)
    epsilon=1e-12 # whenever an inconsistent image
    #img = (img-np.min(img))*(img_max-img_min)/((np.max(img)-np.min(img))+epsilon)+img_min
    img = (img-tf.math.reduce_min(img))*(img_max-img_min)/((tf.math.reduce_max(img)-tf.math.reduce_min(img))+epsilon)+img_min
    return img