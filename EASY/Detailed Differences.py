for i in range(int(input())):
    text1, text2 = input(),input()
    print(text1)
    print(text2)
    for a,b in zip(text1, text2):
        print('.' if a == b else "*", end="")
    print("")