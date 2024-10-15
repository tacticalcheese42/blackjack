from deck_of_cards import deck_of_cards
from time import sleep
from os import system

deck = deck_of_cards.DeckOfCards()
numDecks = int(input("How many decks do you want to use?\n>"))
for i in range(numDecks):
    deck.add_deck()
deck.shuffle_deck()
print("\nDeck shuffled\n")

'''
self.suit = suit_rank_tup[0]
self.rank = suit_rank_tup[1]
self.name = self._translate_card()
self.image_path = ""

spades, diamonds, clubs, hearts
'''
numPlayers = int(input("How many players?\n>"))
cardsInPlay = []


# adds total for hand
def total(list):
    total = 0
    for i in range(len(list)):
        if list[i] == 1:
            total += 11
        elif list[i] == 11:
            total += 10
        elif list[i] == 12:
            total += 10
        elif list[i] == 13:
            total += 10
        else:
            total += list[i]
    if total > 21 and 1 in list:
        total -= 10
    return total


def busted(total):
    if total > 21:
        print("You bust")
        return True
    return False


def initDeck(card1, card2, hands, playerNum):
    cardVal1 = card1.rank
    cardVal2 = card2.rank
    tempList = [[cardVal1, cardVal2], playerNum]
    hands.append(tempList)


# init cards in play
for i in range(numPlayers):
    card1 = deck.give_first_card()
    card2 = deck.give_first_card()
    initDeck(card1, card2, cardsInPlay, i)


def showTable(list):
    tempList = ""
    for i in range(len(list)):
        tempList += "["
        for j in range(len(list[i][0])):
            if j != 0:
                tempList += str(list[i][0][j])+", "
        tempList += "]"
    print("table:\n"+tempList)


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
# TODO put winner thingy here
