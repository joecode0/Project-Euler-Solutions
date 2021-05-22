import pandas as pd 
import numpy as np 
import sys

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def solution_21(args):
    amicable_set = set([])
    for i in range(10000):
        result, sum_ = test_if_amicable_sum(i)
        if result and sum_ != i:
            logger.info("{} and {} are an amicable pair".format(i,sum_))
            amicable_set.add(i)
            amicable_set.add(sum_)

    output_sum = 0
    for item in amicable_set:
        output_sum += item
    logger.info(amicable_set)
    return output_sum

def get_factors_sum(number):
    factors_sum = 0
    i = 1
    j = number
    while i < j:
        j = int(number/i)
        if number%i == 0:
            factors_sum += i
            factors_sum += j
        i += 1
    if i==j:
        if i*j == number:
            factors_sum += i
    factors_sum -= number
    return factors_sum

def test_if_amicable_sum(number):
    sum_a = get_factors_sum(number)
    sum_b = get_factors_sum(sum_a)
    if number == sum_b:
        return True,sum_a
    else:
        return False,sum_a

def solution_22(args):
    df = pd.read_csv('C:/Users/joeco/Python/Project-Euler-Solutions/data/p022_names.csv')
    names = list(df.columns.values)
    names = sorted(names)
    logger.debug(names[0:5])

    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letter_scores = {}
    for i in range(len(alphabet)):
        letter_scores[alphabet[i]] = (i+1)

    names_scores = {}
    for i in range(len(names)):
        name = names[i]
        names_scores[name] = get_name_score(name,letter_scores)

    names_keys = names_scores.keys()
    total_score = 0
    i = 1
    for name in names_keys:
        total_score += (i*names_scores.get(name))
        i += 1
    return total_score

def get_name_score(name,letter_scores):
    name_score = 0
    for letter in name:
        name_score += letter_scores.get(letter)
    return name_score

def solution_23(args):
    abundant_numbers = []
    for i in range(1,28124): #14063
        factors_sum = get_factors_sum(i)
        if factors_sum > i:
            abundant_numbers.append(i)

    all_possible_numbers = set([])
    for i in range(len(abundant_numbers)):
        a = abundant_numbers[i]
        for j in range(i,len(abundant_numbers)):
            b = abundant_numbers[j]
            all_possible_numbers.add(a+b)

    all_impossible_numbers = [x for x in range(28123) if not x in all_possible_numbers] #28123
    logger.debug("{} impossible numbers".format(len(all_impossible_numbers)))
    return sum(all_impossible_numbers)

def get_factors_sum(number):
    factors_sum = 0
    i = 2
    j = int(number/i)
    while i < j:
        if number%i == 0:
            factors_sum += i
            factors_sum += j
        i += 1
        j = int(number/i)
    if i==j:
        if i*j == number:
            factors_sum += i
    factors_sum += 1
    return factors_sum

def solution_24(args):
    # Problem 24: Lexicographic permutations
    from math import factorial
    x = 1000000
    total_first_layer = factorial(9) # 362880
    first_layer_nth_permutation = x%total_first_layer # 274240
    # Therefore 362880 permutations with 0 at beginning, 362880 permutations with 1 at beginning, etc
    # therefore first number is 2, and millions permutation is 274240th permutation of 0,1,3,4,5,6,7,8,9 after a 2
    total_second_layer = factorial(8) # 40320
    second_layer_nth_permutation = first_layer_nth_permutation%total_second_layer # 32320
    # Therefore 40320 permutations with 2,0 at beginning, then 40320 permutations with 2,1, at beginning etc
    # therefore 2nd number is 7, and millionth permutation is 32320th permutation of 0,1,3,4,5,6,8,9 after 2,7
    total_third_layer = factorial(7) # 5040
    third_layer_nth_permutation = second_layer_nth_permutation%total_third_layer # 2080
    # therefore 5040 permutations with 2,7,0 at beginning, then 5040 permutations with 2,7,1, at beginning etc
    # therefore 3rd number is 8, and millionth permutation is 2080th permutation of 0,1,3,4,5,6,9 after 2,7,8
    total_fourth_layer = factorial(6) # 720
    fourth_layer_nth_permutation= third_layer_nth_permutation%total_fourth_layer # 640
    # therefore 720 permutations with 2,7,8,0 at beginning, then 720 with 2,7,8,1 at beginning, etc
    # therefore 4th number is 3, and millionth permutation is 640th permutation of 0,1,4,5,6,9 after 2,7,8,3
    total_fifth_layer = factorial(5) #120
    fifth_layer_nth_permutation = fourth_layer_nth_permutation%total_fifth_layer # 40
    # therefore 120 permutations with 2,7,8,3,0 at beginning, then 120 with 2,7,8,3,1 at beginning etc
    # therefore 5th number is 9, and millionth permutation is 40th permutation of 0,1,4,5,6 after 2,7,8,3,9
    total_sixth_layer = factorial(4) # 24
    sixth_layer_nth_permutation = fifth_layer_nth_permutation%total_sixth_layer #16
    # therefore 24 permutations with 2,7,8,3,9,0 at beginning, then 24 with 2,7,8,3,9,1 at beginning etc
    # therefore 6th number is 1, and millionth permutation is 16th permutation of 0,4,5,6 after 2,7,8,3,9,1
    total_seventh_layer = factorial(3) # 6
    seventh_layer_nth_permutation = sixth_layer_nth_permutation%total_seventh_layer #4
    # therefore 6 permutations with 2,7,8,3,9,1,0 at beginning, then 6 with 2,7,8,3,9,1,4 at beginning etc
    # therefore 7th number is 5, and millionth permutation is 4th permutation of 0,4,6 after 2,7,8,3,9,1,5

    #046
    #064
    #406
    #460
    #604
    #640

    # therefore result = 2,7,8,3,9,1,5,4,6,0
    return 2783915460

def solution_25(args):
    notFound = True
    cur_f = 0
    prev_f = 1
    two_prev_f = 1
    i = 3
    while notFound:
        cur_f = prev_f + two_prev_f
        num_digits = len(str(cur_f))
        #print("F_{} has {} digits".format(i,num_digits))
        if num_digits >= 1000:
            notFound = False
        i += 1
        two_prev_f = prev_f
        prev_f = cur_f
    #print("F_{} has over 1000 digits".format(i-1))
    return i-1

def solution_26(args):
    from decimal import *
    getcontext().prec = 10000
    test = str(str(1/7).split("0.")[1])

    best_so_far_length = 0
    d = 0
    for i in range(2,1000):
        digits_string = str(Decimal(1)/Decimal(i)).replace("0.","")
        repeat, recurring_str = find_repeat(digits_string)
        if repeat >= best_so_far_length:
            #print("New best: 1/{} has {} digits recurring".format(i,repeat))
            best_so_far_length = repeat
            d = i
    #print("Best: 1/{} has {} digits recurring".format(d,best_so_far_length))
    return d

def find_repeat(digits_string):
    original = digits_string
    for j in range(len(digits_string)):
        # Remove first entry and test, then repeat (first loop doesn't remove any entries)
        digits_string = original[j:]
        #print(digits_string)
        for i in range(int(len(digits_string)/2)):
            first_n_items = digits_string[:i]
            #print("First n items: {}".format(first_n_items))
            if first_n_items == digits_string[i:2*i] and i != 0:
                if 3*i < len(digits_string) and first_n_items == digits_string[2*i:3*i]:
                    return len(first_n_items), first_n_items
    return 0,""

def solution_27(args):
    # Problem 27: Quadratic Primes

    # Since formula must satisfy for n=0, b must be a prime
    # Therefore would be useful to produce all primes b <= 1000
    from math import sqrt
    all_values_of_b = get_all_primes(1000)
    # len(all_values_of_b) # 181 possible values for b

    # would now be worth selecting all (a,b) pairs that satisfy quadratic for n = 1 too
    known_primes = set(all_values_of_b)
    ab_pairs = []
    for i in range(-999,1000):
        a = i
        # formula for n = 1 is 1+a+b is prime
        for j in all_values_of_b:
            b = j
            potential_prime = 1+a+b
            result = test_prime(potential_prime,list(known_primes))
            if result:
                known_primes.add(potential_prime)
                ab_pairs.append((a,b))
                #print("New Valid Pair: {} and {}".format(a,b))
    len(ab_pairs) # 53517

    import time
    n = 2
    prev_ab_pairs = ab_pairs
    new_ab_pairs = set([])
    print("Getting all possible usable primes")
    known_primes = set(get_all_primes(100000))
    print("Done")
    while len(prev_ab_pairs) > 1:
        for pair in prev_ab_pairs:
            a = pair[0]
            b = pair[1]
            potential_prime = n**2 + a*n + b
            result = test_prime(potential_prime,list(known_primes))
            if result:
                known_primes.add(potential_prime)
                new_ab_pairs.add(pair)
        print("For n={}, there are {} valid ab pairs".format(n,len(new_ab_pairs)))
        n += 1
        if n == 500:
            print(new_ab_pairs)
        prev_ab_pairs = new_ab_pairs
        new_ab_pairs = set([])
    print(prev_ab_pairs)
    return (-61 * 971)

def test_prime(x, known_primes):
    if x < 2:
        return False
    max_val_to_check = int(sqrt(x))+1
    current_prime = known_primes[0]
    i = 0
    while current_prime < max_val_to_check:
        if x%current_prime == 0:
            return False
        i += 1
        current_prime = known_primes[i]
    return True

def get_all_primes(max_val):
    primes_list = [2,3,5,7,11,13,17]
    for i in range(18,max_val+1):
        result = test_prime(i, primes_list)
        if result:
            primes_list.append(i)
    return primes_list

def solution_28(args):
    return get_diag_sum(1001)

def get_diag_sum(board_size):
    a = 1
    b = 1
    c = 1
    d = 1
    a_to_add = 2
    b_to_add = 4
    c_to_add = 6
    d_to_add = 8
    diag_sum = 1
    virtual_board_size = 1
    while board_size > virtual_board_size:
        a += a_to_add
        b += b_to_add
        c += c_to_add
        d += d_to_add
        #print("{} {} {} {}".format(a,b,c,d))
        diag_sum += a
        diag_sum += b
        diag_sum += c
        diag_sum += d
        virtual_board_size += 2
        a_to_add += 8
        b_to_add += 8
        c_to_add += 8
        d_to_add += 8
    return diag_sum

def solution_29(args):
    final_a_to_b_set = set([])
    for i in range(2,101):
        for j in range(2,101):
            final_a_to_b_set.add(i**j)
    return len(final_a_to_b_set)

def solution_30(args):
    total_sum = 0
    for val in range(10,1000000):
        target = val
        digits = [int(x) for x in str(val)]
        inner_sum = 0
        for digit in digits:
            inner_sum += digit**5
        if inner_sum == target:
            total_sum += target
            #print(val)
    return total_sum

def main(argument_list):
    if len(argument_list) >= 2:
        solution_no = str(argument_list[1])
        args = argument_list[2:]
        solution_dict = {"21":solution_21,"22":solution_22,"23":solution_23,"24":solution_24,"25":solution_25,
                        "26":solution_26,"27":solution_27,"28":solution_28,"29":solution_29,"30":solution_30}
        answer = solution_picker(solution_dict.get(solution_no), args)
        logger.info(" Answer: {}".format(answer))
    else:
        logger.error(" ERROR: You must pass in a solution number")
        
def solution_picker(func,args):
    return func(args)

if __name__ == "__main__":
    main(list(sys.argv))
