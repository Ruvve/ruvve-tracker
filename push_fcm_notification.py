import firebase_admin
from firebase_admin import messaging
from firebase_admin import credentials
import json

secrets = json.loads(open('./firebase-key.json').read())

API_KEY = secrets['API_KEY']
TOKEN = secrets['TOKEN']

cred = credentials.Certificate("./firebase-adminsdk.json")
firebase_admin.initialize_app(cred)

def send_message(title, body):
    title = title
    message = body
    ntf_data = {title: body}
    registration_token = TOKEN

    alert = messaging.ApsAlert(title = title, body = message)
    aps = messaging.Aps(alert = alert, sound = "default")
    payload = messaging.APNSPayload(aps)

    # message
    msg = messaging.Message(
        notification = messaging.Notification(
            title = title,
            body = message
        ),
        data = ntf_data,
        token = registration_token,
        # apns = messaging.APNSConfig(payload = payload)
    )

    # send
    response = messaging.send(msg)
    print('Successfully sent message:', response)

