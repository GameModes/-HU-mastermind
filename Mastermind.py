import random
import collections

def codemaker():
    code = "" #lege code
    while len(code) != 4:  # vullen tot het 4 nummers bevat
        randnumber = random.randint(1, 6)  # getal kiezen tussen 1-6
        code += str(randnumber)
    # print("Code is: " + code) #~verwijder~
    return code

def gokker():
    gok = input("Voer in vier getallen 1-6: ")  #gok code invoering
    return gok

#Tot nu toe zijn twee waardes ontstaan: Code, willekeurig getal & de gok
def woordchecker (gok, code): #module collections heeft het maken van een lijst uit een string erg makkelijker gemaakt: https://stackabuse.com/introduction-to-pythons-collections-module/
    positiechecker = 0 #waarde zit perfect in code
    inwoordchecker = 0 #waarde zit in code
    tempcode = str(code)#Een tijdelijke string maken van de code
    tempgok = str(gok)#Een tijdelijke string maken van de gok
    for number in range(4):
        if tempcode[number] == tempgok[number]:
            positiechecker += 1
            if number == 0:
                tempcode = "9" + tempcode[1:]
            else:
                tempcode = tempcode[:number] + "9" + tempcode[number + 1:]

    for number in range(4):
        if tempgok[number] in tempcode:
            inwoordchecker += 1
            if tempcode.index(tempgok[number]) == 0:
                tempcode = "9" + tempcode[1:]
            else:
                tempcode = tempcode[:tempcode.index(tempgok[number])] + "9" + tempcode[tempcode.index(tempgok[number]) + 1:]

    return [str(positiechecker), str(inwoordchecker)]

def codechecker(gok, code, goktel):
    if gok != code: #wanneer de gok niet gelijk is aan de code
        if goktel != 6: #stopt bij aantal gokken 6
            goktel += 1 #+1 gok
            lst = woordchecker(gok, code) #roept functie woordchecker om lst te krijgen
            print("In " + str(gok) + " zitten er " + str(lst[0]) + " goed")
            print("In " + str(gok) + " zitten er " + str(lst[1]) + " in de code")
            codechecker(gokker(), code, goktel)
        else:
            print("Beurten zijn op. Je hebt verloren. Het goeie antwoord was: " + code)
    else:
        print("Antwoord is goed! In " + goktel + " beurten. De code is inderdaad " + code)

def eerstegok(goktel):
    strategychoice = input("Welke strategy moet de computer gebruiken? Irving's? Knuth's? Neuwirth's? Willekeurig? ")
    if "Wille" in strategychoice or "wille" in strategychoice:
        strategychoice = str(random.randint(1, 3))  # getal kiezen tussen 1-6
    if "Irv" in strategychoice or "irv" in strategychoice or strategychoice == "1": #gebruik van Irving's strategy
        gok = 1123
    elif "Neu" in strategychoice or "neu" in strategychoice or strategychoice == "2": #gebruik van Neuwirth's strategy
        gok = 1234
    else:   #gebruik van Knuth's strategy
        gok = 1122
    possible = []
    for x in range(1111, 6667):  # alle mogelijke oplossingen
        possible.append(str(x))
    simplestrategy(gok, possible, goktel)

def simplestrategy(gok, possible, goktel):
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
    print(str(goktel+1) + ". Alle mogelijkheden: " + str(possible)) #~verwijder~
    if len(possible) > 1:
        goktel += 1
        simplestrategy(possible[0], possible, goktel)
    elif goktel == 6:
        print("Te vaak geprobeerd")
    else:
        print(possible[0] + " is het antwoord in " + str(goktel+1) + " beurten")


def begin():
    keuze = input("Wil u gokken of naar een code feedback geven? ")
    codemaker()  # maakt de code
    if "gok" in keuze:
        goktel = 0 #begint bij 0
        codechecker(gokker(), codemaker(), goktel)
    elif "feed" in keuze or "geven" in keuze:
        goktel = 0
        eerstegok(goktel)
    else:
        print("Verkeerde invoer probeer opnieuw")
        begin()
    opnikeuze = input("Opnieuw? ")
    if 'ja' in opnikeuze or "Ja" in opnikeuze:
        begin()
    else:
        print("bedankt voor het spelen!")

begin()
