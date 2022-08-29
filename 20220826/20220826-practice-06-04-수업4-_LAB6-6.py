# LAB 6-6 : 튜플의 생성과 패킹, 언패킹
the_day = (1919, 3, 1)
year, month, day = the_day
print('year =', year)
print('month =', month)
print('day =', day)

print()

tmp = [10, 20, 30]
tup = tuple(tmp)
a, b, c = tmp
print('a =', a)
print('b =', b)
print('c =', c)
