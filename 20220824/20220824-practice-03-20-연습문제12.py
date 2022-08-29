# 연습문제 14
tmp = input('알파벳을 입력해주세요. : ')

result = '자'

if tmp == 'a' or tmp == 'e' or tmp == 'i' or tmp == 'o' or tmp == 'u' : 
    result = '모'

print('{} 는(은) {}음입니다.'.format(tmp, result))
