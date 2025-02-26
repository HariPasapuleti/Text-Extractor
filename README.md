# 🖼️ Image Text Extractor

A Flask-powered web application that extracts text from images using **Tesseract OCR**. The app supports image preprocessing for improved accuracy, an intuitive interface, and the ability to download extracted text.
 

## 🌟 Features

- **OCR-Based Text Extraction**: Leverages Tesseract OCR for reliable text recognition.
- **Preprocessing for Accuracy**: Automatically preprocesses images (grayscale and thresholding).
- **Image Preview**: See your uploaded image before processing.
- **Text Export**: Download extracted text as a `.txt` file with a single click.
- **Responsive UI**: A mobile-friendly, modern interface.

---

## 🚀 Live Demo

You can view a live demo of the app [here](https://your-demo-link.com)  

---

## 🛠️ Tech Stack

- **Backend**: Flask, Python
- **Frontend**: HTML, CSS, JavaScript
- **Image Processing**: OpenCV, Pillow (PIL)
- **OCR**: Tesseract OCR

---

## 🧑‍💻 Installation Guide

### Prerequisites
1. **Python 3.7+**
2. **Tesseract OCR**:
   - Windows: [Download Tesseract](https://github.com/tesseract-ocr/tesseract).
   - Linux/Mac:
     ```bash
     sudo apt install tesseract-ocr
     ```
 
### Steps to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/HariPasapuleti/Text-Extractor.git
   cd Text-Extractor
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure Tesseract path:
   - Windows:
     ```python
     pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
     ```
   - Linux/Mac: No changes needed (default path).

4. Start the Flask server:
   ```bash
   python text_extractor.py
   ```
<!--
5. Open the app in your browser:
   ```
   http://localhost:5000
   ```
-->

---
## 🖥️ Usage

1. **Upload an Image**: Accepts `.jpg` or `.png` formats.
2. **Preview**: Check the image preview before processing.
3. **Extract Text**: View extracted text directly on the page.
4. **Download**: Save the extracted text as a `.txt` file.

