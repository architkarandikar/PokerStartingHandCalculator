from Card import *

def pair(hole_cards, pre_drawn_cards, drawn_cards):
	value_histogram=[0 for i in range(13)]
	for card in hole_cards + pre_drawn_cards + drawn_cards:
		value_histogram[value_to_id(card.value)] += 1
	for i in range(13):
		if value_histogram[i] >= 2:
			return True
	return False

def hole_pair(hole_cards, pre_drawn_cards, drawn_cards):
	for hole_card in hole_cards:
		for drawn_card in pre_drawn_cards + drawn_cards:
			if hole_card.value == drawn_card.value:
				return True
	return False

def two_pairs(hole_cards, pre_drawn_cards, drawn_cards):
	value_histogram=[0 for i in range(13)]
	for card in hole_cards + pre_drawn_cards + drawn_cards:
		value_histogram[value_to_id(card.value)] += 1
	two_plus = 0
	for i in range(13):
		if value_histogram[i] >= 2:
			two_plus+=1
	return two_plus >= 2

def two_hole_pairs(hole_cards, pre_drawn_cards, drawn_cards):
	drawn_value_histogram=[0 for i in range(13)]
	for drawn_card in pre_drawn_cards + drawn_cards:
		drawn_value_histogram[value_to_id(drawn_card.value)] += 1
	if len(set([hole_card.value for hole_card in hole_cards])) == 1:
		return False
	for hole_card in hole_cards:
		if drawn_value_histogram[value_to_id(hole_card.value)] < 1:
			return False
	return True

def three_of_a_kind(hole_cards, pre_drawn_cards, drawn_cards):
	value_histogram=[0 for i in range(13)]
	for card in hole_cards + pre_drawn_cards + drawn_cards:
		value_histogram[value_to_id(card.value)] += 1
	for i in range(13):
		if value_histogram[i] >= 3:
			return True
	return False

def trips(hole_cards, pre_drawn_cards, drawn_cards):
	drawn_value_histogram=[0 for i in range(13)]
	for drawn_card in pre_drawn_cards + drawn_cards:
		drawn_value_histogram[value_to_id(drawn_card.value)] += 1
	for hole_card in hole_cards:
		if drawn_value_histogram[value_to_id(hole_card.value)] >= 2:
			return True
	return False

def sett(hole_cards, pre_drawn_cards, drawn_cards):
	drawn_value_histogram=[0 for i in range(13)]
	for drawn_card in pre_drawn_cards + drawn_cards:
		drawn_value_histogram[value_to_id(drawn_card.value)] += 1
	hole_value_histogram=[0 for i in range(13)]
	for hole_card in hole_cards:
		hole_value_histogram[value_to_id(hole_card.value)] += 1
	for i in range(13):
		if hole_value_histogram[i] >= 2 and drawn_value_histogram[i] >= 1:
			return True
	return False

def is_straight(value_histogram):
	for i in [z for z in range(9)] + [12]:
		found = True
		for j in range(5):
			k = i+j
			if k >= 13:
				k -= 13
			if value_histogram[k] == 0:
				found = False
				break
		if found:
			return True
	return False

def straight(hole_cards, pre_drawn_cards, drawn_cards):
	value_histogram=[0 for i in range(13)]
	for card in hole_cards + pre_drawn_cards + drawn_cards:
		value_histogram[value_to_id(card.value)] += 1
	return is_straight(value_histogram)

def flush(hole_cards, pre_drawn_cards, drawn_cards):
	suit_histogram=[0 for i in range(4)]
	for card in hole_cards + pre_drawn_cards + drawn_cards:
		suit_histogram[suit_to_id(card.suit)] += 1
	for i in range(4):
		if suit_histogram[i] >= 5:
			return True
	return False

def full_house(hole_cards, pre_drawn_cards, drawn_cards):
	value_histogram=[0 for i in range(13)]
	for card in hole_cards + pre_drawn_cards + drawn_cards:
		value_histogram[value_to_id(card.value)] += 1
	two_plus = 0
	three_plus = 0
	for i in range(13):
		if value_histogram[i] >= 2:
			two_plus+=1
		if value_histogram[i] >= 3:
			three_plus+=1
	return two_plus >= 2 and three_plus >= 1

def four_of_a_kind(hole_cards, pre_drawn_cards, drawn_cards):
	value_histogram=[0 for i in range(13)]
	for card in hole_cards + pre_drawn_cards + drawn_cards:
		value_histogram[value_to_id(card.value)] += 1
	for i in range(13):
		if value_histogram[i] >= 4:
			return True
	return False

def flush_draw(hole_cards, pre_drawn_cards, drawn_cards):
	suit_histogram=[0 for i in range(4)]
	for card in hole_cards + pre_drawn_cards + drawn_cards:
		suit_histogram[suit_to_id(card.suit)] += 1
	for i in range(4):
		if suit_histogram[i] >= 4:
			return True
	return False

def gut_shot_straight_draw(hole_cards, pre_drawn_cards, drawn_cards):
	value_histogram=[0 for i in range(13)]
	for card in hole_cards + pre_drawn_cards + drawn_cards:
		value_histogram[value_to_id(card.value)] += 1
	for i in range(13):
		if value_histogram[i] == 0:
			value_histogram[i] = 1
			if is_straight(value_histogram):
				return True
			value_histogram[i] = 0
	return False

def open_ended_straight_draw(hole_cards, pre_drawn_cards, drawn_cards):
	value_histogram=[0 for i in range(13)]
	for card in hole_cards + pre_drawn_cards + drawn_cards:
		value_histogram[value_to_id(card.value)] += 1
	draws = 0
	for i in range(13):
		if value_histogram[i] == 0:
			value_histogram[i] = 1
			if is_straight(value_histogram):
				draws += 1
			value_histogram[i] = 0
	return draws >= 2