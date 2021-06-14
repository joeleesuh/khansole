"""
Prints out a randomly generated addition problem
and checks if the user answers correctly.
"""

import random 

MIN_RANDOM = 10
MAX_RANDOM = 99

def main():
    random1 = random.randint(MIN_RANDOM, MAX_RANDOM)
    random2 = random.randint(MIN_RANDOM, MAX_RANDOM)

    print("What is " + str(random1) + "+" + str(random2) + "?")
    answer = int(input("Your answer: "))
    
    if (answer != (random1 + random2)):
        print("Incorrect.  The expected answer is " + str(random1 + random2))
    else:
        print("Correct!")

if __name__ == '__main__':
    main()
