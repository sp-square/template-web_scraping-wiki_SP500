import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

res = requests.get(url)
res_txt = res.text
soup = BeautifulSoup(res_txt, features='html.parser')
# print(soup.prettify())

# tables = soup.find_all('table')
# print(len(tables))

my_table = soup.find("table", {"id": "constituents"})
tr_tags = my_table.find_all("tr")
# print(tr_tags[1].contents)

tickers = []
for tr_tag in tr_tags[1:]:
    tickers.append(tr_tag.contents[1].text.split('\n')[0])

print(len(tickers))
print(tickers)
