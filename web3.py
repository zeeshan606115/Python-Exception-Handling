import re,urllib
import urllib.request
u = urllib.request.urlopen('https://timesofindia.indiatimes.com/')
text = u.read()
num  = re.findall('<h1>.*</h1>',str(text))
for n in num:
    print(n)
