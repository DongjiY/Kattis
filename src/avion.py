count = 1
name = input()
output = ""
while True:
    try:
        if "FBI" in name:
            output += str(count) + " "
        count += 1
        name = input()
    except:
        break
if output == "":
    print("HE GOT AWAY!")
else:
    print(output)