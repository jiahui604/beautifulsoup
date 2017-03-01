import re
import urllib

from bs4 import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())
# Retrieve all of the anchor tags
tags = soup('span')
num = []
sum = 0
count = 0
for tag in tags:
    number = re.findall('[0-9]+', tag.text)
    for x in number:
        num.append(int(x))
        sum += int(x)
        count += 1
print(sum)

