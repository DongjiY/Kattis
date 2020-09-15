num = int(input())
if num % 2 != 0:
    print("Either")
else:
    if (num//2) % 2 == 0:
        print("Even")
    else:
        print("Odd")