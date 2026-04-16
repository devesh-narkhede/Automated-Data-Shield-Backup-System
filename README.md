# Automated Data Shield Backup System

This project is an automated backup system developed using Python.  
It performs incremental backup of files and creates zip archive for storage and restore.

---

## Technology Used

Language:
- Python

Libraries and Modules:
- os (file and directory handling)
- shutil (file operations)
- hashlib (MD5 hashing for file comparison)
- zipfile (creating zip archives)
- schedule (task scheduling)
- smtplib and email (sending email with attachment)

---

## Features

- Incremental Backup (only new and modified files are copied)
- Automatic Backup using Scheduler
- Zip file creation with timestamp
- Restore backup from zip file
- Logging system (single log file)
- Backup history tracking
- Email notification with log attachment
- Menu driven user interface

---

## How it Works

- The system checks files using hashing technique
- Only new or modified files are copied to backup folder
- Backup folder is compressed into zip file
- Log file and history are updated
- Email is sent after backup completion

---

## Project Structure

Project/
- main.py  
- backup.py  
- utils.py  
- logger.py  
- restore.py  
- email_sender.py  

Note:  
The following are created automatically when the program runs:
- Backups/  
- Logs/  
- history.txt  

---

## How to Run

1. Open terminal in project folder  
2. Run the program: python main.py  
3. Select option from menu  

---

## Usage

1. Start Backup  
   -> Enter time interval  
   -> Enter source folder  
   -> Backup runs automatically  

2. Restore Backup  
   -> Enter zip file name  
   -> Enter destination folder  

3. View History  
   -> Shows previous backup details  

---

## Note

- Source folder must exist before backup  
- Backup runs continuously until stopped (Ctrl + C)  
- Email requires valid Gmail app password  

---

## Author

Devesh Manoj Narkhede
