import requests
respone = requests.get("http://radostudio.com/")
htmlTXT = respone.text

from bs4 import BeautifulSoup
soup = BeautifulSoup(htmlTXT,"html.parser")
persons = soup.find_all('h2', attrs = {'class' : 'elementor-heading-title elementor-size-default'})
for name in persons:
    print(name.text)


#divs = soup.find_all("div")
#for div in divs:
#    print(div)