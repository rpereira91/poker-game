import json
from random import randint

with open('deck.json') as json_file:  
    data = json.load(json_file)

table = []
hand = []
used_cards = []

def deal_card(place_delt):
    card_numer = get_card()
    place_delt.append(data[card_numer])
    used_cards.append(card_numer)

def get_card():
    card = randint(0,51)
    while (card in used_cards):
        card = randint(0,51)
    return card

def show_hand():
    for h in hand:
        print_card(h)

def show_table():
    for h in table:
        print_card(h)
def burn():
    used_cards.append(get_card())

def print_card(card):
    print("%s of %s" % (card['value'], card['suit']))

deal_card(hand)
deal_card(hand)
print("Hand")
show_hand()
deal_card(table)
deal_card(table)
deal_card(table)
burn()
deal_card(table)
burn()
deal_card(table)
print("Table")
show_table()