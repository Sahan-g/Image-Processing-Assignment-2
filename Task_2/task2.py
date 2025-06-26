import numpy as np
import cv2
import matplotlib.pyplot as plt

# ----------------------------
# Region Growing Function
# ----------------------------
def region_growing(img, seed_points, threshold=10):
    output = np.zeros_like(img, dtype=np.uint8)
    visited = np.zeros_like(img, dtype=bool)
    h, w = img.shape

    for seed in seed_points:
        if visited[seed]:
            continue
        stack = [seed]
        seed_val = int(img[seed])

        while stack:
            x, y = stack.pop()
            if visited[x, y]:
                continue
            visited[x, y] = True
            output[x, y] = 255

            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < h) and (0 <= ny < w) and not visited[nx, ny]:
                        if abs(int(img[nx, ny]) - seed_val) < threshold:
                            stack.append((nx, ny))
    return output

# ----------------------------
# Step 1: Load grayscale image
# ----------------------------
image = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise FileNotFoundError("input.jpg not found")

# ----------------------------
# Pick values based on known object locations
seed_points = [(200, 500), (700, 600),(300,350),(200, 450), (300, 75)]  

# ----------------------------
# Step 3: Apply Region Growing
# ----------------------------
region_output = region_growing(image, seed_points, threshold=15)

# Save region output
cv2.imwrite("region_output.png", region_output)

# ----------------------------
# Step 4: Plot and Save Comparison
# ----------------------------
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.title("Original + Seeds")
plt.imshow(image, cmap='gray')
for y, x in seed_points:
    plt.plot(x, y, 'ro', markersize=5)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Region Growing Output")
plt.imshow(region_output, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.savefig("task2_comparison.png", dpi=300)
print("All images saved successfully.")
