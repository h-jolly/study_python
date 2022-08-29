# 연습문제 3
age = int(input('나이를 입력해주세요. '))
height = int(input('키를 입력해주세요(단위 cm). '))
tmp = '없'

if age >= 19 and height >= 150 :
    tmp = '있'
print('입장할 수 '+ tmp +'습니다.')

