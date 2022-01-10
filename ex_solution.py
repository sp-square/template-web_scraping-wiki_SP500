import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

res = requests.get(url)
res_txt = res.text
soup = BeautifulSoup(res_txt, features='html.parser')

tbody = soup.find_all("tbody")
# print(tbody[0].contents[0])
# print(tbody[0].contents[2].contents[1].text)
# print(tbody[0].contents[4].contents[1].text)
# print(tbody[0].contents[6].contents[1].text)

tickers = []
for i in range(len(tbody[0].contents)):
    if i < 2 or i % 2 != 0:
        continue
    ticker = tbody[0].contents[i].contents[1].text
    tickers.append(ticker.strip('\n'))

print(len(tickers))
print(tickers)
