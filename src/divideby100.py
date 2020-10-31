def find(newstr1):
    newstr1 = newstr.rstrip('0')
    try:
        x = newstr1[newstr1.index('.')+1]
    except IndexError:
        return newstr1.rstrip('.')
    if newstr1.index('.') == 0:
        return "0"+newstr1
    return newstr1

N = input()
M = input()
back = len(M)-1
if len(N) < len(M):
    newstr = "."+M[len(N)+1:]+N
else:
    newstr = N[:len(N)-back]+"."+N[len(N)-back:]
print(find(newstr))


