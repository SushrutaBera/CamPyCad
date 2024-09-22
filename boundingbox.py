import cv2 as cv
import numpy as np
import os
import random

data_dir = 'photos\dataset_final'
labels = os.listdir(data_dir)  # battery, resistor, etc
row = np.zeros((120, 1, 3))
picture = np.zeros((1, 700, 3))
bounding_boxes = []  # List to store bounding box information

# Loop to generate images and draw bounding boxes
for i in range(5):
    rowbounding = []
    for j in range(5):
        # One of labels (eg. battery)
        label = os.path.join(data_dir, labels[random.randint(0, len(labels) - 1)])
        # One of image of label
        img = os.listdir(label)[random.randint(0, len(os.listdir(label)) - 1)]
        # Converting to CV image
        img = cv.imread(os.path.join(label, img))

        # Random gap to insert in left
        L_img = np.concatenate((np.zeros((120, random.randint(10, 50), 3)), img), axis=1)  # add to left

        # Calculate bounding box coordinates
        x0 = random.randint(10, 50)  # Starting x-coordinate
        y0 = random.randint(10, 100)  # Starting y-coordinate
        x1 = x0 + img.shape[1]  # Ending x-coordinate
        y1 = y0 + img.shape[0]  # Ending y-coordinate

        # Draw bounding box on the image
        cv.rectangle(L_img, (x0, y0), (x1, y1), (0, 255, 0), 2)  # Green rectangle

        cv.imshow(f'img{j}', L_img)

        # Store image and bounding box coordinates
        bounding_boxes.append((label, img.copy(), x0, y0, x1, y1))  # Include a copy of the image

        # Concatenate the current image with the row
        if str(row) == str(np.zeros((120, 1, 3))):
            row = L_img
        else:
            row = np.concatenate((row, img), axis=1)

    # Concatenate the current row with the picture
    if str(picture) == str(np.zeros((120, 1, 3))):
        picture = row
        row = np.zeros((120, 1, 3))
    else:
        row_w = row.shape[1]
        remaining = 5 * (120 + 20) - row_w
        if remaining != 0:
            row = np.concatenate((row, np.zeros((120, max(remaining, 0), 3))), axis=1)
        picture = np.concatenate((picture, row), axis=0)
        row = np.zeros((120, 1, 3))

# Add a random bottom border
picture = np.concatenate((picture, np.zeros((random.randint(10, 20), 700, 3))), axis=0)

# Display the final image with bounding boxes
cv.imshow('picture', picture)
cv.waitKey(0)

# imgdir, x0y0 x1y1 component (available in bounding_boxes)