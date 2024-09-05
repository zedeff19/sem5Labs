import cv2
import numpy as np

def retrieve_information(image):
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Flatten the image to a 1D array
    flat_image = gray_image.flatten()

    # Extract the least significant bits
    secret_binary = ''.join(str(pixel & 1) for pixel in flat_image)

    # Extract the length of the secret data (first 4 bytes)
    length_binary = secret_binary[:32]  # 4 bytes for length (4 * 8 bits)
    data_length = int(length_binary, 2)

    # Extract the secret data
    secret_binary = secret_binary[32:32 + data_length * 8]
    secret_data = ''.join(chr(int(secret_binary[i:i + 8], 2)) for i in range(0, len(secret_binary), 8))

    return secret_data

# Read the contrast-stretched image
image = cv2.imread('./images/stretched_encoded_image.jpg')

# Retrieve the secret data
secret_data = retrieve_information(image)
print("Retrieved Secret Data:", secret_data)
