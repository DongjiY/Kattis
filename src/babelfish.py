trans = {}
words = input()
while words != "":
    wordpart = words.split()
    trans[wordpart[1]] = wordpart[0]
    words = input()
# print(trans)
cases = input()
while True:
    try:
        if cases in trans.keys():
            print(trans[cases])
        else:
            print("eh")
        cases = input()
    except:
        break
