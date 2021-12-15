from open_data import open_image

directory_name = 'data'

## dictionary 
bands = open_image(directory_name)
print(bands.keys())

## numpy array 
image = open_image(directory_name, 'array')
print(image.shape)
    