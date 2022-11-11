#!/usr/bin/env python3
"""Beispielskript mit Kopfzeilen gemäß Kodierrichtlinien
   Bezeichner und Kommentare gemäß Kodierrichtlinien
   Vorlesung Konzepte des skriptorientierten Programmierens
   FOM Stuttgart WS 2022/2023"""

lizenz = \
"Dieser Quellkode steht unter der GNU GENERAL PUBLIC LICENSE 3 oder neuer"
skriptName = "skriptMitKopf.py"
skriptVersion = "1"
skriptDatum = "2022-09-18"
autor = "Gerhard Fessler"
skriptId = \
f"{skriptName} {skriptVersion}, {skriptDatum}, Copyright (c) {autor}"
aufrufKurz = f"Aufruf:    {skriptName}"
copyright = """Dieser Skript ist freie Software, die Sie unter bestimmten
Bedingungen weitergeben dürfen. Diese stehen im Quellkode.
Für dieses Python-Skript besteht KEINERLEI GARANTIE, weder für MARKTREIFE 
noch für eine VERWENDBARKEIT FÜR EINEN BESTIMMTEN ZWECK."""

aufrufLang = \
f"""{skriptName} nervt den Aufrufer so lange damit, eine Geheimzahl einzugeben,
bis diese eingegeben wird.

Nach der Eingabe einer Zahl gibt {skriptName} entweder eine Erfolgsmeldung
oder einen Hinweise bezüglich der zu findenden Geheimzahl aus.

Beispielhafter Aufruf:   {skriptName}

Es gibt keine Optionen für den Aufruf""" # aufrufLang

def druckeSkriptId():
    print(skriptId)
    return None

def druckeAufrufKurz():
    druckeSkriptId()
    print()
    print(aufrufKurz)
    return None

def druckeAufrufLang():
    druckeSkriptId()
    print(copyright)
    print()
    print(aufrufLang)
    return None
###############################################################################

druckeSkriptId()
# druckeAufrufKurz()
# druckeAufrufLang()

# Anfängliche Variable
geheimeZahl = 4612
eingegebeneZahl = 0
zaehler = 0

print()

while eingegebeneZahl != geheimeZahl:
    eingegebeneZahl = int(input("Bitte geben Sie eine Zahl ein: "))
    if eingegebeneZahl < geheimeZahl:
        print("Zahl ist kleiner als die Geheimzahl")
    if eingegebeneZahl > geheimeZahl:
        print("Zahl ist größer als die Geheimzahl")
    zaehler = zaehler + 1
print()
print("Gratulation, Sie haben es geschafft!")
print("Zum Finden der Geheimzahl haben Sie", zaehler, "Versuche benötigt.")
