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

def solution_43(args):
    return args

def solution_44(args):
    return args

def solution_45(args):
    return args

def solution_46(args):
    return args

def solution_47(args):
    return args

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
