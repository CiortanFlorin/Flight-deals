from twilio.rest import Client

account_sid = "YOUR TWILLIO SID"
auth_token =  "YOUR TWILLIO TOKEN"

class NotificationManager:
        def __init__(self):
            self.client = Client(account_sid, auth_token)

        def send_msg(self, msg):
            message = self.client.messages \
                .create(
                body= msg,
                from_='YOUR TWILLIO PHONE NUMBER',
                to='YOUR PHONE NUMBER'
            )
            print(message.status)