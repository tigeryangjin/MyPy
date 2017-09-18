from lxml.html import parse
from urllib.request import urlopen

request = urlopen('http://finance.yahoo.com/q/op?s=APPL+Options')
parsed = parse(request)
# parsed = parse(urlopen('http://finance.yahoo.com/q/op?s=APPL+Options'))
doc = parsed.getroot()
urls = [lnk.get('href') for lnk in doc.findall('.//a')]
print(urls)
request.close()
