from Card import *

hits = 0
tries = 0

def draw(hole_cards, pre_drawn_cards, draws, target, used, drawn_cards, id):
	global hits, tries
	if draws == 0:
		tries+=1
		if(target(hole_cards, pre_drawn_cards, drawn_cards)):
			hits+=1
		return
	elif id==52:
		return
	else:
		draw(hole_cards, pre_drawn_cards, draws, target, used, drawn_cards, id + 1)
		if not used[id]:
			drawn_cards.append(id_to_card(id))
			draw(hole_cards, pre_drawn_cards, draws-1, target, used, drawn_cards, id + 1)
			drawn_cards.pop()


def calculate(hole_cards, pre_drawn_cards, draws, target):
	global hits, tries
	hits = 0
	tries = 0

	used = [False for id in range(52)]
	for card in hole_cards + pre_drawn_cards:
		used[card_to_id(card)]=True

	drawn_cards=[]
	draw(hole_cards, pre_drawn_cards, draws, target, used, drawn_cards, 0)

	return 100.0*hits/tries

#print("x Pair: " + str(calculate([Card(s) for s in ['H9', 'SJ']], [], 5, pair)))


#def apply(a,f):
	#return list(map(f, a))

#print(apply([5,6,7,8] ,lambda x : x + 8))

#print(trips([Card(s) for s in ['H9', 'SJ']], [], [Card(s) for s in ['S9', 'CJ', 'C9']]))