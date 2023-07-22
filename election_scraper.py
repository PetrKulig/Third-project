import requests
from bs4 import BeautifulSoup
import csv
import sys

if len(sys.argv) != 3:
    print('Chyba: Tento skript vyžaduje 2 argumenty: odkaz na územní celek a jméno výstupního souboru')
    sys.exit(1)

url = sys.argv[1]
output_file = sys.argv[2]

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find('table', {'id': 'ps311_t1'})
rows = table.find_all('tr')

header = ['Kód obce', 'Název obce', 'Voliči v seznamu', 'Vydáné obálky', 'Platné hlasy']
parties = []

for row in rows:
    cells = row.find_all('td')
    if len(cells) > 1:
        if not parties:
            party_cells = row.find_all('td', {'class': 'cislo'})
            for cell in party_cells:
                party_name = cell['headers'][0]
                parties.append(party_name)
                header.append(party_name)
        area_code = cells[0].text
        area_name = cells[1].text
        voters = cells[2].text
        envelopes = cells[3].text
        valid_votes = cells[4].text
        party_votes = [cell.text for cell in cells[5:]]
        row_data = [area_code, area_name, voters, envelopes, valid_votes] + party_votes

with open(output_file, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(row_data)

print(f'Výsledky hlasování byly uloženy do souboru {output_file}')
