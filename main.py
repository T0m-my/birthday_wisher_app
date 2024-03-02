import pandas
import datetime as dt
import smtplib
import random

SMTP_SERVER = 'smtp.gmail.com'
PORT = 587
MY_EMAIL_ADDR = 'tommymumena@gmail.com'
MY_PASSWORD = ''
# RECEIVER_EMAIL_ADDR = 'thomas.mumena@yahoo.com'
EMAIL_SUBJECT = 'Happy Birthday!'
today_birthdays = []

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
# actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

date_today = dt.datetime.now()
# print(date_today.date())

birthday_data = pandas.read_csv('./birthdays.csv')
for _, row_data in birthday_data.iterrows():
    birthday = dt.datetime(year=row_data['year'], month=row_data['month'], day=row_data['day'])
    # print(birthday)
    if birthday.month == date_today.month and birthday.day == date_today.day:
        today_birthdays.append(row_data)


for person in today_birthdays:
    randomNum = random.choice(range(1, 4))
    with open(f'./letter_templates/letter_{randomNum}.txt') as letter_file:
        # letter_content = [content.strip() for content in letter_file.readlines()]
        letter_content = letter_file.read()
        new_letter_content = letter_content.replace('[NAME]', f'{person['name']}')
        # print(new_letter_content)
        # print(person['email'])

    with smtplib.SMTP(host=SMTP_SERVER, port=PORT) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL_ADDR, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL_ADDR,
            to_addrs=person['email'],
            msg=f'Subject:{EMAIL_SUBJECT}\n\n{new_letter_content}'.encode('utf-8')
        )
