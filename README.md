# EC7212 – Computer Vision and Image Processing Assignment 2

This repository contains Python implementations of two image segmentation techniques:

1. **Otsu’s Thresholding**: Applied on a synthetic image with added Gaussian noise.
2. **Region Growing Segmentation**: Based on predefined seed points and intensity similarity.

---

## 📁 Files Included

- `task1.py` – Implements Otsu’s thresholding on a noisy synthetic image.
- `task2.py` – Implements region growing using hardcoded seed points.
- `input.jpg` – Grayscale image used for Task 2.
- `region_output.png` – Output of region growing.
- `comparison.png` – Composite image showing Task 1 results.
- `task2_comparison.png` – Comparison of original image and region growing result.
- `requirements.txt` – Python dependencies.
- `README.md` – This documentation file.

---

## 🧪 Task 1: Otsu’s Thresholding

**Title:** Image Segmentation Using Otsu’s Thresholding on Noisy Synthetic Data

**Description:**  
This task creates a synthetic 100×100 image with two objects and a background, each with distinct grayscale intensities. Gaussian noise is added to simulate real-world image imperfections. Otsu’s thresholding is then applied to segment the image into foreground and background automatically.

**Output:**  
- `task1_output.png`: Shows the original image, noisy image, and thresholded result side-by-side.

---

## 🌱 Task 2: Region Growing Segmentation

**Title:** Region Growing-Based Image Segmentation from Seed Points

**Description:**  
This task implements a region growing algorithm to segment an object from a grayscale image. Seed points are defined manually in code. The algorithm recursively includes neighboring pixels that fall within a specified intensity threshold compared to the seed.

**Output:**  
- `region_output.png`: Binary image showing segmented region.
- `task2_comparison.png`: Side-by-side view of original image (with seed markers) and output.

---


## 🛠 Installation

### ✅ 1. Create and activate a virtual environment (optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate
