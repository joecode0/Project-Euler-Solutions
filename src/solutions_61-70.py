import pandas as pd 
import numpy as np 
import sys

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def solution_61(args):
    tria = get_triangle_numbers(4)
    logger.debug("First 3 tria dict entries: {}".format(list(tria.items())[:3]))
    logger.debug("Last 3 tria dict entries: {}".format(list(tria.items())[-3:]))
    squa = get_square_numbers(4)
    pent = get_pentagonal_numbers(4)
    hexa = get_hexagonal_numbers(4)
    hept = get_heptagonal_numbers(4)
    octa = get_octagonal_numbers(4)

    key_path = []
    logger.info("All values computed...")

    all_sets = {"squa":squa, "pent":pent, "hexa":hexa, "hept":hept, "octa":octa}
    used_sets = []

    for key, tria_values in tria.items():
        # Loop over each type of number for the 1st link
        for figurate_set_1_name in list(all_sets.keys()):
            figurate_set_1 = all_sets[figurate_set_1_name]
            # Now we've chosen the 1st set, add the key name to the used sets list
            used_sets = [figurate_set_1_name]
            
            # Loop over each value in the triangle set
            for tria_value in tria_values:
                # Test if there exists this 1st link
                figurate_set_1_values = figurate_set_1.get(tria_value)
                if figurate_set_1_values is not None:
                    # 1st link exists, so loop over each set to search for 2nd links
                    for figurate_set_2_name in [x for x in list(all_sets.keys()) if x not in used_sets]:
                        figurate_set_2 = all_sets[figurate_set_2_name]
                        used_sets = [figurate_set_1_name, figurate_set_2_name]
                        # Loop over each value in the 1st link set to test if there exists this 2nd link
                        for figurate_set_1_value in figurate_set_1_values:
                            # Test if there exists this 2nd link
                            figurate_set_2_values = figurate_set_2.get(figurate_set_1_value)
                            if figurate_set_2_values is not None:
                                # 2nd link exists, so loop over each set to search for 3rd links
                                for figurate_set_3_name in [x for x in list(all_sets.keys()) if x not in used_sets]:
                                    figurate_set_3 = all_sets[figurate_set_3_name]
                                    used_sets = [figurate_set_1_name, figurate_set_2_name, figurate_set_3_name]
                                    # Loop over each value in the 2nd link set
                                    for figurate_set_2_value in figurate_set_2_values:
                                        # Test if there exists this 3rd link
                                        figurate_set_3_values = figurate_set_3.get(figurate_set_2_value)
                                        if figurate_set_3_values is not None:
                                            # 3rd link exists, so loop over each set to search for 4th links
                                            for figurate_set_4_name in [x for x in list(all_sets.keys()) if x not in used_sets]:
                                                figurate_set_4 = all_sets[figurate_set_4_name]
                                                used_sets = [figurate_set_1_name, figurate_set_2_name, figurate_set_3_name, figurate_set_4_name]
                                                # Loop over each value in the 3rd link set
                                                for figurate_set_3_value in figurate_set_3_values:
                                                    # Test if there exists this 4th link
                                                    figurate_set_4_values = figurate_set_4.get(figurate_set_3_value)
                                                    if figurate_set_4_values is not None:
                                                        # 4th link exists, so loop over each set to search for 5th links
                                                        for figurate_set_5_name in [x for x in list(all_sets.keys()) if x not in used_sets]:
                                                            figurate_set_5 = all_sets[figurate_set_5_name]
                                                            used_sets = [figurate_set_1_name, figurate_set_2_name, figurate_set_3_name, figurate_set_4_name, figurate_set_5_name]
                                                            # Loop over each value in the 4th link set
                                                            for figurate_set_4_value in figurate_set_4_values:
                                                                # Test if there exists this 5th link
                                                                figurate_set_5_values = figurate_set_5.get(figurate_set_4_value)
                                                                if figurate_set_5_values is not None:
                                                                    # 5th link exists, so just check if this connects to original key
                                                                    logger.debug("Current full set name path: tria -> {} -> {} -> {} -> {} -> {}".format(figurate_set_1_name, figurate_set_2_name, figurate_set_3_name, figurate_set_4_name, figurate_set_5_name))
                                                                    logger.debug("Current full key path: {} -> {} -> {} -> {} -> {} -> {}".format(key, tria_value, figurate_set_1_value, figurate_set_2_value, figurate_set_3_value, figurate_set_4_value))
                                                                    logger.debug("Check if {} in {}".format(key, figurate_set_5_values))
                                                                    if key in figurate_set_5_values:
                                                                        key_path = [key, tria_value, figurate_set_1_value, figurate_set_2_value, figurate_set_3_value, figurate_set_4_value]
                                                                        logger.info("Key path found: {}".format(key_path))
                                                                        return compute_sum(key_path)

    return 0

def compute_sum(key_path):
    final_values = []
    for i in range(len(key_path)-1):
        final_values.append(int(str(key_path[i]) + str(key_path[i+1])))
    final_values.append(int(str(key_path[-1]) + str(key_path[0])))
    logger.info("Final values: {}".format(final_values))
    return sum(final_values)

def convert_to_dict(numbers, num_digits):
    output_dict = {}
    for number in numbers:
        str_num = str(number)
        if len(str_num) == num_digits:
            output_dict[str_num[:2]] = []
    for number in numbers:
        str_num = str(number)
        if len(str_num) == num_digits:
            output_dict[str(str_num[:2])].append(str(str_num[2:]))
    return output_dict

def get_triangle_numbers(num_digits):
    triangle_numbers = []
    n = 1
    val = 1
    while val < 10**num_digits:
        val = int(n*(n+1)/2)
        triangle_numbers.append(val)
        n += 1
    return convert_to_dict(triangle_numbers, num_digits)

def get_square_numbers(num_digits):
    square_numbers = []
    n = 1
    val = 1
    while val < 10**num_digits:
        val = int(n**2)
        square_numbers.append(val)
        n += 1
    return convert_to_dict(square_numbers, num_digits)

def get_pentagonal_numbers(num_digits):
    pentagonal_numbers = []
    n = 1
    val = 1
    while val < 10**num_digits:
        val = int(n*(3*n-1)/2)
        pentagonal_numbers.append(val)
        n += 1
    return convert_to_dict(pentagonal_numbers, num_digits)

def get_hexagonal_numbers(num_digits):
    hexagonal_numbers = []
    n = 1
    val = 1
    while val < 10**num_digits:
        val = int(n*(2*n-1))
        hexagonal_numbers.append(val)
        n += 1
    return convert_to_dict(hexagonal_numbers, num_digits)

def get_heptagonal_numbers(num_digits):
    heptagonal_numbers = []
    n = 1
    val = 1
    while val < 10**num_digits:
        val = int(n*(5*n-3)/2)
        heptagonal_numbers.append(val)
        n += 1
    return convert_to_dict(heptagonal_numbers, num_digits)

def get_octagonal_numbers(num_digits):
    octagonal_numbers = []
    n = 1
    val = 1
    while val < 10**num_digits:
        val = int(n*(3*n-2))
        octagonal_numbers.append(val)
        n += 1
    return convert_to_dict(octagonal_numbers, num_digits)




def solution_62(args):
    return args

def solution_63(args):
    return args

def solution_64(args):
    return args

def solution_65(args):
    return args

def solution_66(args):
    return args

def solution_67(args):
    df = pd.read_csv("C:/Users/joeco/Python/Project-Euler-Solutions/data/p067_triangle.csv")
    triangle = df['a'].tolist()
    d = [[0]]*len(triangle)
    for i in range(len(triangle)):
        data = str(triangle[i])
        new_list = [int(x) for x in data.split(" ")]
        d[i] = new_list
    
    rows = len(d)
    max_path = d
    max_path[-1] = d[-1]
    for i in range(2,rows+1):
        row = rows-i
        for j in range(len(d[row])):
            row_below = max_path[row+1]
            max_val = max(row_below[j],row_below[j+1])
            max_path[row][j] = d[row][j] + max_val

    return max_path[0][0]

def solution_68(args):
    return args

def solution_69(args):
    return args

def solution_70(args):
    return args

def main(argument_list):
    if len(argument_list) >= 2:
        solution_no = str(argument_list[1])
        args = argument_list[2:]
        solution_dict = {"61":solution_61,"62":solution_62,"63":solution_63,"64":solution_64,"65":solution_65,
                        "66":solution_66,"67":solution_67,"68":solution_68,"69":solution_69,"70":solution_70}
        answer = solution_picker(solution_dict.get(solution_no), args)
        logger.info(" Answer: {}".format(answer))
    else:
        logger.error(" ERROR: You must pass in a solution number")
        
def solution_picker(func,args):
    return func(args)

if __name__ == "__main__":
    main(list(sys.argv))
