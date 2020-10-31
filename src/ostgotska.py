phraselst = input().split()
count = 0
for x in phraselst:
    if "ae" in x:
        count += 1
if count/len(phraselst) >= .4:
    print("dae ae ju traeligt va")
else:
    print("haer talar vi rikssvenska")