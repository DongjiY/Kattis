digits = ['0','1','2','3','4','5','6','7','8','9']
originalpass = input()
passarray = input()
prepend = False
append = False
if originalpass[0] in digits and passarray in originalpass[1:]:
    prepend = True
if originalpass[-1] in digits and passarray in originalpass[0:-1]:
    append = True
flip =""
for x in range(len(passarray)):
    if passarray[x] not in digits:
        if passarray[x].isupper():
            flip += passarray[x].lower()
        elif passarray[x].islower():
            flip += passarray[x].upper()
    else:
        flip += passarray[x]
# print(flip)
# print(prepend)
# print(append)
if passarray==originalpass or flip==originalpass or prepend or append:
    print("Yes")
else:
    print("No")

# if passarray[0] in digits and originalpass in passarray[1:]:
#     prepend=True
# if passarray[-1] in digits and originalpass in passarray[0:-1]:
#     append = True