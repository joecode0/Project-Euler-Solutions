import pandas as pd 
import numpy as np 
import sys

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

from math import sqrt, floor

def solution_41(args):
    primes_list = get_all_primes(1000000)
    pandigital_primes = get_all_pandigital_primes(1000000000,primes_list)
    return max(pandigital_primes)

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
        if i%2 != 0:
            result = test_prime(i, primes_list)
            if result:
                primes_list.append(i)
    return primes_list

def get_all_pandigital_primes(max_val,primes_list):
    pandigitals = []
    for i in range(max_val+1):
        if i%2 != 0:
            str_i = str(i)
            size = len(str_i)
            if len(set(list(str_i))) == size:
                if "0" not in str_i and (size+1 < 10) and str(size+1) not in str_i:
                    result = test_prime(i, primes_list)
                    if result:
                        pandigitals.append(i)
                        #print(i)
    return pandigitals

def solution_42(args):
    return

def solution_43(args):
    import itertools
    pandigital_sum = 0
    for p in itertools.permutations('0123456789'):
        number = ''.join(p)
        if has_divisibility_property(number):
            pandigital_sum += int(number)
            logger.debug("Number Found: {}, Pandigital sum so far: {}".format(number,pandigital_sum))
    return pandigital_sum

def has_divisibility_property(number):
    divisors = [2, 3, 5, 7, 11, 13, 17]
    for i, divisor in enumerate(divisors):
        if int(number[i+1:i+4]) % divisor != 0:
            return False
    return True

def solution_44(args):
    n = 1
    found = False
    
    while not found:
        n += 1
        pn = pentagonal_number(n)
        
        for m in range(n - 1, 0, -1):
            pm = pentagonal_number(m)
            if is_pentagonal(pn + pm):
                logger.debug("Found Pentagonal Sum: {} + {} = {}".format(pn, pm, pn + pm))
                if is_pentagonal(abs(pn - pm)):
                    found = True
                    break
                
    return abs(pn - pm)

def pentagonal_number(n):
    return n * (3 * n - 1) // 2

def is_pentagonal(number):
    test_n = ((24 * number + 1) ** 0.5 + 1) / 6
    return test_n == int(test_n)

def solution_45(args):
    # All hexagonal numbers are triangular numbers so we can generate hexagonal numbers and test if they are pentagonal
    n = 144 # because we know we need a result greater than the 143rd hexagonal number
    while True:
        hexagonal_number = n * (2 * n - 1)
        if is_pentagonal(hexagonal_number):
            return hexagonal_number
        n += 1

def is_pentagonal(number):
    test_n = ((24 * number + 1) ** 0.5 + 1) / 6
    return test_n == int(test_n)

def solution_46(args):
    primes = get_all_primes(10000)
    logger.debug("Generated {} primes".format(len(primes)))

    n = 9
    while True:
        if n not in primes and check_goldbach_conjecture(n,primes):
            return n
        n += 2

def check_goldbach_conjecture(composite, primes):
    for prime in primes:
        if prime > composite:
            break
        remainder = composite - prime
        if ((remainder / 2) ** 0.5).is_integer():
            return False
    return True

def solution_47(args):
    # Distinct prime factors
    primes = get_all_primes(1000000)
    logger.debug("Generated {} primes".format(len(primes)))
    consecutive_numbers = []
    num = 2
    while len(consecutive_numbers) < 4:
        if count_distinct_prime_factors(num,primes) == 4:
            consecutive_numbers.append(num)
        else:
            consecutive_numbers = []
        num += 1
    logger.debug("4 Consecutive numbers Found: {}".format(consecutive_numbers))
    return consecutive_numbers[0]

def count_distinct_prime_factors(number, primes):
    factors = set()
    i = 0
    while number > 1:
        factor = primes[i]
        if number % factor == 0:
            factors.add(factor)
            number //= factor
        else:
            i += 1
    return len(factors)

def solution_48(args):
    return args

def solution_49(args):
    return args

def solution_50(args):
    return args

def main(argument_list):
    if len(argument_list) >= 2:
        solution_no = str(argument_list[1])
        args = argument_list[2:]
        solution_dict = {"41":solution_41,"42":solution_42,"43":solution_43,"44":solution_44,"45":solution_45,
                        "46":solution_46,"47":solution_47,"48":solution_48,"49":solution_49,"50":solution_50}
        answer = solution_picker(solution_dict.get(solution_no), args)
        logger.info(" Answer: {}".format(answer))
    else:
        logger.error(" ERROR: You must pass in a solution number")
        
def solution_picker(func,args):
    return func(args)

if __name__ == "__main__":
    main(list(sys.argv))
