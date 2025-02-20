from flask import Flask, request, render_template, jsonify
import pytesseract
from PIL import Image
import cv2
import numpy as np

# Initialize Flask app
app = Flask(__name__, static_folder="static", template_folder="templates")

def preprocess_image(image):
    # Convert image to grayscale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, img_thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
    return img_thresh

def extract_text_from_image(file_stream):
    # Read image from in-memory file stream
    file_bytes = np.frombuffer(file_stream.read(), np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    
    # Preprocess and extract text
    preprocessed_image = preprocess_image(image)
    text = pytesseract.image_to_string(preprocessed_image, config="--psm 6 --oem 3")
    return text

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            # Check if file is uploaded
            if 'file' not in request.files:
                return jsonify({"error": "No file uploaded"}), 400
            
            file = request.files['file']
            if file.filename == "":
                return jsonify({"error": "No file selected"}), 400
            
            # Extract text without saving the file locally
            extracted_text = extract_text_from_image(file)
            
            # Return extracted text as JSON response
            response = {
                "text": extracted_text.strip()
            }
            return jsonify(response)
        except Exception as e:
            return jsonify({"error": f"An error occurred: {str(e)}"}), 500

    return render_template("index.html")

if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(debug=False, port=5001)
