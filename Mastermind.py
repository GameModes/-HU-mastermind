import random
import collections

def codemaker():
    code = "" #lege code
    while len(code) != 4:  # vullen tot het 4 nummers bevat
        randnumber = random.randint(1, 6)  # getal kiezen tussen 1-6
        code += str(randnumber)
    print("Code is: " + code) #~verwijder~
    return code

def gokker():
    gok = " "
    gok = input("Voer in vier getallen 1-6: ")  #gok code invoering
    return gok

#Tot nu toe zijn twee waardes ontstaan: Code, willekeurig getal & de gok
def woordchecker (gok, code): #module collections heeft het maken van een lijst uit een string erg makkelijker gemaakt: https://stackabuse.com/introduction-to-pythons-collections-module/
    positiechecker = 0 #waarde zit perfect in code
    inwoordchecker = 0 #waarde zit in code
    tempcode = collections.Counter(code)#Een tijdelijke lijst maken van de code
    tempgok = collections.Counter(gok)#Een tijdelijke lijst maken van de gok
    # for number in range(4): #telt van 0 tot 3
    #     if gok[number] == tempcode[number]: #als de nummer met de gelijke index hetzelfde is
    #         positiechecker += 1 #waarde stijgt wanneer perfect erin zit
    #         tempcode = list(tempcode) #maakt lijst van string per letter
    #         tempcode[number] = "0" #maakt de gebruikte getal 0 om andere connecties te voorkomen
    #         "".join(tempcode)#maakt er weer een string van
    # for number in range(4):
    #     if gok[number] in str(tempcode) and not gok[number] == tempcode[number]: #voor getallen die alleen in het woord zitten
    #         inwoordchecker += 1
    #         tempcode = list(tempcode)
    #         tempcode[number] = "0"
    #         "".join(tempcode)
    inwoordchecker = sum(min(tempcode[number], tempgok[number]) for number in tempcode) #telt alle keren wanneer het in de code is
    positiechecker = sum(codenum == goknum for codenum, goknum in zip(tempcode, gok)) #telt alle keren wanneer het precies op de juiste plaats staat
    inwoordchecker -= positiechecker #En het precieschecker eraf trekken bij de inwoordchecker omdat als het goed staat ook in het woord is, wat niet mag.
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
            print("Beurten zijn op. Je hebt verloren. Het goeie antwoord was: " + code)
    else:
        print("Antwoord is goed! De code is inderdaad " + code)

def eerstegok():
    strategychoice = input("Welke strategy moet de computer gebruiken? Irving's? Knuth's? Neuwirth's? Willekeurig? ")
    if "Wille" in strategychoice or "wille" in strategychoice:
        strategychoice = str(random.randint(1, 3))  # getal kiezen tussen 1-6

    if "Irv" in strategychoice or "irv" in strategychoice or "1" in strategychoice: #gebruik van Irving's strategy
        gok = 1123
    elif "Neu" in strategychoice or "neu" in strategychoice or "2" in strategychoice: #gebruik van Neuwirth's strategy
        gok = 1234
    else:   #gebruik van Knuth's strategy
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
    print("alle mogelijkheden:" + str(possible)) #~verwijder~
    if len(possible) > 4:
        simplestrategy(possible[0], possible)
    else:
        print(possible[0] + "is het antwoord")


def begin():
    keuze = input("Wil u gokken of naar een code feedback geven? ")
    codemaker()  # maakt de code
    if "gok" in keuze:
        goktel = 0 #begint bij 0
        codechecker(gokker(), codemaker(), goktel)
    elif "feed" in keuze or "geven" in keuze:
        eerstegok()
    opnikeuze = input("Opnieuw? ")
    if 'ja' in opnikeuze or "Ja" in opnikeuze:
        begin()
    else:
        print("bedankt voor het spelen!")

begin()