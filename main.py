"""COPYRIGHT © 2025-2026 可爱牛奶盒 ALL RIGHTS RESERVED"""
import json
import os
import smtplib
import time
import webbrowser
from email.header import Header
from email.mime.text import MIMEText
if os.path.exists(".json"):
    try:
        with open(".json","r",encoding="utf-8") as f:
            data = json.load(f)
        if "smtpserver" in data:
            smtpserver = data["smtpserver"]
        else:
            exit("ERROR - SMTP SERVER UNKNOWN")
        if "smtpport" in data:
            smtpport = data["smtpport"]
        else:
            exit("ERROR - SMTP PORT UNKNOWN")
        if "fromemail" in data:
            frommail = data["fromemail"]
        else:
            exit("ERROR - FROM EMAIL UNKNOWN")
        if "toemail" in data:
            tomail = data["toemail"]
        else:
           exit("ERROR - TO EMAIL UNKNOWN")
        if "type" in data:
            type = data["type"]
        else:
            exit("ERROR - EMAIL TYPE UNKNOWN")
        if "password" in data:
            password = data["password"]
        else:
            exit("ERROR - EMAIL PASSWORD UNKNOWN")
        if "subject" in data:
            subject = data["subject"]
        else:
            exit("ERROR - EMAIL SUBJECT UNKNOWN")
    except Exception as e:
        exit(e)
else:
    exit("ERROR - FILE NOT FOUND")
if os.path.exists(".content"):
    try:
        with open(".content","r") as file:
            content = file.read()
    except Exception as e:
        exit(e)
else:
    exit("ERROR - FILE NOT FOUND")
msg = MIMEText(content,type,"utf-8")
msg["From"] = frommail
msg["To"] = tomail
msg["Subject"] = Header(subject,"utf-8")
try:
    server = smtplib.SMTP_SSL(smtpserver,smtpport)
    server.login(frommail,password)
    server.sendmail(frommail,tomail,msg.as_string())
    server.quit()
    print("EMAIL SENT SUCCESSFULLY")
except Exception as e:
    print(e)