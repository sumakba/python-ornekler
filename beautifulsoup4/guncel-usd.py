import requests
from bs4 import BeautifulSoup

url="http://www.doviz.com"
response=requests.get(url)
alinan_html=response.content
soup=BeautifulSoup(alinan_html,"html.parser")

html_icerik=soup.find_all('span', attrs={'class': 'menu-row2'})
usd = html_icerik[1]
print(usd.text)