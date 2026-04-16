"""
File Name : email_sender.py
Description : Sends email with log file attachment after backup
Author : Devesh Manoj Narkhede
"""

import smtplib
from email.message import EmailMessage
import os


# -------------------------------------------------
# Function Name : SendMailWithAttachment()
# Description : Send email with log file attachment
# Input : zip_file (string), log_file (string)
# Output : None
# Author : Devesh Manoj Narkhede
# -------------------------------------------------
def SendMailWithAttachment(zip_file, log_file):

    try:
        sender_email = "your_email@gmail.com"
        app_password = "your_app_password"
        receiver_email = "receiver_email@gmail.com"

        subject = "Backup Completed Successfully"

        body = f"""
        Hello,

        Backup process completed successfully.

        Zip File : {zip_file}

        Please find attached log file.

        Regards,
        Automated Data Shield System
        """

        # Create email
        msg = EmailMessage()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject
        msg.set_content(body)

        # Attach log file
        if os.path.exists(log_file):
            with open(log_file, "rb") as f:
                file_data = f.read()
                file_name = os.path.basename(log_file)

            msg.add_attachment(file_data,
                               maintype="application",
                               subtype="octet-stream",
                               filename=file_name)

        # SMTP connection
        smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)
        smtp.quit()

        print("Email sent successfully with log attachment...")

    except Exception as e:
        print("Failed to send email:", e)
