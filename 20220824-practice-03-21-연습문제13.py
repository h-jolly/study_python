# 연습문제 15
print(' ------ 연습문제 15 ------ ')
# for문
print(' --- for 문 --- ')
for i in range(1, 10) :
    print('{} * {} = {}'.format(2, i, 2*i))

# while 문
print(' --- while 문 --- ')
i = 1
while i < 10 :
    print('{} * {} = {}'.format(2, i, 2*i))
    i = i + 1

# 연습문제 16
print(' ------ 연습문제 16 ------ ')
tmp = int(input('1에서 9까지의 수를 입력하세요 : '))

while tmp < 1 or tmp > 9 :
    tmp = int(input('1에서 9까지의 수를 다시 입력하세요 : '))

for i in range(1, 10) :
    print('{} * {} = {}'.format(tmp, i, tmp*i))

