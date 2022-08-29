# factoial

n = int(input('수를 입력하세요. :'))
fac = 1
for i in range(1, n + 1) :
    fac *= i

print('{}! = {}'.format(n, fac))
