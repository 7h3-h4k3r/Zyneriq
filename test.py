from twilio.rest import Client

client = Client("your_sid", "your_token")
client.messages.create(
    body=f"Your verification code is: {otp}",
    from_="+919943268951", # Your Twilio number
    to="+919080443868"    # Recipient number
)
