
notes = {"A#":"Bb","C#":"Db","D#":"Eb","F#":"Gb","G#":"Ab"}
count = 1
while True:
    try:
        note,scale = input().split()
        newscale = ""
        for x in notes:
            # print(x,note)
            if x == note:
                newscale = notes[x] + " "+ scale
                break
            elif notes[x] == note:
                newscale = x + " "+ scale
                break
            else:
                newscale = "UNIQUE"
        print("Case "+str(count)+": "+newscale)
        count += 1
    except:
        break