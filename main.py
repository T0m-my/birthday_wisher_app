import pandas
import datetime as dt
import smtplib
import random

SMTP_SERVER = 'smtp.gmail.com'
PORT = 587
MY_EMAIL_ADDR = 'tommymumena@gmail.com'
MY_PASSWORD = ''
RECEIVER_EMAIL_ADDR = ''
EMAIL_SUBJECT = 'Happy Birthday!'

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
# actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
randomNum = random.choice(range(1, 4))
with open(f'./letter_templates/letter_{randomNum}.txt') as letter_file:
    # letter_content = [content.strip() for content in letter_file.readlines()]
    letter_content = letter_file.read()
    new_letter_content = letter_content.replace('[NAME]', 'Carolyn')

with smtplib.SMTP(host=SMTP_SERVER, port=PORT) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL_ADDR, password=MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL_ADDR,
        to_addrs=RECEIVER_EMAIL_ADDR,
        msg=f'Subject:{EMAIL_SUBJECT}\n\n{new_letter_content}'.encode('utf-8')
    )
