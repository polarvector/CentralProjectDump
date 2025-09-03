import numpy as np
import cv2
from matplotlib import pyplot as plt

def process_image(image_path):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    # Check if the image is grayscale or color
    if len(image.shape) == 2:  # Grayscale image
        image_float = np.float32(image)
        channels = 1
    else:  # Color image
        image_float = np.float32(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        channels = image.shape[2]

    # Initialize an array for the transformed image
    transformed_image = np.zeros_like(image_float)

    # Process each channel
    for i in range(channels):
        if channels > 1:
            # Extract the i-th channel if color
            channel = image_float[:, :, i]
        else:
            # Use the single channel if grayscale
            channel = image_float

        # Perform the 2D Fourier Transform
        f = np.fft.fft2(channel)
        fshift = np.fft.fftshift(f)

        # Get the magnitude and phase
        magnitude = np.abs(fshift)
        phase = np.angle(fshift)

        # Normalize the magnitude
        magnitude_normalized = magnitude / np.max(magnitude)

        # Combine normalized magnitude with the original phase
        fshift_normalized = np.exp(1j * phase) * 1#magnitude_normalized

        # Inverse FFT to get the resulting image
        f_ishift = np.fft.ifftshift(fshift_normalized)
        image_back = np.fft.ifft2(f_ishift)
        image_back = np.abs(image_back)

        # Store the processed channel
        if channels > 1:
            transformed_image[:, :, i] = image_back
        else:
            transformed_image = image_back

    # Normalize the resulting image for display
    image_back_normalized = cv2.normalize(transformed_image, None, 0, 255, cv2.NORM_MINMAX)
    image_back_normalized = np.uint8(image_back_normalized)

    return image, image_back_normalized

# Process the image
original_image, magnitude_normalized_image = process_image('pix.jpeg')

# Plotting the original and resulting images in a 2x1 subplot
plt.figure(figsize=(10, 8))

# Original image
plt.subplot(2, 1, 1)
if original_image.shape[2] == 3:  # Color image
    plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
else:  # Grayscale image
    plt.imshow(original_image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Magnitude Normalized Image
plt.subplot(2, 1, 2)
if magnitude_normalized_image.shape[2] == 3:  # Color image
    plt.imshow(magnitude_normalized_image)
else:  # Grayscale image
    plt.imshow(magnitude_normalized_image, cmap='gray')
plt.title('Magnitude Normalized Image')
plt.axis('off')

# Show the plots
plt.tight_layout()
plt.show()

# Optionally save the resulting image
cv2.imwrite('dark_magnitude_normalized.jpg', magnitude_normalized_image)
