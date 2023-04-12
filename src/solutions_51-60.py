import pandas as pd 
import numpy as np 
import sys

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def solution_51(args):
    from itertools import product

    primes = sieve_of_eratosthenes(1000000)
    prime_set = set(primes)
    logger.debug(" Found {} primes".format(len(primes)))
    
    for prime in primes:
        for mask in product('01', repeat=len(str(prime))):
            if mask.count('1') == 0:
                continue

            prime_family = []
            for digit in range(10):
                masked_number = apply_mask(prime, mask, digit)
                if len(str(masked_number)) == len(str(prime)) and masked_number in prime_set:
                    prime_family.append(masked_number)
            
            if len(prime_family) > 7:
                return min(prime_family)

    return 0

def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit + 1, i):
                sieve[j] = False

    return [i for i in range(limit + 1) if sieve[i]]

def apply_mask(number, mask, digit):
    return int(''.join([str(digit) if m == '1' else n for n, m in zip(str(number), mask)]))

def solution_52(args):
    n = 1
    while n < 7:
        start = 10 ** (n - 1)
        end = (10 ** n) // 6
        for number in range(start, end + 1):
            if test_multiple_same_digits(number, 2) and test_multiple_same_digits(number, 3) and test_multiple_same_digits(number, 4) and test_multiple_same_digits(number, 5) and test_multiple_same_digits(number, 6):
                return number
        n += 1
    return 0

def test_multiple_same_digits(number, n):
    original_digits = sorted(str(number))
    multiplied_digits = sorted(str(number * n))
    return original_digits == multiplied_digits

def solution_53(args):
    total_combinations = 0
    for n in range(23,101):
        for r in range(2,n//2+1):
            if (combinations(n,r) > 1000000):
                #print("n: {}, r: {}".format(n,r))
                total_combinations += n-2*r+1
                break # No need to check any more r values for this n
    return total_combinations

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def combinations(n, r):
    if r > n or r < 0 or n < 0:
        return 0
    r = min(r, n - r)  # Take advantage of symmetry: C(n, r) = C(n, n-r)
    numer = 1
    denom = 1
    for i in range(1, r + 1):
        numer *= n
        denom *= i
        n -= 1
    return numer // denom

def solution_54(args):
    # Process poker file input
    poker_file = open("data/p054_poker.txt", "r")

    # Loop through each line in the file
    player_1_wins = 0
    player_2_wins = 0
    i = 0
    for line in poker_file:
        logger.debug("Processing line: {}".format(line))
        # Split the line into two hands
        all_cards = line.split(" ")
        hand_1 = all_cards[0:5]
        hand_2 = all_cards[5:10]
        # Find the best hand for each player
        hand_1_rank, remaining_hand_1 = find_best_hand_rank(hand_1)
        hand_2_rank, remaining_hand_2 = find_best_hand_rank(hand_2)
        logger.debug("Player 1 hand rank: {}".format(hand_1_rank))
        logger.debug("Player 2 hand rank: {}".format(hand_2_rank))
        # Compare the hands
        if hand_1_rank > hand_2_rank:
            logger.debug("Player 1 wins")
            player_1_wins += 1
        elif hand_1_rank < hand_2_rank:
            logger.debug("Player 2 wins")
            player_2_wins += 1
        else:
            # If the hands are still the same rank, recursively compare the highest cards
            logger.debug("Hands are the same rank, comparing highest cards")
            while len(remaining_hand_1) > 0:
                hand_1_highest_card_score, remaining_hand_1 = find_highest_card(remaining_hand_1)
                hand_2_highest_card_score, remaining_hand_2 = find_highest_card(remaining_hand_2)
                logger.debug("Player 1 highest card: {}".format(hand_1_highest_card_score))
                logger.debug("Player 2 highest card: {}".format(hand_2_highest_card_score))
                if hand_1_highest_card_score > hand_2_highest_card_score:
                    player_1_wins += 1
                    logger.debug("Player 1 wins with highest card: {}".format(hand_1_highest_card_score))
                    break
                elif hand_1_highest_card_score < hand_2_highest_card_score:
                    player_2_wins += 1
                    logger.debug("Player 2 wins with highest card: {}".format(hand_2_highest_card_score))
                    break
                else:
                    # The highest cards are the same, so just go to next highest card
                    logger.debug("Highest cards are the same ({} and {}), comparing next highest cards".format(hand_1_highest_card_score, hand_2_highest_card_score))
                    continue
        logger.debug("")
        i += 1
        if i > 4:
            break
    return player_1_wins

def find_best_hand_rank(hand):
    # Find the best hand rank by checking each hand type in order
    remaining_hand = find_royal_flush(hand)
    if remaining_hand != None: return 10, remaining_hand
    remaining_hand = find_straight_flush(hand)
    if remaining_hand != None: return 9, remaining_hand
    remaining_hand = find_n_of_a_kind(hand, 4)
    if remaining_hand != None: return 8, remaining_hand
    remaining_hand = find_full_house(hand)
    if remaining_hand != None: return 7, remaining_hand
    remaining_hand = find_flush(hand)
    if remaining_hand != None: return 6, remaining_hand
    remaining_hand = find_straight(hand)
    if remaining_hand != None: return 5, remaining_hand
    remaining_hand = find_n_of_a_kind(hand, 3)
    if remaining_hand != None: return 4, remaining_hand
    remaining_hand = find_two_pair(hand)
    if remaining_hand != None: return 3, remaining_hand
    remaining_hand = find_n_of_a_kind(hand, 2)
    if remaining_hand != None: return 2, remaining_hand
    return 1, hand

def find_royal_flush(hand):
    # Find the royal flush
    # Check for a straight flush
    remaining_hand = find_straight_flush(hand)
    if remaining_hand != None:
        # Check that the highest card is an ace
        if remaining_hand[0][0] == "A":
            return remaining_hand
    return None

def find_straight_flush(hand):
    # Find the straight flush
    # Check for a straight
    remaining_hand = find_straight(hand)
    if remaining_hand != None:
        # Check for a flush
        remaining_hand = find_flush(remaining_hand)
        if remaining_hand != None:
            return remaining_hand
    return None

def find_full_house(hand):
    # Find the full house
    # Check for three of a kind
    remaining_hand = find_n_of_a_kind(hand, 3)
    if remaining_hand != None:
        # Check for a pair
        remaining_hand = find_n_of_a_kind(remaining_hand, 2)
        if remaining_hand != None:
            return remaining_hand
    return None

def find_flush(hand):
    # Find the flush
    # Check if all suits are the same
    if hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]:
        return hand
    return None

def find_straight(hand):
    # Find the straight
    # Create a dictionary to map card values to integers
    card_value_dict = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
    # Sort the hand by value (lowest to highest)
    sorted_hand = sorted(hand, key=lambda card: card_value_dict.get(card[0]))
    # Check if the cards are consecutive
    if card_value_dict.get(sorted_hand[0][0]) + 1 == card_value_dict.get(sorted_hand[1][0]) and \
            card_value_dict.get(sorted_hand[1][0]) + 1 == card_value_dict.get(sorted_hand[2][0]) and \
            card_value_dict.get(sorted_hand[2][0]) + 1 == card_value_dict.get(sorted_hand[3][0]) and \
            card_value_dict.get(sorted_hand[3][0]) + 1 == card_value_dict.get(sorted_hand[4][0]):
        return sorted_hand
    # Also check if A is last card, then test if others are 2,3,4,5
    if sorted_hand[4][0] == "A":
        if card_value_dict.get(sorted_hand[0][0]) == 2 and \
                card_value_dict.get(sorted_hand[1][0]) == 3 and \
                card_value_dict.get(sorted_hand[2][0]) == 4 and \
                card_value_dict.get(sorted_hand[3][0]) == 5:
            return sorted_hand
    return None

def find_two_pair(hand):
    # Find the two pair
    # Check for a pair
    remaining_hand = find_n_of_a_kind(hand, 2)
    if remaining_hand != None:
        # Check for another pair
        remaining_hand = find_n_of_a_kind(remaining_hand, 2)
        if remaining_hand != None:
            return remaining_hand
    return None

def find_n_of_a_kind(hand, n):
    # Find the n of a kind
    # Create a dictionary to map card values to integers
    card_value_dict = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
    # Sort the hand by value (lowest to highest)
    sorted_hand = sorted(hand, key=lambda card: card_value_dict.get(card[0]))
    # Check if there are n cards of the same value for each value of n
    if len(sorted_hand) == 5:
        if n == 4:
            if sorted_hand[0][0] == sorted_hand[3][0]:
                return [x for x in sorted_hand if x[0] != sorted_hand[0][0]]
            elif sorted_hand[1][0] == sorted_hand[4][0]:
                return [x for x in sorted_hand if x[0] != sorted_hand[1][0]]
        elif n == 3:
            if sorted_hand[0][0] == sorted_hand[2][0]:
                return [x for x in sorted_hand if x[0] != sorted_hand[0][0]]
            elif sorted_hand[1][0] == sorted_hand[3][0]:
                return [x for x in sorted_hand if x[0] != sorted_hand[1][0]]
            elif sorted_hand[2][0] == sorted_hand[4][0]:
                return [x for x in sorted_hand if x[0] != sorted_hand[2][0]]
        elif n == 2:
            if sorted_hand[0][0] == sorted_hand[1][0]:
                return [x for x in sorted_hand if x[0] != sorted_hand[0][0]]
            elif sorted_hand[1][0] == sorted_hand[2][0]:
                return [x for x in sorted_hand if x[0] != sorted_hand[1][0]]
            elif sorted_hand[2][0] == sorted_hand[3][0]:
                return [x for x in sorted_hand if x[0] != sorted_hand[2][0]]
            elif sorted_hand[3][0] == sorted_hand[4][0]:
                return [x for x in sorted_hand if x[0] != sorted_hand[3][0]]
    elif len(sorted_hand) == 3 or len(sorted_hand) == 2:
        if n == 2:
            if sorted_hand[0][0] == sorted_hand[1][0]:
                return [x for x in sorted_hand if x[0] != sorted_hand[0][0]]
            elif sorted_hand[1][0] == sorted_hand[2][0]:
                return [x for x in sorted_hand if x[0] != sorted_hand[1][0]]
    return None

def find_pair(hand):
    # Find the pair
    # Check for a pair
    remaining_hand = find_n_of_a_kind(hand, 2)
    if remaining_hand != None:
        return remaining_hand
    return None

def find_highest_card(hand):
    # Find the high card
    # Create a dictionary to map card values to integers
    card_value_dict = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
    # Sort the hand by value (lowest to highest)
    sorted_hand = sorted(hand, key=lambda card: card_value_dict.get(card[0]))
    return card_value_dict.get(sorted_hand[-1][0]), sorted_hand[:-1]


def solution_55(args):
    return args

def solution_56(args):
    return args

def solution_57(args):
    return args

def solution_58(args):
    return args

def solution_59(args):
    return args

def solution_60(args):
    return args

def main(argument_list):
    if len(argument_list) >= 2:
        solution_no = str(argument_list[1])
        args = argument_list[2:]
        solution_dict = {"51":solution_51,"52":solution_52,"53":solution_53,"54":solution_54,"55":solution_55,
                        "56":solution_56,"57":solution_57,"58":solution_58,"59":solution_59,"60":solution_60}
        answer = solution_picker(solution_dict.get(solution_no), args)
        logger.info(" Answer: {}".format(answer))
    else:
        logger.error(" ERROR: You must pass in a solution number")
        
def solution_picker(func,args):
    return func(args)

if __name__ == "__main__":
    main(list(sys.argv))
