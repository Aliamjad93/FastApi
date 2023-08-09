import numpy as np
import matplotlib.pyplot as plt
from PIL import Image  # This library is used to read and display images

#Loading Images
image_path = r'C:\Users\farha\.spyder-py3\Software_Tasks\catVsdog\uploaded_images\ali.jfif'  # Replace with the actual path to your image
image = Image.open(image_path)


# Getting values into array of image
image_array = np.array(image)



# Calculate grayscale values using the average of RGB channels, axis=2 will use to get values of rgb
grayscale_image = np.mean(image_array, axis=2).astype(np.uint8)


#display images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image)

plt.subplot(1, 2, 2)
plt.title('Grayscale Image')
plt.imshow(grayscale_image, cmap='gray')

plt.show()


