class Card:
	def __init__(self, suit_value):
		self.suit = suit_value[0]
		self.value = suit_value[1]

	def print(self):
		return self.suit + self.value

def suit_to_id(suit):
	if suit == 'S':
		return 0
	elif suit == 'C':
		return 1
	elif suit == 'D':
		return 2
	else:
		return 3

def id_to_suit(id):
	if id == 0:
		return 'S'
	elif id == 1:
		return 'C'
	elif id == 2:
		return 'D'
	else:
		return 'H'

def value_to_id(value):
	if value == 'T':
		return 8
	elif value == 'J':
		return 9
	elif value == 'Q':
		return 10
	elif value == 'K':
		return 11
	elif value == 'A':
		return 12
	else:
		return int(value) - 2

def id_to_value(id):
	if id == 8:
		return 'T'
	elif id == 9:
		return 'J'
	elif id == 10:
		return 'Q'
	elif id == 11:
		return 'K'
	elif id == 12:
		return 'A'
	else:
		return str(id + 2)

def card_to_id(card):
	return 13*suit_to_id(card.suit) + value_to_id(card.value)

def id_to_card(id):
	return Card(id_to_suit(id//13) + id_to_value(id%13))