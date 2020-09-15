vote = input()
votesdict = {}
while vote != "***":
    if vote in votesdict.keys():
        votesdict[vote] = votesdict.get(vote)+1
    else:
        votesdict[vote] = 1
    vote = input()
votecounts = list(votesdict.values())
votecandidates = list(votesdict.keys())
# print(votecandidates,votecounts)
if votecounts.count(max(votecounts)) > 1:
    print("Runoff!")
else:
    print(votecandidates[votecounts.index(max(votecounts))])