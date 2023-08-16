# def isdouble(l):
#     return len(list(filter(lambda x: x%2 == 0, l))) >= 2
# n,m = map(int, input().split())
# lis = list(map(int, input().split()))
# c = 0
# a = 0
# listes = []
# for i in range(n):
#     # print(lis[i:i+m])
#     if isdouble(lis[i:i+m]) == True and lis[i:i+m] not in listes:
#         listes.append(lis[i:i+m])
#         # print(lis[i:i+m])
# print(len(listes))



# n,m = map(int, input().split())
# al = True
# l = []
# for i in range(n):l.append(int(input()))
# for i in range(n-1):
#     if not (l[i] + m) <= l[i+1]: al = False
# print("YES" if al else "NO")

def mars1(year):
    return ((23*5)//9+1+2+year+(year//4)-(year//100)+(year//400))%7
def juin1(year):
    return ((23*6)//9+1+2+year+(year//4)-(year//100)+(year//400))%7


def Leap(year):
    return year%400 == 0 or (year % 4 == 0 and year %100 != 0)
year = int(input())
if Leap(year):
    print(((152+(7-juin1(year))%7+14) - (121+(7 - mars1(year))%7+7))//7, "weeks")
else:print(((151+(7-juin1(year))%7+14) - (120+(7 - mars1(year))%7+7))//7, "weeks")