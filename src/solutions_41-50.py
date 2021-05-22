import pandas as pd 
import numpy as np 
import sys

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def solution_41(args):
    return args

def solution_42(args):
    return args

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
