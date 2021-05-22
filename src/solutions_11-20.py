import pandas as pd 
import numpy as np 
import sys

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def solution_11(args):
    return args

def solution_12(args):
    return args

def solution_13(args):
    return args

def solution_14(args):
    return args

def solution_15(args):
    return args

def solution_16(args):
    return args

def solution_17(args):
    return args

def solution_18(args):
    return args

def solution_19(args):
    return args

def solution_20(args):
    return args

def main(argument_list):
    if len(argument_list) >= 2:
        solution_no = str(argument_list[1])
        args = argument_list[2:]
        solution_dict = {"11":solution_11,"12":solution_12,"13":solution_13,"14":solution_14,"15":solution_15,
                        "16":solution_16,"17":solution_17,"18":solution_18,"19":solution_19,"20":solution_20}
        answer = solution_picker(solution_dict.get(solution_no), args)
        logger.info(" Answer: {}".format(answer))
    else:
        logger.error(" ERROR: You must pass in a solution number")
        
def solution_picker(func,args):
    return func(args)

if __name__ == "__main__":
    main(list(sys.argv))
