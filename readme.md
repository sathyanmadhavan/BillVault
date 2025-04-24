# Bill OCR Web App

This project is a simple Flask web application that allows users to upload images of bills, extract key information using OCR (Optical Character Recognition), and store the results in a MongoDB database.

## Features

- Upload bill images through a web interface.
- Extract vendor name, amount, and date using `pytesseract`.
- Store raw OCR text and extracted fields in MongoDB.

# MongoDB Storage

- Includes a standalone script to perform basic MongoDB operations (insert, update, delete).