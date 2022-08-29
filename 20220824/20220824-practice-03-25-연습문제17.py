# 연습문제 21
tmp = int(input('숫자를 입력하세요. : '))

num = 0
for i in range(2, tmp) :
    if tmp % i == 0 :
        num = 1
        break
    
if tmp % i == 0 :
    print('소수입니다.')
else :
    print('소수가 아닙니다.')

''' 이 방법 말고도, 먼저 2로 나눈후 홀수로 해서 찾는 방법해도 괜춤!
왜냐하면 2부터 하나씩 돌리면 시간복잡도 문제 발생!
    '''
