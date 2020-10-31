
subs = {"at":"@","and":"&","one":"1","won":"1","too":"2","two":"2","to":"2","four":"4","for":"4","bea":"b","bee":"b","be":"b","sea":"c","see":"c","eye":"i","oh":"o","owe":"o","are":"r","you":"u","why":"y"}
for l in range(int(input())):
    l = input().split()
    st = ""
    for w in l:
        start = 0
        end = len(w)
        while start < end:
            for i in range(end, start - 1, -1):
                wo = w[start:i]
                wl = wo.lower()
                if wl in subs:
                    st += subs[wl].upper() if wo[0].isupper() else subs[wl]
                    start = i
                    break
                if start == i:
                    st += w[i]
                    start += 1

        st += " "
    print(st)
