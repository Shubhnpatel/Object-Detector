import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt


def count_objects(image_path):
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Could not load image at {image_path}")

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to the grayscale image (optional but can improve results)
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Threshold the image to binarize
    _, thresh = cv2.threshold(blurred_image, 127, 255, cv2.THRESH_BINARY)

    # Find contours from the binary image
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Filter out very small contours by some criteria (e.g., size, shape, etc.)
    filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 100]  # for example, area > 100 pixels

    # (Optional) Draw contours on the original image (for visualizing)
    final_image = cv2.drawContours(image.copy(), filtered_contours, -1, (0, 255, 0), 3)

    # The number of objects is essentially the number of contours
    object_count = len(filtered_contours)

    # Use matplotlib to display the image
    final_image_rgb = cv2.cvtColor(final_image, cv2.COLOR_BGR2RGB)  # Convert from BGR to RGB
    plt.imshow(final_image_rgb)
    plt.title('Detected Objects')
    plt.show()

    return object_count


def select_image_and_count_objects():
    # Initialize tkinter
    root = tk.Tk()
    root.withdraw()  # We don't want a full GUI, so keep the root window from appearing

    # Show an "Open" dialog box and return the path to the selected file
    image_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.jpeg *.png")])  # You can add more file types if needed.

    if not image_path:  # The user closed the dialog without choosing a file.
        print("No file selected. Exiting...")
        return

    try:
        number_of_objects = count_objects(image_path)
        print(f"Number of objects: {number_of_objects}")
    except Exception as e:
        print(e)


# Execute the function to start the process
select_image_and_count_objects()
