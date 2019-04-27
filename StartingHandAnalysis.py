from Calculator import *
from Lambdas import *

hand = input('Starting Hand (format: CT HJ):: ')
print()
cards = [Card(id) for id in [hand[0:2], hand[3:5]]]

print("Flop:: Pair: " + str(calculate(cards, [], 3, pair)))
print("Flop:: Two Pairs: " + str(calculate(cards, [], 3, two_pairs)))
print("Flop:: Three of a Kind: " + str(calculate(cards, [], 3, three_of_a_kind)))
print("Flop:: Straight: " + str(calculate(cards, [], 3, straight)))
print("Flop:: Flush: " + str(calculate(cards, [], 3, flush)))
print("Flop:: Full House: " + str(calculate(cards, [], 3, full_house)))
print("Flop:: Four of a Kind: " + str(calculate(cards, [], 3, four_of_a_kind)))
print()

print("Flop:: Hole Pair: " + str(calculate(cards, [], 3, hole_pair)))
print("Flop:: Two Hole Pairs: " + str(calculate(cards, [], 3, two_hole_pairs)))
print("Flop:: Trips: " + str(calculate(cards, [], 3, trips)))
print("Flop:: Set: " + str(calculate(cards, [], 3, sett)))
print()

print("Flop:: Flush Draw: " + str(calculate(cards, [], 3, flush_draw)))
print("Flop:: Open Ended Straight Draw: " + str(calculate(cards, [], 3, open_ended_straight_draw)))
print("Flop:: Gut Shot Straight Draw: " + str(calculate(cards, [], 3, gut_shot_straight_draw)))
print()

print("Turn:: Pair: " + str(calculate(cards, [], 4, pair)))
print("Turn:: Two Pairs: " + str(calculate(cards, [], 4, two_pairs)))
print("Turn:: Three of a Kind: " + str(calculate(cards, [], 4, three_of_a_kind)))
print("Turn:: Straight: " + str(calculate(cards, [], 4, straight)))
print("Turn:: Flush: " + str(calculate(cards, [], 4, flush)))
print("Turn:: Full House: " + str(calculate(cards, [], 4, full_house)))
print("Turn:: Four of a Kind: " + str(calculate(cards, [], 4, four_of_a_kind)))
print()

print("Turn:: Hole Pair: " + str(calculate(cards, [], 4, hole_pair)))
print("Turn:: Two Hole Pairs: " + str(calculate(cards, [], 4, two_hole_pairs)))
print("Turn:: Trips: " + str(calculate(cards, [], 4, trips)))
print("Turn:: Set: " + str(calculate(cards, [], 4, sett)))
print()

print("Turn:: Flush Draw: " + str(calculate(cards, [], 4, flush_draw)))
print("Turn:: Open Ended Straight Draw: " + str(calculate(cards, [], 4, open_ended_straight_draw)))
print("Turn:: Gut Shot Straight Draw: " + str(calculate(cards, [], 4, gut_shot_straight_draw)))
print()