from lxml import html
import requests


page = requests.get('http://www.sobiki.de/5buchstaben.html')
code = html.fromstring(page.content)

print(page.status_code)
print(code)
print(page.text)

woerter = code.xpath('//td/text()')
print(woerter)

myList = [i.split('\t')[1] for i in woerter] 
print(myList)
