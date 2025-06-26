import numpy as np
import cv2
import matplotlib.pyplot as plt

# Step 1: Create synthetic image
image = np.zeros((100, 100), dtype=np.uint8)
image[20:50, 20:50] = 127   # Object 1
image[60:90, 60:90] = 255   # Object 2


cv2.imwrite("original.png", image)

# Add Gaussian noise
noise = np.random.normal(0, 20, image.shape).astype(np.float32)
noisy_float = image.astype(np.float32) + noise
noisy_image = np.clip(noisy_float, 0, 255).astype(np.uint8)

cv2.imwrite("noisy.png", noisy_image)

# Apply Otsu’s thresholding
_, otsu_thresh = cv2.threshold(noisy_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imwrite("otsu.png", otsu_thresh)


plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Noisy Image')
plt.imshow(noisy_image, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Otsu's Threshold")
plt.imshow(otsu_thresh, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.savefig("comparison.png", dpi=300)  
print("All images saved successfully.")
