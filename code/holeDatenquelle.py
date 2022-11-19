#!/usr/bin/env python3
"""Skript für den Download und die Filterung des deutschsprachige Wörterbuch von
https://sourceforge.net/projects/germandict/"""

lizenz = \
"Dieser Quellkode steht unter der GNU GENERAL PUBLIC LICENSE 3 oder neuer"
skriptName = "holeDatenquelle.py"
skriptVersion = "1.2"
skriptDatum = "2022-11-19"
autor = "Lukas Lindner"
skriptId = \
f"{skriptName} {skriptVersion}, {skriptDatum}, Copyright (c) {autor}"
aufrufKurz = f"Aufruf:    {skriptName} [Optionen] [Wortlänge] [Einagbedateiname...] [Ausgabedateinamen]"
copyright = """Dieser Skript ist freie Software, die Sie unter bestimmten
Bedingungen weitergeben dürfen. Diese stehen im Quellkode.
Für dieses Python-Skript besteht KEINERLEI GARANTIE, weder für MARKTREIFE 
noch für eine VERWENDBARKEIT FÜR EINEN BESTIMMTEN ZWECK."""

aufrufLang = \
f"""{skriptName} lädt die Wortliste von
https://sourceforge.net/projects/germandict/ herunter und speichert eine auf
Anzahl der Zeichen gefilterte Liste in eine UTF-8 Datei. 

Nach der Eingabe der Anzahl Buchstaben als Filterkriterium gibt {skriptName}
entweder eine Erfolgsmeldung inkl. Anzahl der Wörter oder eine Fehlermeldung
aus.

Beispiele für den Aufruf
Interaktiver Aufruf:   {skriptName}
Durch den Aufruf des Skripts ohne Parameter wird eine Interaktion durch den
Benutzer erwartet.

Aufruf mit Übergabe:
{aufrufKurz}
Beispiel:              {skriptName} -v 6 eingabe1.txt eingabe2.txt ausgabe.txt
Durch die Übergabe einer Ganzzahl an das Skript wird die Ausgabe automatisch
auf Wörter mit der angeben Anzahl an Buchstaben gefiltert.

Es gibt folgende Optionen für den Aufruf:
-h | --help | -?        Hilfe anzeigen
-v                      Erweiterte Ausgabe
-d | --debug            Erweiterte Ausgabe zur Fehlersuche
""" # aufrufLang

def druckeSkriptId():
    print(skriptId)
    return None

def druckeAufrufKurz():
    druckeSkriptId()
    print()
    print(aufrufKurz)
    exit()

def druckeAufrufLang():
    druckeSkriptId()
    print(copyright)
    print()
    print(aufrufLang)
    exit()
    
def leseParameter():
    parameter = sys.argv.copy()
    del parameter[0]
    for param in parameter:
        for name in glob.glob(param):
         
    return parameter
###############################################################################

druckeSkriptId()

import sys
import os
import glob
import requests
import pyunpack
import csv
import shutil

test = leseParameter()
print(test)
exit()

# Prüfen ob die Wortlänge übergeben wurde
if len(sys.argv) == 2:
    wortLaenge = int(sys.argv[1])
elif len(sys.argv) > 2:
    print("Fehler: Skript mit mehr als einem Parameter aufgerufen")
    print("")
    print(aufrufLang)
else:
    # falls nicht wird sie zu 0 und der Benutzer wird nach Vorgabe gefragt
    wortLaenge = 0


#debug = False
debug = True

woerter = []

# Download  und Import des Wörterbuchs germandict von ourceforge.net
link = "https://sourceforge.net/projects/germandict/files/latest/download"
skriptPfad = os.path.dirname(__file__)
downloadPfad = os.path.join(skriptPfad, "german.7z")
zielpfadArchiv = os.path.join(skriptPfad, "german-dict")
woerterbuchPfad = os.path.join(zielpfadArchiv, "german.dic")
ausgabeDatei = os.path.join(skriptPfad, "words.txt")

istVorhanden = os.path.exists(downloadPfad)
if not istVorhanden:
    response = requests.get(link, stream=True)

    if response.status_code == 200:
        if debug:
            print("Herunterladen erfolgreich")
            print(f"HTTP Status Code: {response.status_code}")
        with open(downloadPfad, 'wb') as out:
            out.write(response.content)
    else:
        print("Herunterladen fehlgeschlagen")
        print(f"HTTP Status Code: {response.status_code}")

istVorhanden = os.path.exists(zielpfadArchiv)
if not istVorhanden:
  os.makedirs(zielpfadArchiv)
istVorhanden = os.path.exists(woerterbuchPfad)
if not istVorhanden:
    pyunpack.Archive(downloadPfad).extractall(zielpfadArchiv)

if wortLaenge == 0:
    print("Keine Wortlänge definiert, bitte die gewünschte Wortlänge angeben!")
    wortLaenge = int(input("Wortlänge als Ganzzahl: "))
    print(f"Es wurde Wörter mit {wortLaenge} Buchstaben gewählt")

zaehler = 0
with open(woerterbuchPfad, 'r') as fd:
    reader = csv.reader(fd)
    for row in reader:
        if len(str(row[0])) == wortLaenge:
            woerter.append(row[0])
            zaehler += 1
if debug:
    print(f"Wörterbuch: {woerterbuchPfad}")
    
datei = open(ausgabeDatei, 'w', encoding = 'utf-8')
for word in woerter:
    datei.write(f"{word}\n")
datei.close()

print(f"""{zaehler} Wörter mit {wortLaenge} Buchstaben aus dem Wörterbuch 
germandict in folgende Ausgabedatei geschrieben: 
{ausgabeDatei}""")

if debug:
    print(f"""Lösche temporäre Daten:
    {downloadPfad}
    {zielpfadArchiv}""")
os.remove(downloadPfad)
shutil.rmtree(zielpfadArchiv)