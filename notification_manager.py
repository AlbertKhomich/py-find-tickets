from twilio.rest import Client
import smtplib
from email.mime.text import MIMEText


def make_msg(info):
    text = f"Low price alert! Only €{info[0]} to fly from {info[1]} to {info[2]}, from {info[3]} to {info[4]}"
    if len(info) == 6:
        text += f'\nFlight has 1 stop over via {info[5]}'
    return text


class NotificationManager:

    def __init__(self):
        self.sender = 'khomich1022@gmail.com'
        self.account_sid = "AC5a240904d518095dea998954e9a58490"
        self.auth_token = "dcb4819873eebdc67cd9c8134c4e01f2"
        self.app_key_gmail = "uaqosktqimxapadh"

    def send(self, info):

        text = make_msg(info)

        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            body=text,
            from_="+15673648174",
            to="+4915110050210"
        )
        print(message.sid)

    def send_emails(self, info: list, receivers: list):

        text = make_msg(info)

        msg = MIMEText(text)

        for rec in receivers:
            msg['Subject'] = f'Only €{info[0]} to fly to {info[2]}'
            msg['From'] = self.sender
            msg['To'] = rec

            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(self.sender, self.app_key_gmail)
                server.sendmail(self.sender, rec, msg.as_string())
