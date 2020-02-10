import itertools
import copy

P = []  # Let P be the set that contains all possible combinations
S = []  # Let S be the set that contains all possible answers
prevGuesses = []
numPegs = 4
numColours = 6
firstGuess = [1, 1, 2, 2]
recentGuess = firstGuess
guessCount = 1  # Start at 1 since we have to make the initial guess


# Setup function to fill initial arrays
def setup():
    global P
    global S
    r = []

    for i in range(1, numColours + 1):
        r.append(i)

    comb = itertools.product(r, repeat=numPegs)

    # Fill P with all possible combinations
    for i in comb:
        P.append(list(i))

    S = copy.deepcopy(P)


# Helper function used by countPegs to count the number of black pegs
def countBlackPegs(code, guess):
    blackPegs = 0

    for i in range(len(guess)):
        if (guess[i] == code[i]):
            blackPegs += 1

    return blackPegs


# Helper function used by countPegs to count the number of white pegs
def countWhitePegs(code, guess):
    tempCode = code[:]  # Copy the list so we don't alter the original list
    whitePegs = 0

    for i in guess:
        if (i in tempCode):
            tempCode.remove(i)
            whitePegs += 1

    return whitePegs


# Function to count the number of black/white pegs for a given code and guess
def countPegs(code, guess):
    blackPegs = countBlackPegs(code, guess)
    whitePegs = countWhitePegs(code, guess)

    # Our counting function counts black pegs as duplicate whites, so we
    # have to remove those from the white peg count to be accurate
    whitePegs -= blackPegs

    return blackPegs, whitePegs


# Function to remove impossible codes from S based on new information
def removeImpossible(recentBlackPegs, recentWhitePegs):
    global S
    global recentGuess

    tempS = copy.deepcopy(S)

    # Iterate through S, remove codes that are not possible answers based on new information
    for code in tempS:
        blackCount, whiteCount = countPegs(code, recentGuess)

        if (blackCount != recentBlackPegs or whiteCount != recentWhitePegs):
            S.remove(code)


# Function to validate input from user as a number
def getInputNumber(inputMessage):
    while True:
        try:
            inputNumber = int(input(inputMessage))
            if (inputNumber < 0):
                raise ValueError
        except ValueError:
            print("Error: Please enter a number >= 0")
            continue
        else:
            return inputNumber


# Function to find and return the max hit count of all groups (to find highest min eliminated)
def findMaxHitCount(groups):
    grpHitCount = 0
    maxHitCount = 0

    for key, group in groups:
        grpHitCount = len(list(group))
        if (grpHitCount > maxHitCount):
            maxHitCount = grpHitCount

    return maxHitCount


# Function containing the main logic of the program
def main():
    global P
    global S
    global prevGuesses
    global firstGuess
    global recentGuess
    global guessCount

    print("")
    print("# of Possibilities: ", len(S))
    print("First Guess: ", firstGuess)

    recentBlackPegs = getInputNumber("Enter number of black pegs: ")
    recentWhitePegs = getInputNumber("Enter number of white pegs: ")

    removeImpossible(recentBlackPegs, recentWhitePegs)
    prevGuesses.append(firstGuess)

    # Loop until we guess the correct code
    while recentBlackPegs != 4:
        groups = []
        bestMinEliminated = []
        bestGuesses = []

        for guess in P:  # P contains all possible codes
            if (not guess in prevGuesses):  # For each unused code (slightly save computational time)
                # All guesses in S are sorted and grouped according to resulting peg counts
                # See step 6 of Knuth's five-guess algorithm to understand MinMax technique
                data = sorted(S, key=lambda x: (countPegs(guess, x)))  # Sort peg groups
                groups = itertools.groupby(data, lambda x: (countPegs(guess, x)))

                # Find which group will give us the max hit count
                # This is the group which will eliminate the most possibilities
                maxHitCount = findMaxHitCount(groups)
                minEliminated = len(S) - maxHitCount

                # Add guess + score (highest min eliminated) to lists for comparison later
                bestMinEliminated.append(minEliminated)
                bestGuesses.append(guess)

        # Find the max number of min guesses eliminated and all corresponding indices
        maxMinEliminated = max(bestMinEliminated)
        indices = [index for index, value in enumerate(bestMinEliminated) if value == maxMinEliminated]

        nextGuess = []
        flagFirstGuess = True

        # Iterate through indices, see if we can find one in S, otherwise use the first one
        # Reason: If we have multiple possible best guesses, we try to choose one from S (if it exists)
        # This gives us the possibility of guessing the code earlier
        for i in indices:
            if (bestGuesses[i] in S):
                nextGuess = bestGuesses[i]
                break
            elif (flagFirstGuess):
                nextGuess = bestGuesses[i]
                flagFirstGuess = False

        print("")
        print("# of Possibilities: ", len(S))

        if (len(S) < 1):  # This statement will only trigger if the human has given an incorrect response
            print("Error: No possible combination, based on given information")
            print("Please double check your responses for mistakes and try again")
            exit()

        print("Next Guess: ", nextGuess)

        guessCount += 1
        recentGuess = nextGuess
        recentBlackPegs = getInputNumber("Enter number of black pegs: ")
        recentWhitePegs = getInputNumber("Enter number of white pegs: ")

        # Remove all impossible codes from S, based on new peg information
        removeImpossible(recentBlackPegs, recentWhitePegs)
        prevGuesses.append(recentGuess)

    print("")
    print("Machines win again! :smugface:")  # Give sassy reply to aggravate human
    print("Number of guesses: ", guessCount)
