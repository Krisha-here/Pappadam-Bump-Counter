import cv2
import matplotlib.pyplot as plt

# Corrected path to the image
img = cv2.imread("home-product-img2.png")  # or use full path

# Check if the image was loaded successfully
if img is None:
    print("Error: Image not found or path is incorrect")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Adaptive thresholding
thresh = cv2.adaptiveThreshold(blurred, 255,
                               cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY_INV, 11, 3)

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours
output = img.copy()
cv2.drawContours(output, contours, -1, (0, 255, 0), 1)

print("Bump count:", len(contours))

# Show images
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title("Thresholded")
plt.imshow(thresh, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Contours")
plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.tight_layout()
plt.show()
