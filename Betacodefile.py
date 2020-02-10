import random
def codemaker():
    global code
    code = ""
    while len(code) != 4: #vullen tot het 4 nummers bevat
        randnumber = random.randint(1,6) #getal kiezen onder de 6 (1-6)
        code += str(randnumber)
    print("Code is: "+ code)
#correct

def codechecker ():
    goktel = 0
    gok = input("Voer in vier getallen 1-6: ") #eerste gok
    if goktel != 10:
        if code != gok:
            goktel += 1
            for number in gok:
                if number in code: #zit het getal in de code
                    if gok.index(number) == code.index(number): #zit het getal in de eerste nummer?
                        print(number + " zit goed en is goed")
                    elif gok.index(number) == code.index(number): #zit het getal in de tweede nummer?
                        print(number + " zit goed en is goed")
                    else:
                        print(number + " zit in het woord")
                else:
                    print(number + " zit niet in het woord")
            gok = input("Voer in vier getallen 1-6: ") #tweede - 10 gok
        else: #bij een goed antwoord
            print("Antwoord is goed! De code is inderdaad " + code)
    else: #na 10 beurten
        print("Beurten zijn op. Je hebt verloren. Het goeie antwoord was: " + code)
#niet correct, meerdere letters in 1 woord *regel 19-21)

def fiveguessalgoritm(): #met dank aan: https://en.wikipedia.org/wiki/Mastermind_(board_game)
    gok = 1111
    for x in str(gok):




def begin():
    keuze = input("Wilt u gokken naar een code of feedback geven? ")
    if "gok" in keuze:
        codemaker()
        codechecker()
    elif "feed" in keuze or "geven" in keuze:
        fiveguessalgoritm()

