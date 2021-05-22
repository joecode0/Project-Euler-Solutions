import pandas as pd 
import numpy as np 
import sys

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def solution_31(args):
    return args

def solution_32(args):
    return args

def solution_33(args):
    return args

def solution_34(args):
    return args

def solution_35(args):
    return args

def solution_36(args):
    return args

def solution_37(args):
    return args

def solution_38(args):
    return args

def solution_39(args):
    return args

def solution_40(args):
    return args

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
