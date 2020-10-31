phrase = input()
interval = int(len(phrase)/3)
one = phrase[0: interval]
mid = phrase[interval:-interval]
end = phrase[-interval:]
if one == end or one == mid:
    correctword = one
else:
    correctword = mid
print(correctword)