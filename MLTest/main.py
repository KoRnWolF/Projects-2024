import keras_ocr
import matplotlib.pyplot as plt

# Create a pipeline with keras-ocr
pipeline = keras_ocr.pipeline.Pipeline()

# Load an image (handwritten text image from IAM Dataset)
image_path = 'data/000/a01-000u.png'
image = keras_ocr.tools.read(image_path)

# Perform OCR prediction
prediction_groups = pipeline.recognize([image])

# Display the image and predictions
keras_ocr.tools.drawAnnotations(image=image, predictions=prediction_groups[0])
plt.imshow(image)
plt.show()

# Print the recognized text
for text, box in prediction_groups[0]:
    print(f"Recognized Text: {text}")
