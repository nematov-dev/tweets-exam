import datetime


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import threading

import queries
import utils


def send_verfication_code(email: str,code:int):
    sender_email = "saidakbarnematov2509@gmail.com"
    password = "mizv kktd uldu haij"

    subject = "Verification Code"
    body = f"Your verfication code: {code}"
    
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = email
    message["Subject"] = subject
    message.attach(MIMEText(body,"plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(sender_email,password)
        server.sendmail(sender_email,email,message.as_string())
        server.quit()
    except Exception as e:
        print(e)

def register():
    full_name = input("Enter your full name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")

    if password != confirm_password:
        print("Passwords do not match")
        return register()

    if queries.get_user_by_email(email=email):
        print("Email already register")
        return register()
    
    if queries.add_user_query(params=(full_name,email,password,)):
        code = utils.get_verification_code(email=email)
        email_thread = threading.Thread(target=send_verfication_code,args=(email,code,))
        email_thread.start()
        queries.add_verification_code(email=email,code=code)
        return True
    
    return False


def activate_email():
    email = input("Enter your email: ")
    code = int(input("Enter your code: "))

    user_code = queries.get_user_code(email=email,code=code)
    if user_code:
        current_now = datetime.datetime.now()
        diff = current_now - user_code[-1]
        minute = diff.total_seconds() // 60
        if minute > 2:
            print("Your verification code expred")
            return False
        queries.update_user_status(email=email,status=1)
        print("Your email is verified,you can login now")
        return True
    else:
        print("Your code is not valid")
        return False



def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    user = queries.get_user_by_email(email=email)
    if user and user[3] == password:
        if user[-1] == 0:
            print("Please verify your email")
            return activate_email()
        else:
            queries.update_user_is_login(email=email,is_login=1)
            return True

    return False

        
