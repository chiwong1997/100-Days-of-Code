# ---------- smtplib module ----------
# module for connecting to email servers and sending emails

# import smtplib

# GMAIL_SMTP = "smtp.gmail.com"
# PORT = 587

# my_email = "100daysofcodeproject@gmail.com"
# my_password = "flhitjcbrwhfybmx"


# with smtplib.SMTP(GMAIL_SMTP, port=PORT) as connection:

#     # make connection secure
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(from_addr=my_email, 
#                         to_addrs="chiyinwong97@gmail.com", 
#                         msg="Subject:This is a test email\n\nThis is the body of the email! hello mate"
#                         )
# connection.close() - don't need this unless not using "with" statement

# ---------- datetime module ----------
import datetime

now = datetime.datetime.now()
print(now)
# if we want the year, month, day etc, we can access the attributes of the datetime object
print(now.year)
print(now.minute)
print(now.weekday())  # Monday is 0 and Sunday is 6

date_of_birth = datetime.datetime(year=1997, month=8, day=25, hour=15, minute=30, second=29)
print(date_of_birth)

