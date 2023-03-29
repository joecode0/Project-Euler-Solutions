import sys
import time

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

from math import sqrt, floor

def solution_1(args):
    return print(sum([x for x in range(1000) if x%3 == 0 or x%5 == 0]))

def solution_2(args):
    two_prev = 1
    one_prev = 2
    sum_2 = 2
    while one_prev <= 4000000:
        new_val = two_prev + one_prev
        if new_val%2 == 0:
            sum_2 += new_val
        two_prev = one_prev
        one_prev = new_val
    return sum_2

def solution_3(args):
    prime = 600851475143
    t0 = time.time()
    largest_prime_factor = 2
    last_prime = 2
    known_primes = [2,3,5,7,11,13,17,19,23]
    while prime > 1:
        cur_prime = last_prime
        while prime%cur_prime != 0:
            cur_prime = get_next_prime(cur_prime,known_primes)
            known_primes.append(cur_prime)
        prime /= cur_prime
        largest_prime_factor = max(largest_prime_factor,cur_prime)
        last_prime = cur_prime
    return largest_prime_factor

def get_primes_under_val(val,known_primes):
    return [x for x in known_primes if x <= val]

def test_prime(prime,known_primes):
    if prime in known_primes:
        return True
    testable_max = floor(sqrt(prime))
    testable_primes = get_primes_under_val(testable_max,known_primes)
    isPrime = True
    for test_prime in testable_primes:
        if prime%test_prime == 0:
            isPrime = False
            break
    return isPrime

def get_next_prime(prime,known_primes):
    not_found = True
    while not_found:
        prime += 1
        not_found = not(test_prime(prime,known_primes))
    return prime

def solution_4(args):
    max_palindrome = 0
    largest_solution = ""
    for i in range(900):
        i_val = 999-i
        for j in range(900):
            j_val = 999-j
            val = i_val*j_val
            if test_palindrome(val):
                if val > max_palindrome:
                    max_palindrome = val
                    largest_solution = str(i_val) + "*" + str(j_val) + " = " + str(val)
                break
    return largest_solution

def test_palindrome(num):
    str_num = str(num)
    if str_num[0] != str_num[-1]:
        return False
    length = len(str_num)
    if length%2 == 0:
        comparisons = int(length/2)
    else:
        comparisons = int(floor(length/2))
    for i in range(comparisons):
        if str_num[i] != str_num[-(i+1)]:
            return False
    return True

def solution_5(args):
    current_adder, total, i = [20]*3
    while i > 11:
        if total%(i-1) == 0:
            current_adder = total
            i -= 1
        else:
            total += current_adder
    return total

def solution_6(args):
    sum_square = sum(range(101))**2

    square_sum = 1
    for i in range(2,101):
        square_sum += i**2

    return sum_square-square_sum

def solution_7(args):
    known_primes = [2,3,5,7,11]
    for i in range(5,10001):
        next_prime = get_next_prime(known_primes[-1],known_primes)
        known_primes.append(next_prime)
    return known_primes[-1]

def solution_8(args):
    number = str(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)
    max_product = 1
    for i in range(len(number)-13):
        current_number = str(number[i:i+13])
        if "0" not in current_number:
            product = get_product(current_number)
            max_product = max(product,max_product)
    return max_product

def get_product(current_number):
    product = 1
    for i in range(len(current_number)):
        product *= int(current_number[i])
    return product

def solution_9(args):
    square_numbers = set([x**2 for x in range(1,701)])
    outputs = []
    for i in range(1,501):
        a2 = i**2
        for j in range(1,501):
            b2 = j**2
            c2 = a2+b2
            if c2 in square_numbers:
                sum_ = i+j+sqrt(c2)
                if sum_ == 1000:
                    outputs.append([i,j,sqrt(c2),i*j*sqrt(c2)])
                    break
    return outputs

def solution_10(args):
    known_primes = [2,3,5,7,11,13,17,19,23]
    prime = 23
    sum_ = sum(known_primes)-23
    while prime < 2000000:
        sum_ += prime
        prime = get_next_prime(prime,known_primes)
        if prime < 1500:
            known_primes.append(prime) # only need primes up to sqrt(2 million)
    return sum_

def main(argument_list):
    if len(argument_list) >= 2:
        solution_no = str(argument_list[1])
        args = argument_list[2:]
        solution_dict = {"1":solution_1,"2":solution_2,"3":solution_3,"4":solution_4,"5":solution_5,"6":solution_6,
                        "7":solution_7,"8":solution_8,"9":solution_9,"10":solution_10}
        answer = solution_picker(solution_dict.get(solution_no), args)
        logger.info(" Answer: {}".format(answer))
    else:
        logger.error(" ERROR: You must pass in a solution number")
        
def solution_picker(func,args):
    return func(args)

if __name__ == "__main__":
    main(list(sys.argv))
