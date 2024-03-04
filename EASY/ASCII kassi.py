n=int(input()) + 2
for _ in range(n):
    if _ in [0, n-1]:
        print("+" + "-"*(n-2) + "+")
    else:
        print("|" + " "*(n-2) + "|")
        