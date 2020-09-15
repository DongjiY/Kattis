def convert(thelist):
    while '0' in thelist:
        thelist.remove('0')
    repetitions = 0
    while repetitions < len(thelist)-1:
        if thelist[repetitions] == thelist[repetitions+1]:
            thelist[repetitions] = str(int(thelist[repetitions])+int(thelist[repetitions+1]))
            del thelist[repetitions+1]
        repetitions += 1
    if len(thelist) < 4:
        for x in range(4-len(thelist)):
            thelist.append('0')
    else:
        return thelist
def backwards(thelist):
    while '0' in thelist:
        thelist.remove('0')
    repetitions = len(thelist)
    while repetitions-1 > 0:
        if thelist[repetitions-1] == thelist[repetitions-2]:
            thelist[repetitions-2] = str(int(thelist[repetitions-1])+int(thelist[repetitions-2]))
            del thelist[repetitions-1]
            repetitions -= 2
        else:
            repetitions -= 1
    if len(thelist) < 4:
        for x in range(4-len(thelist)):
            thelist.insert(0,'0')
    else:
        return thelist

board = {1:0,2:0,3:0,4:0,
        5:0,6:0,7:0,8:0,
        9:0,10:0,11:0,12:0,
        13:0,14:0,15:0,16:0}
arrayin = []
for i in range(4):
    arrayin += input().split()
#print(arrayin)
for x in range(len(arrayin)):
    board[x+1] = arrayin[x]
direction = int(input())
line1, line2, line3, line4 = [board[1],board[2],board[3],board[4]],[board[5],board[6],board[7],board[8]],[board[9],board[10],board[11],board[12]],[board[13],board[14],board[15],board[16]]
col1, col2, col3, col4 = [board[1],board[5],board[9],board[13]],[board[2],board[6],board[10],board[14]],[board[3],board[7],board[11],board[15]],[board[4],board[8],board[12],board[16]]
if direction == 0:
    convert(line1)
    convert(line2)
    convert(line3)
    convert(line4)
    totallines = line1+line2+line3+line4
    for x in range(16):
        board[x+1] = totallines[x]
    reps = 1
    while reps <= 16:
        print(board[reps]+" "+board[reps+1]+" "+board[reps+2]+" "+board[reps+3])
        reps += 4
elif direction == 1:
    convert(col1)
    convert(col2)
    convert(col3)
    convert(col4)
    totalcol = col1+col2+col3+col4
    boardindex = 1
    for x in range(4):
        for i in range(x,len(totalcol),4):
            board[boardindex] = totalcol[i]
            boardindex+=1
    reps = 1
    while reps <= 16:
        print(board[reps]+" "+board[reps+1]+" "+board[reps+2]+" "+board[reps+3])
        reps += 4
elif direction == 2:
    backwards(line1)
    backwards(line2)
    backwards(line3)
    backwards(line4)
    totallines = line1+line2+line3+line4
    for x in range(16):
        board[x+1] = totallines[x]
    reps = 1
    while reps <= 16:
        print(board[reps]+" "+board[reps+1]+" "+board[reps+2]+" "+board[reps+3])
        reps += 4
else:
    backwards(col1)
    backwards(col2)
    backwards(col3)
    backwards(col4)
    totalcol = col1+col2+col3+col4
    boardindex = 1
    for x in range(4):
        for i in range(x,len(totalcol),4):
            board[boardindex] = totalcol[i]
            boardindex+=1
    reps = 1
    while reps <= 16:
        print(board[reps]+" "+board[reps+1]+" "+board[reps+2]+" "+board[reps+3])
        reps += 4