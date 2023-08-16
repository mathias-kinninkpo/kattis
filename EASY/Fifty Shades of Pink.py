c = 0
for i in range(int(input())):
    color = input()
    if "rose" in color.lower() or "pink" in color.lower():
        c += 1
if c == 0:print("I must watch Star Wars with my daughter")
else:print(c)