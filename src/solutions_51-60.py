import pandas as pd 
import numpy as np 
import sys

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def solution_51(args):
    return args

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
