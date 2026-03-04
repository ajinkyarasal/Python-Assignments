import smtplib
from email.message import EmailMessage

def send_email(sender_email,app_password, receivers_email,subject,body,report_path = None):
    msg = EmailMessage()
    msg["from"] = sender_email
    msg["to"] = receivers_email
    msg["subject"] = subject
    
    msg.set_content(body)

    if report_path:
        with open(report_path,"rb") as f:
            file_data = f.read()
            file_name = f.name
        
        msg.add_attachment(file_data,
                           maintype="application",
                           subtype="octet-stream",
                           filename=file_name)

    

    smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)
    smtp.login(sender_email,app_password)
    smtp.send_message(msg)

    smtp.quit()
