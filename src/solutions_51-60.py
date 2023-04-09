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
    return args

def solution_53(args):
    return args

def solution_54(args):
    return args

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
