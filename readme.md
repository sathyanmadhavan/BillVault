# BillVaultWeb App

This project is a simple Flask web application that allows users to upload images of bills, extract key information using OCR (Optical Character Recognition), and store the results in a MongoDB database.

## Features

- Upload bill images through a web interface.
- Extract vendor name, amount, and date using `pytesseract`.
- Store raw OCR text and extracted fields in MongoDB.

# MongoDB Storage

- Includes a standalone script to perform basic MongoDB operations (insert, update, delete).


## Prerequisites

Before running the project, ensure you have the following installed on your machine:

- Python 3.7+
- MongoDB (Local or Atlas)
- Tesseract OCR (see below for installation)

## Installation

1. **Clone this repository:**

   ```bash
   git clone https://github.com/<your-username>/bill-scanner.git
   cd bill-scanner

2. **Create and activate a virtual environment:**


    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate` 

3. **Install the required dependencies:**

    pip install -r requirements.txt

4. **Install Tesseract OCR:**

    For windows: https://github.com/UB-Mannheim/tesseract/wiki

    On Linux:

    sudo apt install tesseract-ocr

 - After installing in windows make sure to add the path in environment varibales for smooth usage.

 **Find the Tesseract installation path:**

    - By default, Tesseract is installed at:
        C:\Program Files\Tesseract-OCR


**Open Environment Variables:**

    - Press Win + S to open the search bar and type "Environment Variables".

    - Click on "Edit the system environment variables".

    - In the System Properties window, click the "Environment Variables…" button.

**Edit the Path variable:**

    - Under System variables, scroll down and select the Path variable, then click Edit.

    - Add Tesseract path to the Path variable:

    - In the Edit window, click New and add the Tesseract installation path:

        C:\Program Files\Tesseract-OCR

    -Click OK to save the changes and close all windows.


**Usage**

1. **Start the Flask development server:**

        python app.py

2. Open your browser and go to http://127.0.0.1:5000.

3. Upload a bill and the app will extract details (amount, date, vendor) and store them in the database.

