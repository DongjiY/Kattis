y,p = input().split()
vowels = ['a','i','o','u']
if y[-1] == 'e':
    print(y+"x"+p)
elif y[-1] in vowels:
    print(y[:-1]+"ex"+p)
elif y[-2:] == "ex":
    print(y+p)
else:
    print(y+"ex"+p)