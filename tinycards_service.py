from tinycards import Tinycards
from tinycards.model import Deck
import os

client  = Tinycards(os.environ['TC_LOGIN'], os.environ['TC_PASSWORD'])

def deck_has_duplicates(deck, front):
    cards = deck.cards

    if len(cards) != 0:
        for card in cards:
            if len(card.front.concepts) != 0:
                card_front = card.front.concepts[0].fact.text
                if card_front == front:
                    print('Card with this word on front already exists...')
                    return True

    return False

def add(pair):
    deck = client.find_deck_by_title(os.environ['TC_CURRENT_DECK'])
    if deck is None:
        deck = Deck(os.environ['TC_CURRENT_DECK'])
        deck = client.create_deck(deck)

    if not deck_has_duplicates(deck, pair[0]):
        deck.add_card(pair)
        client.update_deck(deck)