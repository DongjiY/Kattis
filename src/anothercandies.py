import sys
cases = []
for x in sys.stdin.readlines():
    a = x.rstrip()
    if a != '':
        b = int(a)
        cases.append(b)
cases.append(-1)
casenums = int(cases[0])
caselen = int(cases[1])
casestart = 1
thiscase = 1
while thiscase <= casenums:
    if sum(cases[casestart:casestart+caselen+1])%caselen==0:
        print("YES")
    else:
        print("NO")
    casestart = casestart+caselen+1
    caselen = int(cases[casestart])
    thiscase += 1



        



