
# def findVal(moves,thisMove):
#     for y in range(len(moves)-1,-1,-1):
#         if "RESTART" in moves[y]:
#             return moves[y][1]
#         if "SET" in moves[y] and moves[y][1] == thisMove[1]:
#             return moves[y][2]
#     return "0"

# def findVal(moves,thisMove):
#     for y in range(len(moves)-1,-1,-1):
#         if "RESTART" in moves[y]:
#             return moves[y][1]
#         elif "SET" in moves[y] and moves[y][1] == thisMove[1]:
#             return moves[y][2]
#     return "0"

# n,q = [int(x) for x in input().split()]
# moves = []
# correspondence = []
# for x in range(q):
#     # print(moves)
#     # print(correspondence)
#     thisMove = input().split()
#     if "PRINT" not in thisMove:
#         if thisMove[0] == "RESTART":
#             moves.clear()
#             correspondence.clear()
#             moves.append(thisMove[0])
#             correspondence.append(thisMove[1])
#         elif thisMove[0] == "SET":
#             if "SET"+thisMove[1] in moves:
#                 index = moves.index("SET"+thisMove[1])
#                 moves.remove("SET"+thisMove[1])
#                 del correspondence[index]
#             moves.append(thisMove[0]+thisMove[1])
#             correspondence.append(thisMove[-1])
#     else:
#         if "SET"+thisMove[1] not in moves:
#             if "RESTART" in moves:
#                 print(correspondence[0])
#             else:
#                 print(0)
#         elif "SET"+thisMove[1] in moves:
#             print(correspondence[moves.index("SET"+thisMove[1])])


# n, q = [int(x) for x in input().split()]
# m = [[0, 0]] * n # [price, index]
# c = [-1, 0]
# for i in range(q):
#     # print(m)
#     x = input().split()
#     s = x[0]
#     if s == 'SET':
#         m[int(x[1]) - 1] = [i, int(x[2])]
#     elif s == 'PRINT':
#         a = int(x[1]) - 1
#         if m[a][0] > c[0]:
#             print(m[a][1])
#         else:
#             print(c[1])
#     elif s == 'RESTART':
#         c = [i, int(x[1])]

# n,q = [int(x) for x in input().split()]
# users = [0]*n
# every = 0
# # print(users)
# for x in range(q):
#     phrase = input().split()
#     if phrase[0] == "SET":
#         users[int(phrase[1])-1] = int(phrase[2])
#     elif phrase[0] == "RESTART":
#         every = int(phrase[1])
#         users = [0]*n
#     elif phrase[0] == "PRINT":
#         if users[int(phrase[1])-1] == 0:
#             print(every)
#         else:
#             print(users[int(phrase[1])-1])

n,q = [int(x) for x in input().split()]
users = [[0,0]]*n
restartlst = [-99,0]
for x in range(q):
    phrase = input().split()
    if phrase[0] == "SET":
        users[int(phrase[1])-1] = [x,int(phrase[-1])]
    elif phrase[0] == "RESTART":
        restartlst = [x,int(phrase[-1])]
    elif phrase[0] == "PRINT":
        if users[int(phrase[-1])-1][0] > restartlst[0]:
            print(users[int(phrase[-1])-1][1])
        else:
            print(restartlst[1])