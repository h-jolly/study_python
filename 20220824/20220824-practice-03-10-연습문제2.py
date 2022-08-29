# 연습문제 2
name = input('이름을 입력해주세요. ')
age = int(input('나이를 입력해주세요(단위 cm). '))
tmp = '없'
if age >= 140 :
    tmp = '있'
print(name, '님은 놀이기수를 탈 수', tmp, '습니다.')
