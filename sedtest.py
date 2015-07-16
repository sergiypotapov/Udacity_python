__author__ = 'spotapov'

from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACe64d5a45ac8ec6eb0352c5c15d436521"
auth_token = "4d4a4d1371022a845b7c39e16dd38d94"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Pur-pur-pur", to="+380633710303", from_="+12105852895", media_url="http://www.gettyimages.co.uk/gi-resources/images/Homepage/Category-Creative/UK/UK_Creative_462809583.jpg")
print(message.sid)