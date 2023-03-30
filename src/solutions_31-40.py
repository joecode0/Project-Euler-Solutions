import pandas as pd 
import numpy as np 
import sys

from math import sqrt, floor, gcd, factorial, log10

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# TODO: Solution 31
def solution_31(args):
    return args

def solution_32(args):
    all_products = set([])
    for i in range(1,10000):
        for j in range(1,10000):
            product = i*j
            if len(str(i)) + len(str(j)) + len(str(product)) < 10:
                potential = all_unique(str(product))
                if potential:
                    pandigital = test_pandigital(i,j,product)
                    if pandigital:
                        print("{} * {} = {} is pandigital".format(i,j,product))
                        all_products.add(product)

    return sum(all_products)

def all_unique(product):
    numbers = []
    for num in product:
        numbers.append(num)
    if len(set(numbers)) == len(product):
        return True
    else:
        return False

def test_pandigital(i,j,product):
    all_string = str(i) + str(j) + str(product)
    for num in "123456789":
        if num not in all_string:
            return False
    return True

def solution_33(args):
    from math import gcd
    final_fractions = []
    for fraction in generate_all_potential_fractions():
        #print("Fraction = {}".format(fraction))
        a = remove_common_digit(fraction)
        #print("a = {}".format(a))
        a_simplified = get_simplified_fraction(a)
        #print("a_simplified = {}".format(a_simplified))
        fraction_simplified = get_simplified_fraction(fraction)
        #print("fraction_simplified = {}".format(fraction_simplified))
        if a_simplified == fraction_simplified:
            nominator = a_simplified.split("/")[0]
            denominator = a_simplified.split("/")[1]
            if nominator < denominator:
                #print((fraction,a_simplified))
                final_fractions.append((fraction,a_simplified))
            
    final_nominator = 1
    final_denominator = 1
    for pair in final_fractions:
        fraction_string = pair[1]
        nominator = int(fraction_string.split("/")[0])
        denominator = int(fraction_string.split("/")[1])
        final_nominator *= nominator
        final_denominator *= denominator
    final_string = str(final_nominator) + "/" + str(final_denominator)
    return get_simplified_fraction(final_string).split("/")[1]

def generate_all_potential_fractions():
    all_fractions = set([])
    for i in "123456789":
        common_digit = i
        for j in "0123456789":
            other_top_digit = j
            for k in "0123456789":
                other_bottom_digit = k
                all_fractions.add(str(i + j + "/" + i + k))
                if j != "0":
                    all_fractions.add(str(j + i + "/" + i + k))
                if k != "0":
                    all_fractions.add(str(i + j + "/" + k + i))
    return all_fractions   

def get_simplified_fraction(fraction_string):
    #print(fraction_string)
    nominator = int(fraction_string.split("/")[0])
    denominator = int(fraction_string.split("/")[1])
    divisor = gcd(nominator,denominator)
    if divisor == 0:
        return fraction_string
    else:
        final_top = int(nominator/divisor)
        final_bottom = int(denominator/divisor)
        return str(final_top) + "/" + str(final_bottom)

def remove_common_digit(fraction_string):
    nominator = fraction_string.split("/")[0]
    denominator = fraction_string.split("/")[1]
    for digit_string in nominator:
        if digit_string in denominator:
            if nominator[0] == nominator[1]:
                new_top = nominator[0]
            else:
                new_top = nominator.replace(digit_string,"")
            if denominator[0] == denominator[1]:
                new_bottom = denominator[0]
            else:
                new_bottom = denominator.replace(digit_string,"")
            new_fraction = new_top + "/" + new_bottom
            return new_fraction
    #print("no common digit")
    return fraction_string

def solution_34(args):
    from math import factorial
    digit_factorials = {"0":1}
    for i in range(1,10):
        digit_factorials[str(i)] = factorial(i)
    
    total_output = 0

    for i in range(3,999999):
        digits = [int(x) for x in str(i)]
        factorial_sum = 0
        for digit in digits:
            factorial_sum += digit_factorials.get(str(digit))
        if i == factorial_sum:
            total_output += i
            print("{}: sum = {}".format(i,factorial_sum))
    return total_output

def solution_35(args):
    known_primes = set(get_all_primes(1000000))
    known_primes = sorted([x for x in known_primes if no_never_prime_digits(x)])
    known_primes_left_to_check = set(known_primes.copy())
    all_circular_primes = []
    for prime in known_primes:
        if prime in known_primes_left_to_check:
            rotations = get_all_other_rotations(prime)
            circular = True
            for rot in rotations:
                if rot not in known_primes_left_to_check:
                    circular = False
                    break
            if circular:
                all_circular_primes.extend(list(set(rotations + [prime])))
                known_primes_left_to_check -= set(rotations + [prime])
            else:
                known_primes_left_to_check.remove(prime)
    return len(all_circular_primes)

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

def get_all_other_rotations(val):
    all_rotations = []
    str_val = str(val)
    for i in range(len(str_val)-1):
        str_val = str_val[1:] + str_val[0]
        all_rotations.append(int(str_val))
    return all_rotations

def no_never_prime_digits(x):
    str_x = str(x)
    if x < 10:
        return True
    if "0" in str_x:
        return False
    if "2" in str_x:
        return False
    if "4" in str_x:
        return False
    if "6" in str_x:
        return False
    if "8" in str_x:
        return False
    if "5" in str_x:
        return False
    return True

def solution_36(args):
    # Problem 36: Double-base palindromes
    from math import floor

    powers_of_two = generate_powers_of_two(1000000)
    all_double_palindromes = []
    for i in range(1,1000000):
        str_val = str(i)
        if str_val[0] == str_val[-1]:
            isPalindrome = is_palindrome(str_val)
        else:
            isPalindrome = False
        if isPalindrome:
            binary_string = decimal_to_binary(i,powers_of_two)
            if binary_string[-1] == "1":
                bothPalindrome = is_palindrome(binary_string)
            else:
                bothPalindrome = False
        else:
            bothPalindrome = False
        if bothPalindrome:
            #print("{} == {}".format(str_val,binary_string))
            all_double_palindromes.append(i)
    return sum(all_double_palindromes)  

def is_palindrome(str_val):
    for i in range(floor(len(str_val)/2)):
        first_digit = str_val[i]
        last_digit = str_val[-(i+1)]
        if first_digit != last_digit:
            return False
    return True

def generate_powers_of_two(max_val):
    val = 2**0
    powers_of_two = set([val])
    while val < max_val:
        powers_of_two.add(val)
        val *= 2
    return sorted(list(powers_of_two),reverse=True)

def decimal_to_binary(val,powers_of_two):
    binary_string = ""
    non_zero_found = False
    for power in powers_of_two:
        if power <= val:
            val -= power
            binary_string += "1"
            non_zero_found = True
        else:
            if non_zero_found:
                binary_string += "0"
    return binary_string

def solution_37(args):
    # Problem 37: Truncatable primes
    limit = 1000000
    primes = get_all_primes(limit)
    logger.debug("Found {} primes".format(len(primes)))
    trunc_primes = []
    i = 4
    while len(trunc_primes) < 11:
        if is_truncatable_prime(primes[i], primes):
            trunc_primes.append(primes[i])
            logger.debug("Found truncatable prime: {}".format(primes[i]))
        i += 1
        if i >= len(primes) and len(trunc_primes) < 11:
            logger.debug("Limit reached, increasing to {}".format(limit*10))
            limit *= 10
            primes = get_all_primes(limit)
    return sum(trunc_primes)

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

def is_truncatable_prime(prime, primes):
    if prime < 10:
        return False
    prime_str = str(prime)
    for i in range(1, len(prime_str)):
        if int(prime_str[i:]) not in primes or int(prime_str[:i]) not in primes:
            return False
    return True

def solution_38(args):
    # Problem 38: Pandigital numbers
    # Number has to begin with 9, and be 4 digits big
    # Because 9xxx * 2 = 18xxx or 19xxx
    # Therefore, 9 digit number is 9xxx18xxx or 9xxx19xxx
    # Cannot be second number, therefore number must be 90xx18xxx or 91xx18xxx or 92xx18xxx or 93xx18xxx or 94xx18xxx
    # Cannot be second number, therefore number must be 90xx18xxx or 92xx18xxx or 93xx18xxx or 94xx18xxx
    # Must be bigger than 918273645, therefore number must be 92xx18xxx or 93xx18xxx or 94xx18xxx
    # Therefore we know number must range from 9200-9499
    # So 4th number can never be a 4,9,1,8 and either 2 or 3 or 4

    possible_numbers = [x for x in range(9200,9500) if isValid(x)]
    pandigital_numbers = []
    for number in possible_numbers:
        product = double_and_concatenate(number)
        unique_length = len(set(list(product)))
        if unique_length == 9 and "0" not in product:
            pandigital_numbers.append(product)

    final_values = [int(x) for x in pandigital_numbers]
    #print(final_values)
    return max(final_values)

def isValid(x):
    if "1" in str(x):
        return False
    if "8" in str(x):
        return False
    last_digit = int(str(x)[-1])
    if last_digit in [4,9,1,8]:
        return False
    second_digit = int(str(x)[1])
    if last_digit == second_digit:
        return False
    third_digit = int(str(x)[2])
    if second_digit == third_digit:
        return False
    if third_digit == last_digit:
        return False
    if last_digit == 0:
        return False
    if third_digit == 9:
        return False
    double_last = last_digit * 2
    if str(double_last)[-1] in str(x)[:-1]:
        return False
    return True

def double_and_concatenate(x):
    output = str(x)
    doubled = 2*x
    output += str(doubled)
    return output

def solution_39(args):
    from math import sqrt
    all_solutions_dict = {}
    all_solutions_count_dict = {}
    square_numbers = set([x**2 for x in range(1001)])
    for i in range(2,1001):
        all_solutions_count_dict[str(i)] = 0
        all_solutions_dict[str(i)] = []
    for a in range(2,1001):
        a_sqrd = a**2
        for b in range(a,1001):
            b_sqrd = b**2
            p = a+b
            if (p+max(a,b)) <= 1000:
                c_sqrd = a_sqrd+b_sqrd
                if c_sqrd in square_numbers:
                    c = int(sqrt(c_sqrd))
                    p += c
                    if p <= 1000:
                        all_solutions_dict[str(p)].append([a,b,c])
                        all_solutions_count_dict[str(p)] += 1
                        #print(p)
    max_count = 1
    max_i = 2
    for i in range(2,1001):
        count = all_solutions_count_dict[str(i)]
        if count > max_count:
            #print("{} has {} solutions: {}".format(i,count,all_solutions_dict[str(i)]))
            count = max_count 
            max_i = i 
    return max_i

def solution_40(args):
    # Problem 40: Champernowne's constant
    i = 0
    number = 1
    string = ""
    while i < 1000000:
        cur_string = str(number)
        string += cur_string
        i += len(cur_string)
        number += 1
    d_1 = int(string[0])
    d_10 = int(string[9])
    d_100 = int(string[99])
    d_1000 = int(string[999])
    d_10000 = int(string[9999])
    d_100000 = int(string[99999])
    d_1000000 = int(string[999999])
    product = d_1*d_10*d_100*d_1000*d_10000*d_100000*d_1000000
    return product

def main(argument_list):
    if len(argument_list) >= 2:
        solution_no = str(argument_list[1])
        args = argument_list[2:]
        solution_dict = {"31":solution_31,"32":solution_32,"33":solution_33,"34":solution_34,"35":solution_35,
                        "36":solution_36,"37":solution_37,"38":solution_38,"39":solution_39,"40":solution_40}
        answer = solution_picker(solution_dict.get(solution_no), args)
        logger.info(" Answer: {}".format(answer))
    else:
        logger.error(" ERROR: You must pass in a solution number")
        
def solution_picker(func,args):
    return func(args)

if __name__ == "__main__":
    main(list(sys.argv))
