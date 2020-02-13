import random
def codemaker():
    code = ""
    while len(code) != 4: #vullen tot het 4 nummers bevat
        randnumber = random.randint(1,6) #getal kiezen tussen 1-6
        code += str(randnumber)
    print("Code is: "+ code)
    return code
#correct
def gokker():
    gok = input("Voer in vier getallen 1-6: ")
    return gok

def codechecker (gok, code):
    goktel = 0
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
            gokker()
        else: #bij een goed antwoord
            print("Antwoord is goed! De code is inderdaad " + code)
            gevonden = True
    else: #na 10 beurten
        print("Beurten zijn op. Je hebt verloren. Het goeie antwoord was: " + code)
#niet correct, meerdere letters in 1 woord *regel 19-21)

def woordchecker(gok, code):
    positiechecker = 0
    inwoordchecker = 0
    tempcode = code
    for number in range(4):
        if gok[number] == tempcode[number]:
            positiechecker += 1
            tempcode = list(tempcode)  # zorgt ervoor dat meerdere 2's niet dezelfde nummer vergelijken
            tempcode[number] = "0"
            "".join(tempcode)
    for number in range(4):
        if gok[number] in str(tempcode) and not gok[number] == tempcode[number]:
            inwoordchecker += 1
            tempcode = list(tempcode)
            tempcode[number] = "0"
            "".join(tempcode)
    return [str(positiechecker), str(inwoordchecker)]

def codechecker2(gok, code, goktel):
    if goktel != 6:
        if code != gok:
            goktel += 1
            lst = woordchecker(gok, code)
            print("In " + str(gok) + " zitten er " + str(lst[0]) + " goed")
            print("In " + str(gok) + " zitten er " + str(lst[1]) + " in de code")
            gok = input("Voer in vier getallen 1-6: ")
            codechecker2(gok, code, goktel)
        else:  # bij een goed antwoord
            print("Antwoord is goed! De code is inderdaad " + code)
            gevonden = True
    else:  # na 10 beurten
        print("Beurten zijn op. Je hebt verloren. Het goeie antwoord was: " + code)
    # positiechecker = 0
    # inwoordchecker = 0
    # tempcode = code
    # if goktel != 6:
    #     if code != gok:
    #         goktel += 1
    #         for number in range(4):
    #             if gok[number] == tempcode[number]:
    #                 positiechecker += 1
    #                 tempcode = list(tempcode) #zorgt ervoor dat meerdere 2's niet dezelfde nummer vergelijken
    #                 tempcode[number] = "0"
    #                 "".join(tempcode)
    #             elif gok[number] in str(tempcode) :
    #                 inwoordchecker += 1
    #                 tempcode = list(tempcode)
    #                 tempcode[number] = "0"
    #                 "".join(tempcode)
    #         print("In " + str(gok) + " zitten er " + str(positiechecker) + " goed")
    #         print("In " + str(gok) + " zitten er " + str(inwoordchecker) + " in de code")
    #         codechecker2(gokker(), code, goktel)
    #     else:  # bij een goed antwoord
    #         print("Antwoord is goed! De code is inderdaad " + code)
    #         gevonden = True
    # else:  # na 10 beurten
    #     print("Beurten zijn op. Je hebt verloren. Het goeie antwoord was: " + code)
    # return [positiechecker, inwoordchecker]

def eerstegok():
    gok = 1122
    simplestrategy2(gok)

def simplestrategy2():
    gok = 1122
    possible = []
    for x in range(1111, 6666):
        possible.append(str(x))
        possible2 = []  # lijst na functie
        print("Gok: " + str(gok))
        positie = str(input("Hoeveel getallen zitten goed? "))
        inwoord = str(input("Hoeveel getallen zitten in het woord? "))
        lst2 = [positie, inwoord]
        for nummercheck in possible:
            lst = woordchecker(str(gok), nummercheck)
            print(lst)
            if lst2 == lst:
                possible2.append(str(nummercheck))
            possible = possible2
        print(possible2)



def simplestrategy(): #met dank aan: https://en.wikipedia.org/wiki/Mastermind_(board_game)
    possible = []
    for x in range(1111, 6666):
        possible.append(str(x))
    def eerstegok(possible):
        possiblerem = [] #lijst om mogelijkheden weg te halen
        possible2 = [] #lijst na functie
        gok = 1122
        print("Gok: " + str(gok))
        positie = str(input("Hoeveel getallen zitten goed? "))
        inwoord = str(input("Hoeveel getallen zitten in het woord? " ))
        if positie == "0": #goeie positie
            if inwoord == "0": #wanneer geen 1 of 2 bevat
                for x in range(3333, 6666): #maak nieuwe lijst van 3333 tot 6666
                    possible2.append(str(x))
                # geen1en2()
            elif inwoord == "4": #alle mogelijkheden zonder 1 of 2 eruit
                possiblerem += [x for x in possible if not "1" in x or not "2" in x]
                possible2 = [i for i in possible if i not in possiblerem]
            else: #wanneer wel bevat, haal alle andere mogelijkheden eruit
                possiblerem += [x for x in possible if not "1" in x or not "2" in x or x[0] == 1 or x[1] == 1 or x[2] == 2 or x[3] == 2]
                possible2 = [i for i in possible if i not in possiblerem]
        elif positie == "1":
            if inwoord == "1":
                for y in possible:
                    if str(11) in possible or str(22) in y: #remove 11xx, x11x, xx11, 22xx, x22x, xx22
                        possible.remove(y)
        elif positie == "2":
            for y in possible:
                if not str(11) in y and not str(22) in y:
                    possible.remove(y)
        else:
            print('test')
        print(possible2)
    eerstegok(possible)
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

# def mastermindstrategy():

def begin():
    keuze = input("Wilt u gokken naar een code of feedback geven? ")
    if "gok" in keuze:
        goktel = 0
        codemaker()
        codechecker2(gokker(), codemaker(), goktel)
    elif "feed" in keuze or "geven" in keuze:
        simplestrategy2()

begin()
