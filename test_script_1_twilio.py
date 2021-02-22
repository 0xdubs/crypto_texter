# test script 1 - twilio

import os
from twilio.rest import Client

account_sid = os.environ['account_sid']
auth_token = os.environ['auth_token']

client = Client(account_sid, auth_token)

client.api.account.messages.create(
to="+17777777777", #input your personal phone number here
from_="+18888888888", #input your Twilio phone number here
body="Hello there!") #input the message you want to text here
