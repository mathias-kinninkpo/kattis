from collections import Counter
print("yes" if Counter(input().split()).most_common(1)[0][1] == 1 else "no")