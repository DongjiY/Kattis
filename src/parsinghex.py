import sys

hexa = ['0','1','2','3','4','5','6','7','8','9','a','A','b','B','c','C','d','D','e','E','f','F']
chars = []
for x in sys.stdin:
    chars += x
chars = "".join(chars)
indy = 0
hexas = []
while "0X" in chars[indy:] or "0x" in chars[indy:]:
    bigX = chars.find("0X",indy)
    lilX = chars.find("0x",indy)
    case = False
    if lilX < bigX:
        case = True
    if bigX == -1:
        case = True
    if lilX == -1:
        case = False
    if case:
        hexstr = "0x"
        index = chars.index("0x",indy)
        for x in range(index+2,len(chars)):
            if chars[x] in hexa:
                hexstr += chars[x]
            else:
                indy = x
                hexas.append(hexstr)
                break           
    else:
        hexstr = "0X"
        index = chars.index("0X",indy)
        for x in range(index+2,len(chars)):
            if chars[x] in hexa:
                hexstr += chars[x]
            else:
                indy = x
                hexas.append(hexstr)
                break
for x in hexas:
    toStr = int(x,16)
    print(x,str(toStr))