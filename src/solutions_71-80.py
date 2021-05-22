import pandas as pd 
import numpy as np 
import sys

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def solution_71(args):
    return args

def solution_72(args):
    return args

def solution_73(args):
    return args

def solution_74(args):
    return args

def solution_75(args):
    return args

def solution_76(args):
    return args

def solution_77(args):
    return args

def solution_78(args):
    return args

def solution_79(args):
    return args

def solution_80(args):
    return args

def main(argument_list):
    if len(argument_list) >= 2:
        solution_no = str(argument_list[1])
        args = argument_list[2:]
        solution_dict = {"71":solution_71,"72":solution_72,"73":solution_73,"74":solution_74,"75":solution_75,
                        "76":solution_76,"77":solution_77,"78":solution_78,"79":solution_79,"80":solution_80}
        answer = solution_picker(solution_dict.get(solution_no), args)
        logger.info(" Answer: {}".format(answer))
    else:
        logger.error(" ERROR: You must pass in a solution number")
        
def solution_picker(func,args):
    return func(args)

if __name__ == "__main__":
    main(list(sys.argv))
