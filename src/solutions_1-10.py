import pandas as pd 
import numpy as np 
import sys

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def solution_1(args):
    return 2*int(args[0])

def solution_2(args):
    return args

def solution_3(args):
    return args

def solution_4(args):
    return args

def solution_5(args):
    return args

def solution_6(args):
    return args

def solution_7(args):
    return args

def solution_8(args):
    return args

def solution_9(args):
    return args

def solution_10(args):
    return args

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
