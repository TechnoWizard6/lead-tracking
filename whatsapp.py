import os
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException


def send_whatsapp(message):

    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")

    from_number = os.getenv("TWILIO_WHATSAPP_FROM")
    to_number = os.getenv("ALERT_NUMBER")

    if not account_sid:
        print("TWILIO_ACCOUNT_SID not configured")
        return

    if not auth_token:
        print("TWILIO_AUTH_TOKEN not configured")
        return

    if not from_number:
        print("TWILIO_WHATSAPP_FROM not configured")
        return

    if not to_number:
        print("ALERT_NUMBER not configured")
        return

    try:

        client = Client(account_sid, auth_token)

        msg = client.messages.create(
            from_=from_number,
            to=to_number,
            body=message
        )

        print("WhatsApp Sent:", msg.sid)

    except TwilioRestException as e:

        print("Twilio Error")
        print(e)

    except Exception as e:

        print("Unexpected Error")
        print(e)
