# main script 2 - Stonks_forever.py

from subprocess import Popen
import sys
import time
import os, fnmatch

listOfFiles = os.listdir('.')
pattern = "*.py"

list_of_files = []

# for loop below gathers all python files in current directory
for entry in listOfFiles:
   if fnmatch.fnmatch(entry, pattern):
      list_of_files.append(entry)
      
filename = list_of_files[1] # this filename needs to point to robin_crypto_info.py
while True:
   print("\nStarting " + filename)
   p = Popen("python " + filename, shell=True)
   p.wait()
