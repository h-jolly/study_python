# 연습문제 10
a, b = input('두 정수를 입력해주세요. : ').split()
tmp = int(a) % int(b) == 0
print(a+'는(은) '+ b +'의 배수 여부 : ' + ('Y' if tmp else 'N'))
