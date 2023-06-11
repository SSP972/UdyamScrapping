import cv2
import pytesseract
import re

# Path to the Tesseract executable (update this if necessary)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def preprocess_image(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    return gray
def extract_text(image_path):
    # Preprocess the image
    gray = preprocess_image(image_path)

    # Perform OCR on the preprocessed image
    text = pytesseract.image_to_string(gray)
    text=re.sub(r'\s', '', text)
    return text
