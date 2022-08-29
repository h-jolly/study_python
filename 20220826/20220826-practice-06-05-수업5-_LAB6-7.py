# LAB 6-7 : 튜플의 활용
person = ('홍길동', 2019001, 179)
print('person =', person)

tmp = list(person)
tmp[1] = 2019003
person = tuple(tmp)

print('person =', person)
