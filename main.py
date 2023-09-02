import smtplib
import datetime as dt
import random
import pandas


my_gmail = "your email"
gmail_connection = "smtp.gmail.com"  # this is only for gmails...
app_password = "your app pass"
# gmail_port = 465


today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["name"], data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

for datas in birthday_dict:
    if datas[1:] == today_tuple:
        birthday_person = birthday_dict[datas]
        birthday_person_email = birthday_person["email"]
        letter_num = random.randint(1, 3)
        with open(f"letter_templates/letter_{letter_num}.txt") as letter_file:
            letter_template = letter_file.read()
            message_text = letter_template.replace("[NAME]", birthday_person["name"])
        subject = f"HAPPY BIRTHDAY {birthday_person['name'].capitalize()}!"
        msg = f"Subject:{subject}\n\n{message_text}"
        print(subject, message_text, sep="\n")

        try:
            with smtplib.SMTP(gmail_connection) as connection:
                connection.starttls()
                connection.login(user=my_gmail, password=app_password)
                connection.sendmail(from_addr=my_gmail, to_addrs=birthday_person_email, msg=msg)
            print("Ok. The email has been sent.")
        except:
            print("can't send the Email")
