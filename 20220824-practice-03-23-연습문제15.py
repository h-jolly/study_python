# 연습문제 18
print(' ------ 연습문제 18 ------ ')
print('맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.')
print('1) 햄버거')
print('2) 치킨')
print('3) 피자')

tmp = int(input('1에서 3까지의 메뉴를 선택하세요 : '))
while tmp < 1 or tmp > 3 :
    tmp = int(input('메뉴를 다시 입력해주세요 : '))

text = '피자'
if tmp == 1 :
    text = '햄버거'
elif tmp == 2 :
    text = '치킨'
print('{}을 선택하였습니다.'.format(text))

print()

# 연습문제 19
print(' ------ 연습문제 19 ------ ')
print('맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.')
print('- 햄버거(입력 b)')
print('- 치킨(입력 c)')
print('- 피자(입력 p)')

tmp = input('메뉴를 입력해주세요(알파벳 b, c, p 입력) : ')
tmp_num = 0
while tmp_num != 1 :
    if tmp == 'b' or tmp == 'c' or tmp == 'p' :
        tmp_num = 1
    else : 
        tmp = input('메뉴를 다시 입력해주세요(알파벳 b, c, p 입력) : ')

text = '피자'
if tmp == 'b' :
    text = '햄버거'
elif tmp == 'c' :
    text = '치킨'
print('{}을 선택하였습니다.'.format(text))
