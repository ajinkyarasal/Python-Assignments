#=========================================
# Program : Simple Gmail Mail Sender
# Purpose : Send mail using Python  SMTP
#=========================================

#smtplib = Pythons library to talk to mail server using SMTP protocol
# SMTP = Simple Mail Transfer Protocol , used for sending emails,
import smtplib 
from email.message import EmailMessage

#Email message helps create a proper email with :
# 1. headers (from/to/subject)
# 2. body (content)
# 3. later you can add attachment too. .

#==================================================
# Function : Marvellous_send_email
# Description : Send email using Gmail SMTP server
#==================================================
#This function does the complete email sending job.
def send_mail(sender,app_password,receiver,subject,body):

    print(sender)
    print(app_password)
    print(receiver)

    #Step 1 : Create Email object,creates an empty email container in memory
    msg = EmailMessage()

    #Step 2 : Set mail headers
    # These are email headers
    # Gmail uses these to show who sent it ,who receives it  and subject line.
    msg["from"] = sender
    msg["to"] = receiver
    msg["subject"] = subject

    #Step 3 : Add email body
    # Adds message body
    # Body can contain multi line content.
    msg.set_content(body)

    #Step 4 : Create SMTP SSL connection manually
    # Create secure smtp connection
    # Connects to GMAILS SMTP server
    # "smtp.gmail.com" = gmail server address
    # 465 = SSL port.secure connection from start.
    #SSL means data is encrypted between your program and Gmail server
    smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)

    #Step 5 : Login using Gmail + App password
    # Authenticates your gmail account using
    # Gmail id and
    # App password (not normal password).
    smtp.login(sender ,app_password)

    #Step 6 : Send Email
    smtp.send_message(msg)

    #Step 7: Close connection
    smtp.quit()

#==================================================
# Function : main
# Description : Driver code
#==================================================
def main():

    #Always use separate temporary/testing account
    sender_email = "studentajinkya@gmail.com"

    #App password generated from Google Account
    #myaccount.google.com/apppasswords, navigate here to generate the password.
    app_password = "fxgo ogum yalb gvfy"

    #Your second email for testing
    receiver_email = "ajinkyarasal26@gmail.com"

    subject = "Test email from Python script"

    body = """Jay Ganesh,
    This is a test email sent using Marvellous  Python.

    Regards,
    Marvellous Infosystem
    """

    send_mail(sender_email,app_password,receiver_email,subject,body)

    print("Marvellous Mail Sent Successfully")

if __name__ == "__main__":
    main()