from twilio.rest import Client

TWILIO_VIRTUAL_NUMBER = "+12166776679"
TWILIO_SID = "ACd7d2dd1e19507149dceadb4199e9266a"
TWILIO_AUTH_TOKEN = "13645aeed80ad5da7967b7ce97044679"
TWILIO_VERIFIED_NUMBER = "7018339408"


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)