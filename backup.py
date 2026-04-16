"""
File Name : backup.py
Description : Performs backup of files, creates zip, logs details and sends email
Author : Devesh Manoj Narkhede
"""

import os
import time
import shutil

from utils import calculate_hash, make_zip
from logger import WriteLog, WriteHistory
from email_sender import SendMailWithAttachment


# -------------------------------------------------
# Function Name : BackupFiles()
# Description : Copy new or modified files from source to destination
# Input : Source (string), Destination (string)
# Output : copied_files (list)
# Author : Devesh Manoj Narkhede
# -------------------------------------------------
def BackupFiles(Source, Destination):

    copied_files = []

    os.makedirs(Destination, exist_ok=True)

    for root, dirs, files in os.walk(Source):
        for file in files:

            src_path = os.path.join(root, file) 
            relative = os.path.relpath(src_path, Source) # Convert to relative path for destination
            dest_path = os.path.join(Destination, relative) 

            os.makedirs(os.path.dirname(dest_path), exist_ok=True) # Create nested folders if they don't exist

            # Copy the files if it's new or modified
            if (not os.path.exists(dest_path)) or \
               (calculate_hash(src_path) != calculate_hash(dest_path)):

                shutil.copy2(src_path, dest_path)
                copied_files.append(relative)

    return copied_files


# -------------------------------------------------
# Function Name : DataShieldStart()
# Description : Start backup process with logging and email
# Input : Source (string)
# Output : None
# Author : Devesh Manoj Narkhede
# -------------------------------------------------
def DataShieldStart(Source="Data"):

    try:
        Border = "-" * 50
        display_time = time.strftime("%Y-%m-%d %H:%M:%S")

        # Folder existence check
        if not os.path.exists(Source):
            print("Source folder does not exist")
            return False

        print(Border)
        print("Backup process started at :", display_time)
        print(Border)

        BackupFolder = os.path.join("Backups", "Backup_Files")

        files = BackupFiles(Source, BackupFolder)

        zip_file = make_zip(BackupFolder)

        print(Border)
        print("Backup completed successfully")

        if len(files) == 0:
            print("No new or modified files found")
        else:
            print("Files copied :", len(files))

        print("Zip file created :", zip_file)
        print("Completed at :", display_time)
        print(Border)

        # Logging, History and Email
        log_file = WriteLog(Source, BackupFolder, files, zip_file, display_time)
        WriteHistory(len(files), zip_file, display_time)
        SendMailWithAttachment(zip_file, log_file)
        return True    

    except Exception as e:
        print("Error occurred :", e)
        return False  