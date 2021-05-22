import pandas as pd 
import numpy as np 
import sys

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def solution_61(args):
    return 2*int(args[0])

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
