import re,urllib
import urllib.request
u = urllib.request.urlopen("https://timesofindia.indiatimes.com/")
text = u.read()
number = re.findall('[h][1-6]',str(text),re.IGNORECASE)
for n in number:
    print(n)
