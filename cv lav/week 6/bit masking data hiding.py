import cv2
import numpy as np

def embed_information(image, secret_data):
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Include length of the secret data at the beginning
    data_length = len(secret_data)
    secret_data = f"{data_length:04d}" + secret_data  # Prefix length as a 4-digit number

    # Ensure secret data fits within the image
    if len(secret_data) > gray_image.size:
        raise ValueError("Secret data is too large to fit in the image.")

    # Convert secret data to binary
    secret_binary = ''.join(format(byte, '08b') for byte in secret_data.encode())

    # Flatten the grayscale image to a 1D array
    flat_image = gray_image.flatten()

    # Embed secret data into the least significant bit (LSB)
    for i in range(len(secret_binary)):
        flat_image[i] = (flat_image[i] & 0xFE) | int(secret_binary[i])

    # Reshape back to original image dimensions
    encoded_image = flat_image.reshape(gray_image.shape)

    return encoded_image

def contrast_stretching(image):
    min_val = np.min(image)
    max_val = np.max(image)
    new_min = 0
    new_max = 255
    stretched_image = (image - min_val) * (new_max - new_min) / (max_val - min_val) + new_min
    return np.uint8(stretched_image)

# Read the image
image = cv2.imread('C:/Users/student/PycharmProjects/220962432_lab6/.venv/Scripts/images/skewed.png')

# Secret data to embed
secret_data = "HadoopTheSpark"

# Embed the secret data
encoded_image = embed_information(image, secret_data)

# Apply contrast stretching
stretched_encoded_image = contrast_stretching(encoded_image)

# Save the resulting image
cv2.imwrite('./images/stretched_encoded_image.jpg', stretched_encoded_image)
