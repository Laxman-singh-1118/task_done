
from twilio.rest import Client

# Credentials
account_sid = input("put ur sid of twilio")
auth_token = input('pls put ur token')# KEEP THIS SAFE!

client = Client(account_sid, auth_token)

# Send SMS
message = client.messages.create(
    body="Hello from Python using Twilio!",
    from_=input("Your Twilio phone number")
    to=input('Destination phone number')
)

print("Message SID:", message.sid)
