import requests
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def sendmail(from_email, password, to_email, subject,  message):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, "plain"))
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.ehlo()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, str(msg))
        server.close()
        return True
    except Exception as e:
        print("Something went wrong" + str(e))

while True:
    time_1 = time.localtime()
    if time_1.tm_hour == 19 and time_1.tm_min == 17 and time_1.tm_sec == 0:
        api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
        city = "Prague"
        url = api_address + city
        json_data = requests.get(url).json()
        format_add = json_data["main"]

        temperature = json_data['main']['temp']
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']

        message = "Temperature: " + str(temperature) + " K\n Pressure: " + str(pressure) + " mbar\nHumidity: " + str(
            humidity) + "%"

        sendmail("example@exaple.com", "password", "matej.cervenka03@gmail.com", "Temperature morning report",
             message)









