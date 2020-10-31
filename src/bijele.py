pieces = [1,1,2,2,2,8]
board = [int(x) for x in input().split()]
output = []
for x in range(len(board)):
    output.append(str(pieces[x]-board[x]))
print(" ".join(output))