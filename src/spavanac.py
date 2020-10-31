hours, minutes = [int(x) for x in input().split()]
if minutes >= 45:
    print(str(hours)+" "+str(minutes-45))
else:
    if hours-1 < 0:
        print(str(23)+" "+str(60-(45-minutes)))
    else: 
        print(str(hours-1)+" "+str(60-(45-minutes)))
