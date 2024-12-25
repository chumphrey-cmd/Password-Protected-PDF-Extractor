
# Simple PDF Text Extractor

## Overview

Simple tool designed to extract text from standard or password-protected PDFs. Prompts the user to input the password securely or press **Enter** if there is no password. It then outputs the extracted text into a specified file or directory of the users choice.

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

- **With directory**

```python
python extractor.py -i '.\path\to\file.pdf' -o '.\path\to\output.txt'
```

- **Without directory**

```python
python extractor.py -i '.\file.pdf' -o 'output.txt'

```

### Command Line Arguments

- `-i`, `--input`: Path to the input PDF file.
- `-o`, `--output`: Path to the output text file.