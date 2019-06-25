from urllib.request import urlopen
import urllib.request, urllib.parse, urllib.error
import json
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
n = 0
url = input('Enter - ')
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
info = json.loads(data)
#print('User count:', len(info))
#print(json.dumps(info, indent=4))
for stuff in info['comments']:
    #print (stuff['count'])
    n = n + int(stuff['count'])
print (n)
