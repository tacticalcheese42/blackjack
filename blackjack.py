from deck_of_cards import deck_of_cards
from time import sleep
from os import system


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


# checks if the player has gone over 21
def busted(total):
    if total > 21:
        print("You bust")
        return True
    return False


# deals out cards for each player
def initDeck(card1, card2, hands, playerNum):
    # gives each player two cards
    cardVal1 = card1.rank
    cardVal2 = card2.rank
    # gives each player a set of cards and a player number
    tempList = [[cardVal1, cardVal2], playerNum]
    hands.append(tempList)


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


# checks what the highest points are and displays to the users
def declareWinner(list):
    # sets a dummy winner, list of scores & players, and string to display
    winner = 0
    addWinners = []
    winnerC = 0
    scores = []
    string = ""
    # goes through each player and finds the total
    for i in range(len(list)):
        # current players total
        cplayer = total(list[i][0])
        # checks and sees if the score is higher than the current highest
        if cplayer > total(list[winner][0]):
            winner = i
            winnerC += 1
            scores.append([i+1, -1])
        elif cplayer == total(list[winner][0]):
            addWinners.append(i)
            winnerC += 1
            scores.append([i+1, -1])
        else:
            scores.append([i+1, cplayer])
    # sets up a string of all the other players scores to display
    for i in range(len(scores)):
        if scores[i][1] > -1:
            string += "Player "+str(scores[i][0])+" scored "+str(scores[i][1])+" points.\n"
    # displays winner and all scores
    wPlayerNum = str(cardsInPlay[winner][1]+1)
    if winnerC == 1:
        print("The winner is player " + wPlayerNum)
    else:
        stringW = ""
        for i in range(len(addWinners)):
            stringW += ", and " + str(addWinners[i])
        print("There was a tie. The winners are players " + wPlayerNum + stringW)
    print("They scored a total of " + str(total(list[winner][0])) + " points.")
    sleep(0.7)
    print(string)


# adds a deck of cards (or decks) to be used for the game
deck = deck_of_cards.DeckOfCards()
numDecks = int(input("How many decks do you want to use?\n>"))
# adds any additional decks
for i in range(numDecks):
    deck.add_deck()
# shuffles deck
deck.shuffle_deck()
print("\nDeck shuffled\n")

# initializes main list for however many players there are
numPlayers = int(input("How many players?\n>"))
cardsInPlay = []

# init cards in play
for i in range(numPlayers):
    card1 = deck.give_first_card()
    card2 = deck.give_first_card()
    initDeck(card1, card2, cardsInPlay, i)


# main loop
for i in range(numPlayers):
    showTable(cardsInPlay)
    hand = cardsInPlay[i][0]
    print("Player " + str(cardsInPlay[i][1]+1))
    print(hand)
    print("Your total is: " + str(total(hand)))
    while True:
        hos = input("hit or stay?\n>")
        if hos.lower().startswith('h'):
            card = deck.give_first_card()
            hand.append(card.rank)
            print(hand)
            print("Your total is: " + str(total(hand)))
            if busted(total(hand)):
                sleep(1)
                break
            sleep(1)
        else:
            break
    system("cls")
    if i < numPlayers - 1:
        print("Player " + str(i+1) + " done. Now player " + str(i+2))
        placeholder = input("Press [Enter] to continue.")
        system("cls")

declareWinner(cardsInPlay)
