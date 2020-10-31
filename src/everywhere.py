dataset = int(input())
for x in range(dataset):
    cities = int(input())
    citylist = set(())
    for y in range(cities):
        citylist.add(input())
    print(len(citylist))
    