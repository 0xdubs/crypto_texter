# Automated Crypto-Currency Text Alerts with Python and Twilio
Send automated texts to yourself when crypto prices move above or below a percentage threshold. 

This code is based on my recent medium article, which can be found at https://daniel-warren.medium.com/automated-crypto-currency-text-alerts-with-python-and-twilio-4ddea257315f.

This is still a work in progress, so please let me know if you find any issues or if there are specific features you would like me to add.

## Notes
The `requirements.txt` file should list all Python libraries that your notebooks
depend on, and they will be installed using:

```
pip install -r requirements.txt
```

## Step 1 - Try running test_script_1.py
The `test_script_1_twilio.py` file should be the first file you attempt to run and it should verify whether you are able to send yourself texts via Twilio. Refer to the medium article to follow a more in depth discussion of this test file. To verify if it works, try:

```
python test_script_1_twilio.py
```


## Step 2 - Try running test_script_2.py
The `test_script_2_robinhood.py` file should be the second file you attempt to run and it should verify whether you are able to acces your own Robinhood account programmatically. Please refer to the medium article to follow a more in depth discussion of this test file. To verify if it works, try:

```
python test_script_2_robinhood.py
```



## Step 3 - Run full automation
If you have both of the test scripts above operational, all you should need to do now is run the following code:

```
python stonks_forever.py
```

And boom! $DOGE to the mooooooon! (This is not financial advice)
