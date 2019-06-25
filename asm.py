# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
# html = urllib.request.urlopen(url, context=ctx).read()0
lst =list()
for count in range(0,7):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    tag = tags[17]
    email = tag.get('href', None)
    name = email.split('_')
    rname = name[2].split('.')
    rrname = rname[0]
    url = email
    lst.append(rrname)
print (lst)
