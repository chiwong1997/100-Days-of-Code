import smtplib

my_email = "100daysofcodeproject@gmail.com"
my_password = "flhitjcbrwhfybmx"


connection = smtplib.SMTP("smtp.gmail.com", port=587)

# make connection secure
connection.starttls()
connection.login(user=my_email, password=my_password)
connection.sendmail(from_addr=my_email, 
                    to_addrs="xx.com", 
                    msg="Subject:Hello\n\nThis is the body of the email! hello mate")
connection.close()

