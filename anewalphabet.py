alpha = {'A':"@", 'B':"8", 'C':"(", 'D':"|)", 'E':"3", 'F':"#", 'G':"6", 'H':"[-]", 'I':"|", 'J':"_|", 'K':"|<", 'L':"1", 'M':"[]\/[]", 'N':"[]\[]", 'O':"0", 'P':"|D", 'Q':"(,)", 'R':"|Z", 'S':"$", 'T':"']['", 'U':"|_|", 'V':"\/", 'W':"\/\/", 'X':"}{", 'Y':"`/", 'Z':"2"}
readphrase = input()
phrase = readphrase.upper()
chararray = list(phrase)
newphrase = ""
for i in chararray:
    if i in alpha:
        lettertoadd = alpha[i]
        newphrase += lettertoadd
    else:
        newphrase += str(i)
print(newphrase)