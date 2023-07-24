import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv

url = "https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ"
href = "ps32?xjazyk=CZ&xkraj=2&xnumnuts=2102"

abs_url = urljoin(url, href)

response1 = requests.get(abs_url)
soup1 = BeautifulSoup(response1.content, "html.parser")

# Zpracování první tabulky
vysledky = []
html = []
tables = soup1.find_all('table', {"class": "table"})
for table in tables:
    rows = table.find_all("tr")
    for row in rows:
        cells = row.find_all("td")
        if len(cells) >= 2:
            vysledky.append([cells[0].text, cells[1].text])
        if len(cells) >= 1:
            link = cells[0].find("a")
            if link:
                href = link.get("href")
                if href:
                    abs_href = urljoin(abs_url, href)
                    html.append(abs_href)

data = []
for i in html:
    response = requests.get(i)
    soup = BeautifulSoup(response.content, "html.parser")
    # Získání první tabulky
    table = soup.find('table', {"class": "table"})
    if table:
        rows = table.find_all("tr")
        # Získání třetího řádku (index 2)
        if len(rows) >= 3:
            cells = rows[2].find_all("td")
            if len(cells) >= 8:
                data.append([cells[3].text, cells[4].text, cells[6].text, cells[7].text])

# Zpracování druhé tabulky a získání hlaviček sloupců
data2 = []
for i in html:
    response = requests.get(i)
    soup = BeautifulSoup(response.content, "html.parser")
    tables = soup.find_all('table', {"class": "table"})
    for table in tables:
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if len(cells) >= 3:
                header = cells[1].text
                value = cells[2].text
                data2.append([header, value])

# Uložení dat do souboru CSV
with open("vysledky.csv", mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    headers = ["Kod", "Obec", "Voliči v seznamu", "Platné hlasy", "Odevzdané obálky", "Vydané obálky"]
    writer.writerow(headers)

    for vysledek, radky in zip(vysledky, data):
        row_data = vysledek + radky
        writer.writerow(row_data)

    for row in data2:
        writer.writerow(["", row[0], "", "", "", ""] + [row[1]])

print("Data byla zapsána do vysledky.csv")
