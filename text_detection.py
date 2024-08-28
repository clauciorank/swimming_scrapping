import easyocr
import cv2


class TextDetection:
    def __init__(self, image_path, boxes):
        self.path = image_path
        self.image = cv2.imread(self.path)
        self.reader = easyocr.Reader(['pt'])
        self.boxes = boxes

    def detect_text(self):
        all_text = []
        for n, i in enumerate(self.boxes):
            print(f'Reading text from line {n+1}')
            # Path to your image
            x_start, y_start, x_end, y_end = i
            image = self.image.copy()
            image = image[y_start:y_end, x_start:x_end]

            # Perform OCR
            results = self.reader.readtext(image)

            # Draw bounding boxes around detected text boxes
            text_ = []
            for (bbox, text, prob) in results:
                text_.append(text)
                # (top_left, top_right, bottom_right, bottom_left) = bbox
                # top_left = tuple(map(int, top_left))
                # bottom_right = tuple(map(int, bottom_right))
                # cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
                # cv2.putText(image, text, top_left, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            all_text.append(text_)

        return all_text
