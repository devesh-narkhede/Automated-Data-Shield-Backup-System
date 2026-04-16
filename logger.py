"""
File Name : logger.py
Description : Handles logging and backup history
Author : Devesh Manoj Narkhede
"""

import os
import time

# -------------------------------------------------
# Function Name : WriteLog()
# Description : Create and append backup log file
# Input : Source (string), Destination (string),
#         files (list), zip_file (string), time_stamp (string)
# Output : log_filename (string)
# Author : Devesh Manoj Narkhede
# -------------------------------------------------
def WriteLog(Source, Destination, files, zip_file, time_stamp):

    os.makedirs("Logs", exist_ok=True)

    log_filename = os.path.join("Logs", "Backup_Log.txt")

    with open(log_filename, "a") as fobj:

        fobj.write("=" * 50 + "\n")
        fobj.write(f"Backup Time : {time_stamp}\n")
        fobj.write(f"Source      : {Source}\n")
        fobj.write(f"Destination : {Destination}\n")

        fobj.write("\nFiles Copied:\n")

        if len(files) == 0:
            fobj.write("No new or modified files\n")
        else:
            for file in files:
                fobj.write(f"{file}\n")

        fobj.write(f"\nTotal Files : {len(files)}\n")
        fobj.write(f"Zip File    : {zip_file}\n")
        fobj.write("=" * 50 + "\n\n")

    return log_filename


# -------------------------------------------------
# Function Name : WriteHistory()
# Description : Maintain backup history
# Input : file_count (int), zip_file (string), time_stamp (string)
# Output : None
# Author : Devesh Manoj Narkhede
# -------------------------------------------------
def WriteHistory(file_count, zip_file, time_stamp):

    history_file = "history.txt"

    size = 0
    if os.path.exists(zip_file):
        size = os.path.getsize(zip_file)

    with open(history_file, "a") as fobj:
        fobj.write(f"{time_stamp} | Files: {file_count} | Size: {size} bytes | {zip_file}\n")


# -------------------------------------------------
# Function Name : DisplayHistory()
# Description : Display backup history
# Input : None
# Output : None
# Author : Devesh Manoj Narkhede
# -------------------------------------------------
def DisplayHistory():

    history_file = "history.txt"

    print("=" * 50)
    print("BACKUP HISTORY")
    print("=" * 50)

    if not os.path.exists(history_file):
        print("No history available.")
        return

    with open(history_file, "r") as fobj:
        data = fobj.read()

        # Display history or message if empty
        if not data.strip():
            print("No history available.")
        else:
            print(data)