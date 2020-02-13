import random

def codemaker():
    code = "" #lege code
    while len(code) != 4:  # vullen tot het 4 nummers bevat
        randnumber = random.randint(1, 6)  # getal kiezen tussen 1-6
        code += str(randnumber)
    print("Code is: " + code)
    return code

def gokker():
    gok = " "
    gok = input("Voer in vier getallen 1-6: ")  #gok code invoering
    return gok

#Tot nu toe zijn twee waardes ontstaan: Code, willekeurig getal & de gok
def woordchecker (gok, code):
    positiechecker = 0 #waarde zit perfect in code
    inwoordchecker = 0 #waarde zit in code
    tempcode = code #tijdelijke bewerkbare copy van de code
    for number in range(4): #telt van 0 tot 3
        if gok[number] == tempcode[number]: #als de nummer met de gelijke index hetzelfde is
            positiechecker += 1 #waarde stijgt wanneer perfect erin zit
            tempcode = list(tempcode) #maakt lijst van string per letter
            tempcode[number] = "0" #maakt de gebruikte getal 0 om andere connecties te voorkomen
            "".join(tempcode)#maakt er weer een string van
    for number in range(4):
        if gok[number] in str(tempcode) and not gok[number] == tempcode[number]: #voor getallen die alleen in het woord zitten
            inwoordchecker += 1
            tempcode = list(tempcode)
            tempcode[number] = "0"
            "".join(tempcode)
    return [str(positiechecker), str(inwoordchecker)]

def codechecker(gok, code, goktel):
    if gok != code: #stopt bij aantal gokken 6
        if goktel != 6: #wanneer de gok niet gelijk is aan de code
            goktel += 1 #+1 gok
            lst = woordchecker(gok, code) #roept functie woordchecker om lst te krijgen
            print("In " + str(gok) + " zitten er " + str(lst[0]) + " goed")
            print("In " + str(gok) + " zitten er " + str(lst[1]) + " in de code")
            codechecker(gokker(), code, goktel)
        else:
            print(print("Beurten zijn op. Je hebt verloren. Het goeie antwoord was: " + code))
    else:
        print("Antwoord is goed! De code is inderdaad " + code)

def eerstegok():
    gok = 1122
    possible = []
    for x in range(1111, 6666):  # alle mogelijke oplossingen
        possible.append(str(x))
    simplestrategy(gok, possible)


def simplestrategy(gok, possible):
    possible2 = [] #lijst na functie
    print("Gok: " + str(gok))
    positie = str(input("Hoeveel getallen zitten goed? "))
    inwoord = str(input("Hoeveel getallen zitten in het woord? "))
    lst2 = [positie, inwoord] #maak lijst van de posite en inwoord
    for nummercheck in possible:
        lst = woordchecker(str(gok), nummercheck) #roept woordchecker op om met de jouw gok waarde alle antwoorden bekijken van de lijst
        if lst2 == lst:
            possible2.append(str(nummercheck))
        possible = possible2
    simplestrategy(possible[0], possible)

def begin():
    keuze = input("Wil u gokken of naar een code feedback geven? ")
    codemaker()  # maakt de code
    if "gok" in keuze:
        goktel = 0 #begint bij 0
        codechecker(gokker(), codemaker(), goktel)
    elif "feed" in keuze or "geven" in keuze:
        eerstegok()

begin()