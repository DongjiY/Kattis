people,chicken = [int(x) for x in input().split()]
if chicken - people >= 0:
    if chicken - people == 1:
        print("Dr. Chaz will have "+str(chicken-people)+" piece of chicken left over!")
    else:
        print("Dr. Chaz will have "+str(chicken-people)+" pieces of chicken left over!")
else:
    if abs(chicken-people) == 1:
        print("Dr. Chaz needs "+str(abs(chicken-people))+" more piece of chicken!")
    else:
        print("Dr. Chaz needs "+str(abs(chicken-people))+" more pieces of chicken!")