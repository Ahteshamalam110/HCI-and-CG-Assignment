import numpy as np
import matplotlib.pyplot as plt

# Create an original RGB image
img = np.zeros((400, 400, 3), dtype=np.uint8)

# Add some colors to the image
img[0:200, 0:200] = [255, 0, 0]       # Red
img[0:200, 200:400] = [0, 255, 0]     # Green
img[200:400, 0:200] = [0, 0, 255]     # Blue
img[200:400, 200:400] = [255, 255, 0] # Yellow

print("--- SPATIAL DOWNSAMPLING ---")

# Original image information
print("Original Image Shape:", img.shape)
print("Original Memory:", img.nbytes, "bytes")

# 1. Downsample using N = 8
N = 8
downsampled = img[::N, ::N, :]

print("Downsampled Shape:", downsampled.shape)
print("Downsampled Memory:", downsampled.nbytes, "bytes")

# 2. Re-expand using np.repeat()
expanded = np.repeat(downsampled, N, axis=0)
expanded = np.repeat(expanded, N, axis=1)

# Keep the original size
expanded = expanded[:img.shape[0], :img.shape[1], :]

print("Expanded Shape:", expanded.shape)

# 3. Calculate percentage drop in spatial dimensions
height_drop = (1 - downsampled.shape[0] / img.shape[0]) * 100
width_drop = (1 - downsampled.shape[1] / img.shape[1]) * 100

# Calculate memory footprint drop
memory_drop = (1 - downsampled.nbytes / img.nbytes) * 100

print("Row Dimension Drop:", round(height_drop, 2), "%")
print("Column Dimension Drop:", round(width_drop, 2), "%")
print("Memory Footprint Drop:", round(memory_drop, 2), "%")

# Display original and pixelated images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(expanded)
plt.title("Pixelated Image (N=8)")
plt.axis("off")

plt.tight_layout()
plt.savefig("task4_pixelation_output.png", dpi=150)

plt.show()