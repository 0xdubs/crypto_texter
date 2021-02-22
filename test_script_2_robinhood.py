# test script 2 - robinhood

import robin_stocks
from robin_stocks import *
import robin_stocks.robinhood as r
import time
import os

login = r.login('USERNAME','PASSCODE') #enter your username and passcode for your Robinhood account

symbol = 'DOGE' #enter the crypto symbol you're interested in
symbol_live_price = robin_stocks.robinhood.crypto.get_crypto_quote(symbol, info=None)['mark_price'] #anytime this .get_crypto_quote() function is run the live price of DOGE is returned

print("live symbol price: $",symbol_live_price)
