n = int(input())
while n != -1:
    totalmiles = 0
    array=[]
    for i in range(n):
        array = array+(input().split())
    for i in range(0,len(array),2):
        if i >=2:
            totalmiles += int(array[i])*(int(array[i+1])-int(array[i-1]))
        else:
            totalmiles += int(array[i])*int(array[i+1])
    print(str(totalmiles)+" miles")
    n = int(input())