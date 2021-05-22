import pandas as pd 
import numpy as np 
import sys

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def solution_21(args):
    return args

def solution_22(args):
    return args

def solution_23(args):
    return args

def solution_24(args):
    return args

def solution_25(args):
    return args

def solution_26(args):
    return args

def solution_27(args):
    return args

def solution_28(args):
    return args

def solution_29(args):
    return args

def solution_30(args):
    return args

def main(argument_list):
    if len(argument_list) >= 2:
        solution_no = str(argument_list[1])
        args = argument_list[2:]
        solution_dict = {"21":solution_21,"22":solution_22,"23":solution_23,"24":solution_24,"25":solution_25,
                        "26":solution_26,"27":solution_27,"28":solution_28,"29":solution_29,"30":solution_30}
        answer = solution_picker(solution_dict.get(solution_no), args)
        logger.info(" Answer: {}".format(answer))
    else:
        logger.error(" ERROR: You must pass in a solution number")
        
def solution_picker(func,args):
    return func(args)

if __name__ == "__main__":
    main(list(sys.argv))
