# 연습문제 12
x, y = input('좌표를 입력해주세요.(X Y) : ').split()

x = int(x)
y = int(y)

# 반지름
r = (x*x + y*y) ** 0.5

print('원의 {}부에 있음'.format('내' if r < 5 and r > -5 else '외'))


# 연습문제 13
print()
x, y = input('좌표를 입력해주세요.(X Y) : ').split()

x = int(x)
y = int(y)

r = ((x *y) ** 0.5) ** -0.5
print('원의 {}부에 있음'.format('내' if r < 10 and r > -10 else '외'))
