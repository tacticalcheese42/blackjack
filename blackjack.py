from deck_of_cards import deck_of_cards
from time import sleep
from os import system


# Variable Declaration
deck = 0
numPlayers = 0
cardsInPlay = []


# FUNCTIONS

# checks if the player has gone over 21
def busted(total):
    if total > 21:
        print("You bust")
        return True

    return False


# winner check stuff
def declareWinner(hands):
    totals = []
    highest = 0
    others = []
    string = "Player "
    for i in range(len(hands)):
        totals.append([i, total(hands[i][0])])

        if totals[i][1] > totals[highest][1] and totals[i][1] <= 21:
            highest = i
            others = []
        elif totals[i][1] == totals[highest][1] and i > 0:
            others.append(i)

    string += str(totals[highest][0]+1)+" won with "
    string += str(totals[highest][1])+" points."
    for i in range(len(others)):
        string += "\n"
        string += "Player "
        string += str(totals[others[i]][0]+1)+" also won with "
        string += str(totals[others[i]][1])+" points."

    return [string, totals, highest]


def initCards():
    global deck

    try:
        # adds a deck of cards (or decks) to be used for the game
        deck = deck_of_cards.DeckOfCards()
        numDecks = int(input("How many decks do you want to use?\n>"))
        # adds any additional decks
        for i in range(numDecks):
            deck.add_deck()
        # shuffles deck
        deck.shuffle_deck()
        print("\nDeck shuffled\n")
    except ValueError:
        print("Sorry, thats not a valid input. Please try again.")
        initCards()


# deals out cards for each player
def initDeck(card1, card2, hands, playerNum):
    # gives each player two cards
    cardVal1 = card1.rank
    cardVal2 = card2.rank
    # gives each player a set of cards and a player number
    tempList = [[cardVal1, cardVal2], playerNum]
    hands.append(tempList)


def initTable():
    global numPlayers, cardsInPlay

    try:
        # initializes main list for however many players there are
        numPlayers = int(input("How many players?\n>"))
        # [[cards for player1, player num-1],...]
        cardsInPlay = []

        # init cards in play
        for i in range(numPlayers):
            card1 = deck.give_first_card()
            card2 = deck.give_first_card()
            initDeck(card1, card2, cardsInPlay, i)
    except ValueError:
        print("Sorry, that's not a valid input. Please try again.")
        initTable()


# Creates string displaying all other players besides the winners score.
def otherPoints(list, winner):
    display = ""

    for i in range(len(list)):

        if winner != list[i][0]:
            display += "Player "
            display += str(list[i][0]+1)
            display += " scored "
            display += str(list[i][1])
            display += " points.\n"

    return display


# prints all of the cards that can be seen by player
def showTable(list):
    # makes a list of all the players cards that are face up
    tempList = ""

    # creates each players hand as a list to add to tempList
    for i in range(len(list)):
        tempList += "["
        # adds all of the cards except the first
        for j in range(len(list[i][0])):
            if j != 0:
                tempList += str(list[i][0][j])+", "
        tempList += "]"

    # prints final list to the user
    print("table:\n"+tempList)


# adds totals up for a hand
def total(list):
    total = 0
    # for each card it checks to decide how many points should be added
    for i in range(len(list)):
        # add 11 for an ace
        if list[i] == 1:
            total += 11
        # add 10 for all face cards
        elif list[i] == 11:
            total += 10
        elif list[i] == 12:
            total += 10
        elif list[i] == 13:
            total += 10
        # add face val for all other cards
        else:
            total += list[i]

    # checks to see if an ace needs to be one point instead of eleven
    if total > 21 and 1 in list:
        total -= 10

    return total


# INITIALIZATION

initCards()
initTable()


# MAIN LOOP
for i in range(numPlayers):
    showTable(cardsInPlay)
    hand = cardsInPlay[i][0]
    print("Player " + str(cardsInPlay[i][1]+1))
    print(hand)
    print("Your total is: " + str(total(hand)))
    while True:
        hos = input("hit or stay?\n>")
        if hos.lower().startswith('hit'):
            card = deck.give_first_card()
            hand.append(card.rank)
            print(hand)
            print("Your total is: " + str(total(hand)))
            if busted(total(hand)):
                sleep(1)
                break
            sleep(1)
        elif hos.lower().startswith('stay'):
            break
        else:
            print("Sorry, thats not a vaild input, please try again.")
            sleep(1)
    system("cls")
    if i < numPlayers - 1:
        print("Player " + str(i+1) + " done. Now player " + str(i+2))
        placeholder = input("Press [Enter] to continue.")
        system("cls")

winner = declareWinner(cardsInPlay)
print(winner[0])
print(otherPoints(winner[1], winner[2]))
