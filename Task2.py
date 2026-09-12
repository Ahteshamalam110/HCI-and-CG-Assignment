import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Create image matrix
image = np.zeros((300, 400, 3), dtype=np.uint8)

# Top Left - Red
image[0:150, 0:200] = [255, 0, 0]

# Top Right - Green
image[0:150, 200:400] = [0, 255, 0]

# Bottom Left - Blue
image[150:300, 0:200] = [0, 0, 255]

# Bottom Right - White
image[150:300, 200:400] = [255, 255, 255]

# Print image information
print("Shape:", image.shape)
print("Data type:", image.dtype)
print("Total elements:", image.size)
print("Total memory in bytes:", image.nbytes)

# Show the image
plt.imshow(image)
plt.show()