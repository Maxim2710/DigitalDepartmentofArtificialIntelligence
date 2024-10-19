import matplotlib.pyplot as plt
from PIL import Image

image = Image.open('Lenna.png')
image_resized = image.resize((128, 128))

plt.imshow(image_resized)
plt.axis('off')
plt.show()

print('1')