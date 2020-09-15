alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
while True:
    try:
        user = input().split()
        # print(user)
        username = ""
        totalheart = 0
        count = 0
        for x in range(len(user)):
            if user[x][0] in alpha:
                username += user[x] + " "
            else:
                totalheart += float(user[x])
                count += 1
        avgrate = totalheart/count
        print("{:.6f}".format(avgrate)+" "+username)
    except:
        break