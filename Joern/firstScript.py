import random
#import antigravity 


skriptname = "Woerter Spiel"
Autor = "Jörn"
Version = "2.0"
Datum = "02.09.22"

header = f"{skriptname}, {Autor}, {Version}, {Datum}"
print(header)
  
# open file
with open("Woerter.txt", "r") as file:
    data = file.read()
    words = data.split()
      
    # Generating a random number for word position
    word_pos = random.randint(0, len(words)-1)
    #print("Position:", word_pos)
    print("Zufälliges Wort aus Datei:", words[word_pos])
wort = words[word_pos]
pruefen = False

richtig = 0
falsch = 0
anzahl = len(wort)
print("Das gesuchte wort hat", anzahl, "Buchstaben")
while richtig != anzahl:
    richtig = 0
    falsch = 0
    print("Bitte geben Sie Ihr Wort ein")
    eingabe = input("")
    if len(eingabe) != anzahl:
        print("Das sind keine ", anzahl, " Buchstaben, versuche es erneut")
    else:
        print(eingabe, "mit" , wort, "vergeleichen")
        for i in range(anzahl):
            if eingabe[i] == wort[i]:
                print(wort[i], "vergleich", eingabe[i])
                print("stimmt")
                richtig += 1
            else:
                print(wort[i], "vergleich", eingabe[i])
                print("stimmt nicht")
                falsch += 1
        print("Sie haben ", richtig , "Buchstaben richtig und ", falsch , "Buchstaben falsch \n")
        if richtig == anzahl:
            print("Glückwunsch alles richtig")
        else:
            print("---------------------------------------------------------------------------")
            print("versuchen Sie es nochmal")
            
    
    
            
