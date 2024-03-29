"""
Prints out 10 random numbers between 0 and 100.
"""

import random

NUM_RANDOM = 10
MIN_RANDOM = 0 
MAX_RANDOM = 100 

def main():
    for i in range(10):
        print(random.randint(MIN_RANDOM, MAX_RANDOM))

if __name__ == '__main__':
    main()
