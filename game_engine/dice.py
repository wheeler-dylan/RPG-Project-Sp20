#Author:        Dylan E. Wheeler
#Email:         dylan.wheeler@usm.edu
#Date:          2019 02 02
#Course:        CSC425 - Software Engineering II
#Prof.:         Dr. A. Louise Perkins

#this file contains functions to roll dice (produce random numbers)
#   and check for successful rolls against probability likelihoods

import random
import math
import sys


difficulty_grades = {
    "automatic":    sys.maxsize,
    "very_easy":    2.0,
    "easy":         1.5,
    "standard":     1.0,
    "hard":         0.67,
    "formidable":   0.5,
    "herculean":    0.1,
    "hopeless":     -1.0
    }
    
critical_target = 4     #rolling lower than this always succeeds
fumble_target = 96      #rolling higher than this always fails


#roll dice against a given probablity and return success/fail result (boolean)
def roll_check(f_probability, f_difficulty = "standard"):
    target = int(math.floor(float(f_probability) * difficulty_grades[f_difficulty]))
    print("Target:\t" + str(target))        #debugging

    roll = random.randrange(100) #produces a pseudorandom integer between 0 and 99 inclusively
    print("Roll:\t" + str(roll))            #debugging

    if (roll > fumble_target):
        print("Fumble!")        #debugging
        return False
    elif (roll < critical_target):
        print("Crit!")          #debugging
        return True
    elif (roll < target):
        print("Success!")       #debugging
        return True
    else:
        print("Fail!")          #debugging
        return False

#end roll check