import time
from playwright.sync_api import sync_playwright
import os
from getcaptcha import extract_text
from utiles import delete_directory_if_size_exceeds
from logger import logging

#version 2.0
def Scrap(id_input):
    with sync_playwright() as playwright:

        while True:
            browser = playwright.chromium.launch()
            context = browser.new_context()
            page = context.new_page()

            page.goto('https://udyamregistration.gov.in/Udyam_Verify.aspx', timeout=60000)  # Replace with the actual URL of the webpage

            # Find the captcha image element
            page.wait_for_selector('img#ctl00_ContentPlaceHolder1_imgCaptcha')
            element = page.query_selector('img#ctl00_ContentPlaceHolder1_imgCaptcha')
            bounding_box = element.bounding_box()

            # Create the 'cap_temp' directory if it doesn't exist
            os.makedirs('cap_temp', exist_ok=True)
            # Get ID as input
            # id_input = 'UDYAM-MH-01-0000006'
            # input('Enter the ID: ')

            # Save the captcha image
            file_name = f"cap_temp/{id_input}.jpg"
            logging.info('Saving the image file....')
            page.screenshot(path=file_name, clip={
                'x': bounding_box['x'],
                'y': bounding_box['y'],
                'width': bounding_box['width'],
                'height': bounding_box['height']
            })

            page.fill('input[name="ctl00$ContentPlaceHolder1$txtUdyamNo"]', id_input)
            captcha_input = extract_text(file_name)
            if len(captcha_input)!=6:
                continue
            page.fill('input[name="ctl00$ContentPlaceHolder1$txtCaptcha"]', captcha_input)

            # Click the verification button
            page.click('input[name="ctl00$ContentPlaceHolder1$btnVerify"]')

            time.sleep(2)  # Wait for 2 seconds for the next page to load

            # Get the new page that opens after clicking Verify
            new_page = context.pages[-1]

            # Wait for the new page to load
            new_page.wait_for_load_state('networkidle')


            # Check if the verification code is incorrect
            if 'ctl00_ContentPlaceHolder1_lblCaptcha' in page.content():
                logging.info("Incorrect verification code. Please try again.\n")
                # Close the browser before rerunning the program
                context.close()
                browser.close()
                continue
            # Save the HTML content of the new page
            file_name = f"data_files/{id_input}.html"
            html_content = new_page.content()
            logging.info('Saving the data file....')
            os.makedirs('data_files', exist_ok=True)
            with open(file_name, "w") as files:
                files.write(html_content)

            # Close the browser
            context.close()
            browser.close()
            break
    delete_directory_if_size_exceeds('cap_temp',5)
# if __name__ == '__main__':
#     main()

#### Version 1
# def main():
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False)
#         context = browser.new_context()
#         page = context.new_page()
#
#         page.goto('https://udyamregistration.gov.in/Udyam_Verify.aspx',timeout=60000)  # Replace with the actual URL of the webpage
#
#
#         # Find the captcha image element
#         page.wait_for_selector('img#ctl00_ContentPlaceHolder1_imgCaptcha')
#         element = page.query_selector('img#ctl00_ContentPlaceHolder1_imgCaptcha')
#         bounding_box = element.bounding_box()
#
#         # Create the 'cap_temp' directory if it doesn't exist
#         os.makedirs('cap_temp', exist_ok=True)
#         # Get ID as input
#         id_input = 'UDYAM-MH-01-0000009'
#         # input('Enter the ID: ')
#
#         # Save the captcha image
#         file_name = "cap_temp/{id_input}.jpg"
#         print('Saving the image file....')
#         page.screenshot(path=file_name, clip={
#             'x': bounding_box['x'],
#             'y': bounding_box['y'],
#             'width': bounding_box['width'],
#             'height': bounding_box['height']
#         })
#
#         page.fill('input[name="ctl00$ContentPlaceHolder1$txtUdyamNo"]', id_input)
#         page.fill('input[name="ctl00$ContentPlaceHolder1$txtCaptcha"]', input('Enter the Captcha: '))
#
#         # Click the verification button
#         page.click('input[name="ctl00$ContentPlaceHolder1$btnVerify"]')
#
#         time.sleep(2)  # Wait for 2 seconds for the next page to load
#
#         # Get the new page that opens after clicking Verify
#         new_page = context.pages[-1]
#
#         # Wait for the new page to load
#         new_page.wait_for_load_state('networkidle')
#         time.sleep(2)
#
#         # Save the HTML content of the new page
#         file_name = f"data_files/{id_input}.html"
#         html_content = new_page.content()
#         print('Saving the data file....')
#         os.makedirs('data_files', exist_ok=True)
#         with open(file_name, "w") as files:
#             files.write(html_content)
#
#         # Close the browser
#         context.close()
#         browser.close()
#
# if __name__ == '__main__':
#     main()
