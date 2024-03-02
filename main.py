import pandas
import datetime as dt
import smtplib
import random

PORT = 587
SMTP_SERVER = 'smtp.gmail.com'
SENDER_EMAIL_ADDR = ''
SENDER_PASSWORD = ''
EMAIL_SUBJECT = 'Happy Birthday!'

# create tuple (current_day, current_day)
today_date = dt.datetime.now()
today_date_tuple = (today_date.day, today_date.month)

# create list of tuples with elements of ((day, month),row) from birthdays.csv
birthday_data = pandas.read_csv('./birthdays.csv')
birthdays = [((row_data['day'], row_data['month']), row_data) for (index, row_data) in birthday_data.iterrows()]

# filter out birthdays that match today
today_birthdays = [birthday[1] for birthday in birthdays if birthday[0] == today_date_tuple]

for birthday_person in today_birthdays:
    # pick random letter template and replace with actual name
    randomNum = random.randint(1, 3)
    with open(f'./letter_templates/letter_{randomNum}.txt') as letter_file:
        letter_content = letter_file.read()
        new_letter_content = letter_content.replace('[NAME]', f'{birthday_person['name']}')

    # send email
    with smtplib.SMTP(host=SMTP_SERVER, port=PORT) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL_ADDR, password=SENDER_PASSWORD)
        connection.sendmail(
            from_addr=SENDER_EMAIL_ADDR,
            to_addrs=birthday_person['email'],
            msg=f'Subject:{EMAIL_SUBJECT}\n\n{new_letter_content}'.encode('utf-8')
        )
