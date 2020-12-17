import requests
from bs4 import BeautifulSoup
import json
import unidecode

URL = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Romania#Cases'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
# afisez titlul paginii
hi = soup.select('title')
print(hi[0].getText())
tabel = soup.find('table', class_='wikitable sortable')
# print(tabel) tabelul exista
rows = tabel.find_all('tr')
# print(county_rows) am reusit sa extrag si liniile fiecarei coloane
counties = []
for i in range(1, len(rows) - 1):
    columns = rows[i].find_all('td')
    if len(columns) > 0:
        try:
            county_name = unidecode.unidecode(columns[0].find('a').text.strip())
            no_cases = columns[1].text.strip()
            no_recoveries = columns[2].text.strip()
            no_deaths = columns[3].text.strip()
            incidence = columns[4].text.strip()
            counties.append({"County": county_name,
                             "Cases": no_cases,
                             "Recoveries": no_recoveries,
                             "Deaths": no_deaths,
                             "Incidence": incidence})
        except AttributeError:
            pass

# for county in counties:
#     print(county)

with open('data.txt', 'w') as file:
    for county in counties:
        file.write(f'{json.dumps(county)}\n')
