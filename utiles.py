import os
import shutil
from logger import logging

def delete_directory_if_size_exceeds(directory_path, size_limit_in_Megabytes):
    size_limit_in_bytes= size_limit_in_Megabytes * 1024 * 1024
    total_size = 0
    for path, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(path, file)
            total_size += os.path.getsize(file_path)

    if total_size > size_limit_in_bytes:
        shutil.rmtree(directory_path)
        logging.info(f"Directory '{directory_path}' deleted because it exceeded the size limit of {size_limit_in_bytes} bytes.")

