"""
Program Name : Automated Data Shield Backup System
File Name : main.py
Author : Devesh Manoj Narkhede
"""

import os
import schedule
import time

from backup import DataShieldStart
from restore import RestoreBackup
from logger import DisplayHistory


# -------------------------------------------------
# Function Name : Border()
# Description : Prints separator line for UI
# Author : Devesh Manoj Narkhede
# -------------------------------------------------
def Border():
    print("=" * 50)

# -------------------------------------------------
# Function Name : DisplayMenu()
# Description : Displays main menu options
# Author : Devesh Manoj Narkhede
# -------------------------------------------------
def DisplayMenu():
    Border()
    print("AUTOMATED DATA SHIELD BACKUP SYSTEM")
    Border()
    print("1. Start Backup")
    print("2. Restore Backup")
    print("3. View Backup History")
    print("4. Help")
    print("5. Usage")
    print("6. Exit")
    Border()

# -------------------------------------------------
# Function Name : DisplayHelp()
# Description : Displays help information
# Author : Devesh Manoj Narkhede
# -------------------------------------------------
def DisplayHelp():
    Border()
    print("HELP SECTION")
    Border()

    print("This system provides automated backup functionality with the following features:\n")

    print("1. Incremental Backup:")
    print("   -> Copies only new or modified files using hashing technique")
    print()

    print("2. Scheduled Backup:")
    print("   -> Automatically performs backup at given time interval")
    print()

    print("3. Zip Archive Creation:")
    print("   -> Creates compressed backup files with timestamp")
    print()

    print("4. Restore Feature:")
    print("   -> Restores all files from backup zip to desired location")
    print()

    print("5. Logging System:")
    print("   -> Maintains log file of backup operations")
    print()

    print("6. Backup History:")
    print("   -> Stores history of backups with date, file count and size")
    print()

    print("7. Email Notification:")
    print("   -> Sends email after backup completion with log file attachment")

    Border()


# -------------------------------------------------
# Function Name : DisplayUsage()
# Description : Displays usage instructions
# Author : Devesh Manoj Narkhede
# -------------------------------------------------
def DisplayUsage():
    Border()
    print("USAGE & HELP INSTRUCTIONS")
    Border()

    print("1. Start Backup:")
    print("   -> Enter time interval in minutes")
    print("   -> Enter source folder name")
    print("   -> System will automatically backup files")
    print("   -> Only new or modified files are copied")
    print()

    print("2. Restore Backup:")
    print("   -> Enter zip file name (or full path)")
    print("   -> Enter destination folder")
    print("   -> All files from backup will be restored")
    print()

    print("3. View Backup History:")
    print("   -> Displays previous backup details")
    print("   -> Includes date, file count and size")
    print()

    print("4. Help:")
    print("   -> Displays information about system features")
    print()

    print("5. Exit:")
    print("   -> Closes the application")

    Border()

# -------------------------------------------------
# Function Name : StartScheduler()
# Description : Starts scheduled backup at given interval
# Input : interval (int), source (string)
# Output : None
# Author : Devesh Manoj Narkhede
# -------------------------------------------------
def StartScheduler(interval, source):

    print("-" * 50)
    print("Backup Scheduler Started Successfully")
    print("Time Interval (minutes):", interval)
    print("Press Ctrl + C to stop")
    print("-" * 50)

    schedule.every(interval).minutes.do(DataShieldStart, source)

    while True:
        schedule.run_pending()
        time.sleep(1)

# -------------------------------------------------
# Function Name : main()
# Description : Entry point Function 
# Author : Devesh Manoj Narkhede
# -------------------------------------------------
def main():
    while True:
        DisplayMenu()

        choice = input("Enter your choice: ")
        print("-" * 50)

        if choice == "1":
            try:
                interval = int(input("Enter time interval (in minutes): "))
                source = input("Enter folder name to backup: ")

                # Folder existence check 
                if not os.path.exists(source):
                    print("Source folder does not exist")
                else:
                    StartScheduler(interval, source)

            except Exception as e:
                print("Error:", e)

        elif choice == "2":
            zipfile = input("Enter zip file name (or full path): ")
            destination = input("Enter destination folder: ")
            RestoreBackup(zipfile, destination)

        elif choice == "3":
            DisplayHistory()

        elif choice == "4":
            DisplayHelp()

        elif choice == "5":
            DisplayUsage()

        elif choice == "6":
            Border()
            print("Thank you for using Data Shield System")
            Border()
            break

        else:
            print("Invalid choice, please try again.")

        Border()
        input("Press Enter to continue...")

# -------------------------------------------------
# Function Name : main()
# Description : Entry point Function to start the program
# -------------------------------------------------

if __name__ == "__main__":
    main()