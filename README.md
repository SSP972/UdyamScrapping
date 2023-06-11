Download all program files.

Install the requirements specified in the requirements.txt file.

Install Tesseract for captcha resolution. Make sure you have Tesseract installed on your system. You can refer to the Tesseract documentation for installation instructions specific to your operating system.

Go to the getcaptcha.py file.

In the pytesseract.pytesseract.tesseract_cmd line, make sure the path to the Tesseract executable is correct. Modify it if necessary to point to the correct location.

Go to the Read_file.py file.

Set the value of the file_path variable to the path of your CSV file. The CSV file should have a single column named "ID" with values in the format "udyam-xx-00-0000000".

If you have properly installed all the prerequisites, you are good to go and can start scraping the data as many times as needed.
