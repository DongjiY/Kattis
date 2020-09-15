originalphrase = input().split()
newphraseset = set(originalphrase)
if len(originalphrase) != len(newphraseset):
    print("no")
else:
    print("yes")
