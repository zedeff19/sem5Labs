import numpy as np
import cv2

def gaussian_blur(image, kernel_size=5, sigma=1):
    """Apply Gaussian Blur to an image."""
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), sigma)

def compute_gradients(image):
    """Compute image gradients using Sobel filters."""
    sobel_x = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]])
    
    sobel_y = np.array([[1, 2, 1],
                        [0, 0, 0],
                        [-1, -2, -1]])

    Ix = cv2.filter2D(image, -1, sobel_x)
    Iy = cv2.filter2D(image, -1, sobel_y)
    return Ix, Iy

def harris_response(Ix, Iy, k=0.04):
    """Compute the Harris response."""
    Ixx = Ix * Ix
    Iyy = Iy * Iy
    Ixy = Ix * Iy
    
    # Gaussian filter to smooth the components
    Sxx = cv2.GaussianBlur(Ixx, (5, 5), 1)
    Syy = cv2.GaussianBlur(Iyy, (5, 5), 1)
    Sxy = cv2.GaussianBlur(Ixy, (5, 5), 1)
    
    # Determinant and trace
    det_M = (Sxx * Syy) - (Sxy ** 2)
    trace_M = Sxx + Syy
    
    # Harris response
    R = det_M - k * (trace_M ** 2)
    return R

def non_maximum_suppression(R, threshold):
    """Apply non-maximum suppression."""
    corners = np.zeros_like(R)
    corners[R > threshold] = R[R > threshold]
    
    # Apply dilation to find local maxima
    dilated = cv2.dilate(corners, None)
    corners = np.where((corners == dilated), corners, 0)
    return corners

def harris_corner_detector(image, k=0.04, threshold=1e-5):
    """Main function to run Harris Corner Detection."""
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_image = np.float32(gray_image)  # Convert to float

    Ix, Iy = compute_gradients(gray_image)
    R = harris_response(Ix, Iy, k)
    corners = non_maximum_suppression(R, threshold)

    return corners

# Load an image
image = cv2.imread('./Scripts/img.png')
corners = harris_corner_detector(image)

# Display the results
output_image = image.copy()
output_image[corners > 0] = [0, 0, 255]  # Mark corners in red

cv2.imshow('Harris Corners', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
