
# Simple Password PDF Text Extractor

## Overview

The Password PDF Text Extractor is a simple tool designed to extract text from password-protected PDFs. It prompts the user to input the password securely and outputs the extracted text into a specified file.

## Prerequisites

- Python 3.10+
- Required Python packages listed in `requirements.txt`

## Installation

1. **Create a Virtual Environment**:

   ```bash
   python -m venv venv
   ```

2. **Activate the Virtual Environment**:
   - On Windows:

     ```bash
     .\venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

3. **Install Required Packages**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the tool, run the following command in your terminal or command prompt:

```bash
python extractor.py -i "PATH\TO\FILE.pdf" -o "EXAMPLE_FILE.txt"
```

### Command Line Arguments

- `-i`, `--input`: Path to the input PDF file.
- `-o`, `--output`: Path to the output text file.

Upon execution, you will be prompted to enter the password for the PDF securely.
