def checkBoard(nums):
    rows = []
    for x in range(nums):
        thisInput = input()
        if thisInput.count('W') != thisInput.count('B'):
            return 0
        if "BBB" in thisInput or "WWW" in thisInput:
            return 0
        rows.append(thisInput)
    columns = []
    for x in range(nums):
        thisCol = ""
        for y in range(nums):
            thisCol += rows[y][x]
        columns.append(thisCol)
    # print(columns)
    for x in range(nums):
        if columns[x].count('W') != columns[x].count('B'):
            return 0
        if "BBB" in columns[x] or "WWW" in columns[x]:
            return 0
    return 1

nums = int(input())
print(checkBoard(nums))
