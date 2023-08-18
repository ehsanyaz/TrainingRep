import requests
from bs4 import BeautifulSoup

respone = requests.get("http://radostudio.com/")
htmlTXT = respone.text

soup = BeautifulSoup(htmlTXT,"html.parser")
persons = soup.find_all('h2', attrs = {'class' : 'elementor-heading-title elementor-size-default'})
for name in persons:
    print(name.text)
