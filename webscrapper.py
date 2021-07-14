import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.livescore.com/en/football/champions-league/")
#print(page.status_code)

soup = BeautifulSoup(page.content,'html.parser')
#print(soup.prettify)

#print(list(soup.children))
for i in soup.find_all(id = "content-center"):
    print(i.prettify())






file1 = open("debug.text","w")
file1.write(str(list(soup.children)))