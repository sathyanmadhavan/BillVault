"""Flask app to upload bills, perform OCR using Tesseract, and store results in MongoDB."""

import os
import re
from flask import Flask, request, render_template
from pymongo import MongoClient
from PIL import Image
import pytesseract
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

client = MongoClient("mongodb://localhost:27017/")
db = client["bill_data"]
collection = db["bills"]

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def extract_fields(text):
    """Extract vendor name, amount, and date from OCR text."""
    amount = re.search(r'(?i)(?:₹|rs\.?)\s?([\d,]+\.\d{2}|\d+)', text)
    date = re.search(r'(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})', text)
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    vendor = lines[0] if lines else "Unknown"
    return {
        'vendor': vendor,
        'amount': amount.group() if amount else None,
        'date': date.group() if date else None,
        'raw_text': text
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    """Main route to upload bill, perform OCR, and save to database."""
    if request.method == 'POST':
        file = request.files['bill']
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            image = Image.open(filepath)
            text = pytesseract.image_to_string(image)

            fields = extract_fields(text)
            fields['filename'] = filename

            collection.insert_one(fields)

            return (
                f"<h3>OCR Text saved to DB</h3>"
                f"<pre>{text}</pre>"
                f"<a href='/'>Upload Another</a> | <a href='/bills'>View Bills</a>"
            )

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
