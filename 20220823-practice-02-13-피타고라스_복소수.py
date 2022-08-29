# 피타고라스
print('피타고라스 정리')

a = int(input('밑변을 입력하시오 : '))
b = int(input('높이을 입력하시오 : '))

c = (a**2 + b**2) ** 0.5

print('빗면의 값 : ', c)


---------------------------------------------------------

# 복소

# Complex number

print('1번')

position = 1 + 2j
print('회전하기 전 : ', position)

rotation = 0 + 1j
position = position + rotation
print('회전 후 : ', position)

print('2번')

position = 1 + 2j
print('회전하기 전 : ', position)

rotation = (3**0.5)/2+0.5j
position = position + rotation
print('회전 후 : ', position)
