# LAB 6-8 : 튜플의 반환
def square(a, b):
    return a ** 2, b ** 2

x = 10
y = 20
x_sq, y_sq = square(x, y)
print('1) {} 제곱 = {}, {} 제곱 = {}'.format(x, x_sq, y, y_sq))

print('2) (10, 20, 30) + (40, 50, 60) = {}'.format((10, 20, 30) + (40, 50, 60)))

