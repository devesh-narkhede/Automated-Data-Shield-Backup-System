"""
File Name : utils.py
Description : Utility functions for hashing and zip creation
Author : Devesh Manoj Narkhede
"""

import os
import time
import hashlib
import zipfile


# -------------------------------------------------
# Function Name : calculate_hash()
# Description : Generate MD5 hash of given file
# Input : path (string) - path of file
# Output : hexdigest (string) - MD5 hash value
# Author : Devesh Manoj Narkhede
# -------------------------------------------------
def calculate_hash(path):
    hobj = hashlib.md5()

    with open(path, "rb") as fobj:
        while True:
            # Read file in chunks to handle large files
            data = fobj.read(1024)
            if not data:
                break
            hobj.update(data)

    return hobj.hexdigest()


# -------------------------------------------------
# Function Name : make_zip()
# Description : Create zip archive of given folder
# Input : folder (string) - folder to zip
#         output_folder (string) - destination folder for zip (default : "Backups")
# Output : zip_name (string) - created zip file path
# Author : Devesh Manoj Narkhede
# -------------------------------------------------
def make_zip(folder, output_folder="Backups"):

    os.makedirs(output_folder, exist_ok=True) # Create output folder if it doesn't exist

    # Timestamp for unique zip
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    folder_name = os.path.basename(folder)

    zip_name = os.path.join(output_folder, f"{folder_name}_{timestamp}.zip")

    # Create zip file
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zobj:

        for root, dirs, files in os.walk(folder):
            for file in files:
                full_path = os.path.join(root, file)
                relative = os.path.relpath(full_path, folder)

                zobj.write(full_path, relative)

    return zip_name