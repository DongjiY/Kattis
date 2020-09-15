
nums = int(input())
for x in range(nums):
    phrase = input().lower()
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in range(len(letters)-1,-1,-1):
        if letters[i] in phrase:
            del letters[i]
    missing = "".join(letters)
    if len(letters) == 0:
        print("pangram")
    else:
        print("missing " +missing)
        