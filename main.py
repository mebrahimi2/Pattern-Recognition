from open_data import open_image, open_csv

directory_name = 'data'
### Open image

#dictionary 
bands = open_image(directory_name)
print(bands.keys())

#numpy array 
image = open_image(directory_name, 'array')
print(image.shape)

### Open ground truth points
ground_truth = "all_data"

#Ground truth points in an array
gtp = open_csv(ground_truth, directory_name)
print(gtp.shape)
#Ground truth points in x, y arrays
x_gtp, y_gtp = open_csv(ground_truth, directory_name, "XY", "ClassName")
print(x_gtp.shape)
print(y_gtp.shape)