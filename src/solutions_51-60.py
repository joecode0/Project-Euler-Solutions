import pandas as pd 
import numpy as np 
import sys
import nltk
from nltk.corpus import words

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
        logger.debug("Processing line: {}".format(line.strip("\n")))
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
            # If the hands are the same rank, firstly compare what cards that gave them that rank
            logger.debug("Hands are the same rank, comparing what gave them that rank")
            hand_1_scoring_cards = [x for x in hand_1 if x not in remaining_hand_1]
            hand_2_scoring_cards = [x for x in hand_2 if x not in remaining_hand_2]

            if len(hand_1_scoring_cards) in [2, 3, 4]:
                logger.debug("Both hands have pairs, 3 of a kind or 4 of a kind")
                # If 2, both have pairs, if 3, both have 3 of a kind, if 4, both have 4 of a kind or two pairs
                # In all cases, simply the highest card in all the scoring cards will determine the winner
                hand_1_highest_card_score, _ = find_highest_card(hand_1_scoring_cards)
                hand_2_highest_card_score, _ = find_highest_card(hand_2_scoring_cards)
                logger.debug("Player 1 highest scoring card: {}".format(hand_1_highest_card_score))
                logger.debug("Player 2 highest scoring card: {}".format(hand_2_highest_card_score))
                if hand_1_highest_card_score > hand_2_highest_card_score:
                    player_1_wins += 1
                    logger.debug("Player 1 wins with highest scoring card: {}".format(hand_1_highest_card_score))
                    continue
                elif hand_1_highest_card_score < hand_2_highest_card_score:
                    player_2_wins += 1
                    logger.debug("Player 2 wins with highest scoring card: {}".format(hand_2_highest_card_score))
                    continue
                else:
                    # If the highest scoring cards are the same, then the hands are the same
                    logger.debug("Scoring hands are same, move to comparing other cards")
            elif len(hand_1_scoring_cards) == 5:
                logger.debug("Both hands have straight, flush, full house, straight flush or royal flush")
                # If 5, both either have royal flush, straight flush, full house, straight or flush
                # For royal flush, straight flush, straight and flush, the highest card in the hand will determine the winner
                # For full house, the highest card in the 3 of a kind will determine the winner
                    # If the highest card in the 3 of a kind is the same, the highest card in the pair will determine the winner
                    # So check the full house scenario first, then can collectively solve the rest in one go
                if hand_1_rank == 7:
                    logger.debug("Both hands have full house")
                    # Full house
                    hand_1_highest_card_score, _ = find_highest_card(hand_1_scoring_cards[0:3])
                    hand_2_highest_card_score, _ = find_highest_card(hand_2_scoring_cards[0:3])
                    logger.debug("Player 1 highest scoring card: {}".format(hand_1_highest_card_score))
                    logger.debug("Player 2 highest scoring card: {}".format(hand_2_highest_card_score))
                    if hand_1_highest_card_score > hand_2_highest_card_score:
                        player_1_wins += 1
                        logger.debug("Player 1 wins with highest scoring card: {}".format(hand_1_highest_card_score))
                        continue
                    elif hand_1_highest_card_score < hand_2_highest_card_score:
                        player_2_wins += 1
                        logger.debug("Player 2 wins with highest scoring card: {}".format(hand_2_highest_card_score))
                        continue
                    else:
                        # If same, then we need to compare the pairs
                        logger.debug("Highest scoring cards are the same, comparing pairs")
                        hand_1_highest_card_score, _ = find_highest_card(hand_1_scoring_cards[3:5])
                        hand_2_highest_card_score, _ = find_highest_card(hand_2_scoring_cards[3:5])
                        logger.debug("Player 1 highest scoring card: {}".format(hand_1_highest_card_score))
                        logger.debug("Player 2 highest scoring card: {}".format(hand_2_highest_card_score))
                        if hand_1_highest_card_score > hand_2_highest_card_score:
                            player_1_wins += 1
                            logger.debug("Player 1 wins with highest scoring card: {}".format(hand_1_highest_card_score))
                            continue
                        elif hand_1_highest_card_score < hand_2_highest_card_score:
                            player_2_wins += 1
                            logger.debug("Player 2 wins with highest scoring card: {}".format(hand_2_highest_card_score))
                            continue
                        else:
                            # If the highest scoring cards are the same, then the hands are the same
                            logger.debug("Scoring hands are same, move to comparing other cards")
                else:
                    logger.debug("Both hands have straight, flush, straight flush or royal flush")
                    # Straight, flush, straight flush or royal flush
                    hand_1_highest_card_score, _ = find_highest_card(hand_1_scoring_cards)
                    hand_2_highest_card_score, _ = find_highest_card(hand_2_scoring_cards)
                    logger.debug("Player 1 highest scoring card: {}".format(hand_1_highest_card_score))
                    logger.debug("Player 2 highest scoring card: {}".format(hand_2_highest_card_score))
                    if hand_1_highest_card_score > hand_2_highest_card_score:
                        player_1_wins += 1
                        logger.debug("Player 1 wins with highest scoring card: {}".format(hand_1_highest_card_score))
                        continue
                    elif hand_1_highest_card_score < hand_2_highest_card_score:
                        player_2_wins += 1
                        logger.debug("Player 2 wins with highest scoring card: {}".format(hand_2_highest_card_score))
                        continue
                    else:
                        # If the highest scoring cards are the same, then the hands are the same
                        logger.debug("Scoring hands are same, move to comparing other cards")

            # If the hands are still the same at this point, recursively compare the remaining highest cards
            logger.debug("Scoring hands are equal, comparing leftover highest cards")
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
        #logger.info(i)
        i += 1
        # if i > 10:
        #     break
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
    elif len(sorted_hand) == 3:
        if n == 2:
            if sorted_hand[0][0] == sorted_hand[1][0]:
                return [x for x in sorted_hand if x[0] != sorted_hand[0][0]]
            elif sorted_hand[1][0] == sorted_hand[2][0]:
                return [x for x in sorted_hand if x[0] != sorted_hand[1][0]]
    elif len(sorted_hand) == 2:
        if n == 2:
            if sorted_hand[0][0] == sorted_hand[1][0]:
                return [x for x in sorted_hand if x[0] != sorted_hand[0][0]]
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

def get_card_value(card):
    # Create a dictionary to map card values to integers
    card_value_dict = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
    return card_value_dict.get(card[0])

def solution_55(args):
    total_count = 0
    for i in range(1, 10000):
        count = 0
        num = i
        while count < 50:
            num = do_lychrel_step(num)
            if test_num_palindrome(num):
                break
            count += 1
        if count == 50:
            total_count += 1
    return total_count

def do_lychrel_step(num):
    # Do a Lychrel step
    num_str = str(num)
    num_str_reversed = num_str[::-1]
    num_str_reversed_int = int(num_str_reversed)
    return num + num_str_reversed_int

def test_num_palindrome(num):
    # Test if a number is a palindrome
    num_str = str(num)
    if num_str == num_str[::-1]:
        return True
    return False

def solution_56(args):
    max_sum = 0
    for a in range(1, 100):
        for b in range(1, 100):
            current_sum = digital_sum(a ** b)
            max_sum = max(max_sum, current_sum)
    return max_sum

def digital_sum(number):
    return sum(map(int, str(number)))

def solution_57(args):
    from fractions import Fraction
    # Create a list to hold the fractions
    fractions = []
    # Create the first fraction
    fractions.append(Fraction(1, 2))
    # Create the next 999 fractions
    for i in range(1000):
        # Create the next fraction
        fractions.append(Fraction(1, 2 + fractions[-1]))
    logger.debug([Fraction(1) + x for x in fractions[:5]])
    # Count the number of fractions with a longer numerator than denominator
    count = 0
    for fraction in fractions:
        fraction = Fraction(1) + fraction
        if len(str(fraction.numerator)) > len(str(fraction.denominator)):
            count += 1
    return count

def solution_58(args):
    # Spiral primes
    # The diagonals of the spiral follow a clear pattern, so we can just loop through and compute these
    current_val = 1
    num_prime = 0
    total_diags = 1
    n = 1
    for n in range(1,100000):
        jump = n*2
        for _ in range(4):
            current_val += jump
            if is_prime(current_val):
                num_prime += 1
        total_diags += 4
        percent_prime = num_prime / total_diags
        if n % 1000 == 0:
            logger.debug("n: {}, percent prime: {}".format(n, percent_prime))
        if percent_prime < 0.1:
            return 2*n + 1
    return 0

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

def solution_59(args):
    nltk.download('words')

    # XOR decryption
    # Read in the file
    with open("data/p059_cipher.txt") as f:
        cipher = [int(x) for x in f.read().split(",")]

    # Create a list of all possible keys
    key_list = []
    for a in range(97, 123):
        for b in range(97, 123):
            for c in range(97, 123):
                key_list.append([a, b, c])

    # Loop through all possible keys
    for key in key_list:
        #logger.debug("Trying key: {}".format(key))

        # Create a list to hold the decrypted message
        decrypted_message = []

        # Loop through the cipher
        for i in range(len(cipher)):
            # XOR the cipher with the key
            decrypted_message.append(cipher[i] ^ key[i % 3])

        # Check if the decrypted message is valid
        message = "".join([chr(x) for x in decrypted_message])

        # Tokenize the message into words
        words_in_message = message.split()
        if "the" in words_in_message:
            logger.debug("Found a valid message with key: {}".format(key))
            return sum(decrypted_message)

    return 0

def is_valid_message(words_in_message, min_word_length=3, threshold=0.5):
    # Get the set of common English words
    english_words = set(words.words())

    # Count the number of valid English words in the message
    valid_word_count = 0
    for word in words_in_message:
        if len(word) >= min_word_length and word in english_words:
            valid_word_count += 1

    # Calculate the ratio of valid English words to total words
    valid_word_ratio = valid_word_count / len(words_in_message)

    # Return True if the ratio is greater than or equal to the threshold
    return valid_word_ratio >= threshold
    
def solution_60(args):
    from itertools import combinations
    primes = sieve_of_eratosthenes(1000)
    primes = set(primes)
    pairs = set([(p1, p2) for p1, p2 in combinations(primes, 2) if concat_prime(p1, p2)])

    for candidate in combinations(primes, 5):
        if all((p1, p2) in pairs for p1, p2 in combinations(candidate, 2)):
            return sum(candidate)
                
    return 0

def concat_prime(p1, p2):
    return is_prime(int(str(p1) + str(p2))) and is_prime(int(str(p2) + str(p1)))

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
