# 연습문제 20
tmp = int(input('숫자를 입력하세요. : '))

for i in range(1, tmp+1) :
    print(' '*(tmp-i) + '*'*i)
