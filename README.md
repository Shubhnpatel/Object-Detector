Object Detection using OpenCV
A user-friendly tool that allows for the selection and analysis of images to detect and count objects. The system is built on the powerful OpenCV library to handle the image processing components.

Installation
Prerequisites
Ensure you have Python installed on your machine.

Required Libraries
The following Python libraries are essential for the functionality of this tool:

OpenCV
NumPy
Matplotlib
Tkinter
You can install these libraries using pip, the Python package installer.

How to Use
After setting up the prerequisites:

Run the application.
When prompted, select an image from your machine.
The system will process the image and display the count of detected objects in a dialog box.

CODE EXPLAINATION

What the code does:

The code allows a user to select an image file from their computer. It then processes the image to detect and count objects within it. Once it finishes analyzing the image, the code shows the image with the detected objects outlined and then displays the count of those objects in a pop-up dialog.

Breakdown of the code's functionality:

Image Loading and Preparation:

The code starts by reading the chosen image.
It then converts this image into a gray-scale version (basically, a black-and-white version).
To improve the quality of detection, the code slightly blurs the gray-scale image.
Object Detection:

The blurred gray-scale image is processed to create a binary image. In this binary image, potential objects are white, and the background is black.
The code identifies the boundaries (contours) of these white areas, which represent potential objects.
It then filters out very small areas to avoid counting insignificant details or noise as objects.
Visualization:

The code outlines the detected objects on the original image.
This marked image is displayed to the user using a visualization tool.
User Interface:

The code uses a graphical interface (through tkinter) to allow the user to select an image file.
After processing, it also displays the number of detected objects in a pop-up dialog.
