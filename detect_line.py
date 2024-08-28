import cv2
import numpy as np
import matplotlib.pyplot as plt


class DetectLines:
    def __init__(self, image_path):
        self.path = image_path

    def detect_lines(self):
        # Load the image in grayscale
        img = cv2.imread(self.path, cv2.IMREAD_GRAYSCALE)

        # Get image dimensions
        height, width = img.shape

        # Initialize a list to store mean values
        mean_values = []

        # Calculate the mean pixel value for each line
        for y in range(height):
            mean_value = np.mean(img[y, :])
            mean_values.append(mean_value)

        # Plot the mean values for each line
        # Plot the mean values for each line
        # plt.figure(figsize=(10, 6))
        # plt.plot(mean_values, label='Mean Pixel Value')
        # plt.title('Mean Pixel Value for Each Line (y-coordinate)')
        # plt.xlabel('Line Number (y-coordinate)')
        # plt.ylabel('Mean Pixel Value')
        # plt.axhline(y=np.mean(mean_values) * 0.9, color='r', linestyle='--', label='Threshold')
        # plt.legend()
        #
        # # Save the plot as an image file
        # plot_save_path = 'mean_values_plot.png'
        # plt.savefig(plot_save_path)

        threshold = 252

        # Initialize variables to store line boundaries
        start_y = None
        end_y = None
        lines = []

        for y in range(height):
            if mean_values[y] < threshold:
                if start_y is None:
                    start_y = y
                end_y = y
            else:
                if start_y is not None and end_y is not None:
                    lines.append((start_y, end_y))
                    start_y = None
                    end_y = None

        # Add the last line if it wasn't closed
        if start_y is not None and end_y is not None:
            lines.append((start_y, end_y))

        # Draw bounding boxes around detected lines
        # output_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        boxes = []
        for i, (start_y, end_y) in enumerate(lines):
            if (end_y-start_y) > 10:
                # cv2.rectangle(output_img, (0, start_y-3), (width, end_y+3), (0, 255, 0), 2)
                boxes.append((0, start_y-3, width, end_y+3))

                # # Save the line as image
                # line_img = img[start_y-3:end_y+3, :]
                # line_img_path = f'lines/line_{i}.png'
                # cv2.imwrite(line_img_path, line_img)

        return boxes

        # Save the result image with bounding boxes
        # result_image_path = 'path_to_save_result_image.jpg'
        # cv2.imwrite(result_image_path, output_img)
