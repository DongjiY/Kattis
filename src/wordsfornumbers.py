numconv2 = {"10":"ten","11":"eleven","12":"twelve","13":"thirteen",
"14":"fourteen","15":"fifteen","16":"sixteen","17":"seventeen",
"18":"eighteen","19":"nineteen","2":"twenty","3":"thirty",
"4":"forty","5":"fifty","6":"sixty","7":"seventy","8":"eighty",
"9":"ninety","0":""}
numconv = {"1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine","0":"zero"}
while True:
    try:
        phrase = input().split()
        for x in range(len(phrase)):
            if phrase[x][0] in numconv:
                # print(phrase[x])
                if len(phrase[x]) == 1:
                    phrase[x] = numconv[phrase[x]]
                elif len(phrase[x]) == 2:
                    if phrase[x][0] == "1":
                        phrase[x] = numconv2[phrase[x]]
                    elif phrase[x][1] != "0":
                        phrase[x] = numconv2[phrase[x][0]]+"-"+numconv[phrase[x][1]]
                    else:
                        phrase[x] = numconv2[phrase[x][0]]+numconv2[phrase[x][1]]
        phrasetostring = " ".join(phrase)
        print(phrasetostring.capitalize())
    except:
        break