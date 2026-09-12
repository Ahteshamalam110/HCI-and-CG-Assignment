import numpy as np
import matplotlib.pyplot as plt

# Automatically create an RGB image
image = np.zeros((400, 400, 3), dtype=np.uint8)

# Create four colored areas
image[:200, :200] = [255, 0, 0]
image[:200, 200:] = [0, 255, 0]
image[200:, :200] = [0, 0, 255]
image[200:, 200:] = [255, 255, 0]

print("--- CHANNEL EXTRACTION SUMMARY ---")
print(f"Original Image Shape : {image.shape}")

# Extract RGB channels
red = image[:, :, 0]
green = image[:, :, 1]
blue = image[:, :, 2]

print(f"Red Channel Shape   : {red.shape} | Mean Intensity: {red.mean():.2f}")
print(f"Green Channel Shape : {green.shape} | Mean Intensity: {green.mean():.2f}")
print(f"Blue Channel Shape  : {blue.shape} | Mean Intensity: {blue.mean():.2f}")

# Create isolated channels
red_image = np.zeros_like(image)
red_image[:, :, 0] = red

green_image = np.zeros_like(image)
green_image[:, :, 1] = green

blue_image = np.zeros_like(image)
blue_image[:, :, 2] = blue

# Display
fig, ax = plt.subplots(2, 3, figsize=(12, 8))

ax[0, 0].imshow(red_image)
ax[0, 0].set_title("Red Only")
ax[0, 0].axis("off")

ax[0, 1].imshow(green_image)
ax[0, 1].set_title("Green Only")
ax[0, 1].axis("off")

ax[0, 2].imshow(blue_image)
ax[0, 2].set_title("Blue Only")
ax[0, 2].axis("off")

ax[1, 0].imshow(red, cmap="gray")
ax[1, 0].set_title("Red Intensity")
ax[1, 0].axis("off")

ax[1, 1].imshow(green, cmap="gray")
ax[1, 1].set_title("Green Intensity")
ax[1, 1].axis("off")

ax[1, 2].imshow(blue, cmap="gray")
ax[1, 2].set_title("Blue Intensity")
ax[1, 2].axis("off")

plt.tight_layout()
plt.savefig("task3_channels_output.png", dpi=150)

print("Display Window : Matplotlib 2x3 Subplot Grid Rendered.")

plt.show()