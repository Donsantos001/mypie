import random
import shelve
import pprint
import Capitals

qobj = Capitals.capitals

for guess in range(0, 34):
    ind = random.randint(0, 34)
    capital = list(qobj.keys())[ind]
    print("Type the capital of " + capital)
    ans = input()

    if ans in qobj.values():
        print("You got it in " + str(guess+1) + " guesses")
        break
    else:
        print("You missed it, the answer is " + capital + " "  + str(33-guess) + " more guesses")