# main script 1 - robin_crypto_info.py

import robin_stocks
from robin_stocks import *
import robin_stocks.robinhood as r
import time
import os
from twilio.rest import Client
from math import log10, flooR

account_sid = os.environ['account_sid']
auth_token = os.environ['auth_token']

client = Client(account_sid, auth_token)

login = r.login('USERNAME','PASSWORD')

# function below rounds a value to 2 sig figs
def round_sig(x, sig=2):
    return round(x, sig-int(floor(log10(abs(x))))-1)
 
symbol = 'DOGE' # input whatever crypto you want

n = 0
while n<100:   # in case I want to terminate loop
   n+=0        # current setup intentionally runs forever
   price_0 = float(robin_stocks.robinhood.crypto.get_crypto_quote(symbol, info=None)['mark_price'])
   time.sleep(15) # 15 second delay b/w gathering price values  
   price_f = float(robin_stocks.robinhood.crypto.get_crypto_quote(symbol, info=None)['mark_price'])
   percentage_change = (price_f-price_0)/price_0*100
   if percentage_change>0.5:
      client.api.account.messages.create(
      to='+17777777777'
      from='+18888888888'
      body='DOGE TO THE MOON! Up ' + str(round_sig(percentage_change)) + '%. Current price: $' + str(round_sig(price_f)))
   elif percentage_change<0.5:
      client.api.account.messages.create(
      to='+17777777777'
      from='+18888888888'
      body='DOGE AWAY FROM MOON! Down ' + str(round_sig(percentage_change)) + '%. Current price: $' + str(round_sig(price_f)))
   else:
      pass
