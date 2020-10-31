while True:
    try:
        x = int(input())
        ones = 1
        count = 1
        while ones % x != 0:
            ones = (ones % x)*10 +1
            count += 1
        print(count)
    except:
        break