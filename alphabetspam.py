uppercase = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lowercase = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
linein = input()
upcount, lowcount, space, symbol = 0,0,0,0
for x in range(len(linein)):
    if linein[x] in uppercase:
        upcount += 1
    elif linein[x] in lowercase:
        lowcount += 1
    elif linein[x] == "_":
        space += 1
    else:
        symbol += 1
print(space/len(linein))
print(lowcount/len(linein))
print(upcount/len(linein))
print(symbol/len(linein))