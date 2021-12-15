from PIL import Image
import numpy as np
from glob import glob


def open_image(directory, output_type=None):
    """
    Opens all the image bands have in a directory.
    
    The default output is a dictionary.
    
    Args:
        directory (string): 
        output_type (string, optional): If you want your output to be a array, Please enter "array".
        Defaults to None.
    """
    bands = {}
    for filename in glob(directory + '/*.tif'):
        band_name = filename.split(directory + '\\')[1].split(".")[0]
        band = Image.open(filename)
        band_array = np.array(band)
        bands[band_name] = band_array
    if output_type:
        keylist = [*bands.keys()]
        head = keylist[0].rstrip('0123456789')
        head_length = len(head)
        band_number = [int(key[head_length:]) for key in keylist]
        band_number.sort()
        band_list = []
        for number in band_number:
            key = head + str(number)
            band_list.append(bands[key])
        image_array = np.stack(band_list,axis=2)
        return image_array
    else:
        return bands