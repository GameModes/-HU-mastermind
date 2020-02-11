import random
def codemaker():
    global code
    code = ""
    while len(code) != 4: #vullen tot het 4 nummers bevat
        randnumber = random.randint(1,6) #getal kiezen tussen 1-6
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
    possible = []
    for x in range(1111, 6666):
        possible.append(x)
    def eerstegok():
        gok = 1122
        print("Gok: " + str(gok))
        positie = str(input("Hoeveel getallen zitten goed? "))
        inwoord = str(input("Hoeveel getallen zitten in het woord?" ))
        if positie == "0": #goeie positie
            if inwoord == "0": #wanneer niet bevat
                for y in possible:
                    if 1 in y or 2 in y:
                        possible.remove(y)
            else: #wanneer wel bevat haal alle andere mogelijkheden eruit
                for y in possible:
                    if not 1 in y and not 2 in y:
                        possible.remove(y)
        elif positie == "1":
            if inwoord == "1":
                for y in possible:
                    if 11 in y or 22 in y:
                        possible.remove(y)
        elif positie == "2":
            for y in possible:
                if not str(11) in y and not str(22) in y:
                    possible.remove(y)
        else:
            print('test')
        print(possible)
    eerstegok()
# def tweedegok():

def wildegok():
    code = ""
    while len(code) != 4:  # vullen tot het 4 nummers bevat
        randnumber = random.randint(1, 6)  # getal kiezen tussen 1-6
        code += str(randnumber)
    print("Gok: " + str(code))
    positie = str(input("Hoeveel getallen zitten goed? "))
    inwoord = str(input("Hoeveel getallen zitten in het woord?"))


def vraagnaariedernummer():
    getalopslag = {1: "0", 2: "0", 3: "0", 4: "0"}
    for gok in range(1111, 6666, 1111):
        nummerbijblijven = 0
        print(gok)
        for x in str(gok):
            nummerbijblijven += 1
            nummer = input("Is " + x + " op de juiste plek?")
            if nummer == "nee" or nummer == "Nee":
                # nummer = input("Is " + x + "In het getal?")
                continue
            else:
                getalopslag[nummerbijblijven]= x
    print(getalopslag)




def begin():
    keuze = input("Wilt u gokken naar een code of feedback geven? ")
    if "gok" in keuze:
        codemaker()
        codechecker()
    elif "feed" in keuze or "geven" in keuze:
        wildegok()

begin()
