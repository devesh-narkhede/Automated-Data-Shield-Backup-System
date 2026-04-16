"""
File Name : restore.py
Description : Restore backup from zip file to given destination
Author : Devesh Manoj Narkhede
"""

import os
import zipfile


# -------------------------------------------------
# Function Name : RestoreBackup()
# Description : Extract zip file to destination folder
# Input : zip_file (string), destination (string)
# Output : None
# Author : Devesh Manoj Narkhede
# -------------------------------------------------
def RestoreBackup(zip_file, destination):

    try:
        Border = "-" * 50

        print(Border)
        print("Restore process started")
        print(Border)

        # Check in current path 
        if not os.path.exists(zip_file):
            # Try inside Backups folder 
            zip_file = os.path.join("Backups", zip_file)

            if not os.path.exists(zip_file):
                print("Zip file does not exist")
                return

        # Create destination folder if it doesn't exist
        os.makedirs(destination, exist_ok=True)

        # Extract zip file
        with zipfile.ZipFile(zip_file, 'r') as zobj:
            zobj.extractall(destination)

        print(Border)
        print("Restore completed successfully")
        print("Files extracted to :", destination)
        print(Border)

    except Exception as e:
        print("Error during restore :", e)