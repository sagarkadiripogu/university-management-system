import smtplib
import random
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


OTP_EXPIRY_SECONDS = 300
MAX_ATTEMPTS = 3


def verify_student_email(email):

    otp = str(random.randint(1111, 9999))
    start_time = time.time()

    body = f"""<html>
                <h1 style="background-color:green;margin:20px;padding:20px;border:3px solid green">
                OTP for Verification - {otp}
                </h1>
            </html>"""

    msg = MIMEMultipart()
    msg["To"] = email
    msg["From"] = "sagarkadiripogu@gmail.com"
    msg["Subject"] = "OTP - Verification"
    msg.attach(MIMEText(body, "html"))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("sagarkadiripogu@gmail.com", "njzi ckgx jedf gwhq")
    server.send_message(msg)
    server.quit()

    print("Email Sent Successfully!")

    attempts = 0

    while attempts < MAX_ATTEMPTS:

        if time.time() - start_time > OTP_EXPIRY_SECONDS:
            print("OTP Expired! Please try again.")
            return False

        user_otp = input("Enter OTP: ")

        if user_otp == otp:
            print("Email Verified Successfully!")
            return True
        else:
            attempts += 1
            print(f"Wrong OTP! Attempts left: {MAX_ATTEMPTS - attempts}")

    print("Maximum attempts reached!")
    return False