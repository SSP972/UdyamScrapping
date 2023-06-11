import pandas as pd
from Scraping import Scrap
from logger import logging
import time
def Read_csv(csv_file_path):
    try:
        data=pd.read_csv(csv_file_path)
        for val in data.ID.values:
            Scrap(val)
    except Exception as e:
        logging.error(e)

file_path=r'C:\Users\patil\Documents\udyam.csv'

Read_csv(file_path)