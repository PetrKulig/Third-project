Third-project
----------------------

Třetí projekt - Engeto Akademie

Popis projektu:
-----------------

Projekt slouží k extrahování výsledků voleb v roce 2017

 Instalace  knihoven
 --------------------

 Knihovny, které jsou použity v kódu jsou uloženy v souboru requirements.txt

 Instalaci doporučuji spustit následovně:

 pip3 instal -r  requirements.txt

 Spouštění souboru
 ------------------

 Pro  spouštění souboru použijte povinné argumenty

 python volebni_vysledky.py "odkaz_na_územní_celek" "jméno_výstupního_souboru.csv"

poté se vám stáhne csv soubor s výsledky voleb

Ukázka projektu
------------------

Výsledky hlasování pro okres Beroun

první argument: "https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ"
druhý argument: vysledky.csv

spouštění programu:
 python election_sraper.py "https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ" vysledky.csv

 Informace o konci stahování:
 ------------------------------

 Data byla zapsána do election_scraper.csv




