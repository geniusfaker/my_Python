import requests
from bs4 import BeautifulSoup
url='http://www.nytimes.com'
read= requests.get(url)
soup=BeautifulSoup(read.text, features="lxml")

list=[]
soup=BeautifulSoup(requests.get(url).text, features='lxml')
titles=soup.find_all('head', {'class': 'story-heading'})
for i in titles:
    list.append(i)
print(list)