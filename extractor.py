import PyPDF2
import argparse
import getpass
import os

def extract_text_from_pdf(pdf_path, pdf_password):

    # Open the PDF file in binary read mode
    with open(pdf_path, 'rb') as file:
        # Create a PDF reader object using PyPDF2
        pdf_reader = PyPDF2.PdfReader(file)

        # Check if the PDF is encrypted
        if pdf_reader.is_encrypted:
            try:
                # Attempt to decrypt the PDF using the provided password
                pdf_reader.decrypt(pdf_password)
            except Exception as e:
                print(f"Failed to decrypt PDF: {e}")
                return  # Exit function if decryption fails

        # Initialize a list to store extracted text for each page
        extracted_text = []
        
        # Loop through each page in the PDF
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]  # Get the specific page
            text = page.extract_text()  # Extract text from the page
            # Append extracted text to list, prefixed by page number for clarity
            extracted_text.append(f"Page {page_num + 1}:\n{text}\n")

    return extracted_text  # Return the list of extracted text

def write_text_to_file(text_list, output_file):
    """
    Writes a list of text strings to a specified output file.
    
    """
    # Convert the output file path to an absolute path
    output_file_path = os.path.abspath(output_file)
    
    # Open the output file in write mode with UTF-8 encoding
    with open(output_file_path, 'w', encoding='utf-8') as f:
        # Write each piece of text from the list to the file
        for text in text_list:
            f.write(text)

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Extract text from a password-protected PDF.")
    
    # Add arguments for input and output file paths
    parser.add_argument('-i', '--input', required=True, help="Path to input PDF file")
    parser.add_argument('-o', '--output', required=True, help="Path to output text file")
    
    # Parse arguments from command line
    args = parser.parse_args()

    # Prompt user for password securely using getpass
    pdf_password = getpass.getpass(prompt='Enter PDF password: ')

    # Extract text from the specified PDF using provided password
    text_list = extract_text_from_pdf(args.input, pdf_password)

    if text_list is not None:  # Ensure extraction was successful before writing
        # Write the extracted text to a specified output file
        write_text_to_file(text_list, args.output)
        print("Text extraction complete.")
    else:
        print("Text extraction failed.")

if __name__ == "__main__":
    main()