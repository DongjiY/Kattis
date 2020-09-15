from collections import Counter
from collections import OrderedDict
import string

def printwords(wordlst,num):
    correctwords = []
    frequency = OrderedDict(Counter(wordlst))
    # print(frequency, type(frequency))
    newfrequency = OrderedDict(sorted(frequency.items()))
    # print(newfrequency, type(newfrequency))
    if num in newfrequency.values():
        for x,y in newfrequency.items():
            if y == num:
                print(x)
    else:
        print("There is no such word.")

nums = int(input())
stringlst = []
thisInput = input()
while True:
    try:
        if thisInput == "EndOfText":
            # print(stringlst)
            printwords(stringlst,nums)
            print()
            stringlst = []
            nums = int(input())
            thisInput = input()
        if thisInput == "":
            thisInput = input()
        else:
            thisInput = thisInput.lower()
            formatted = thisInput.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation)))
            stringlst += formatted.split()
            thisInput = input()
    except:
        break



