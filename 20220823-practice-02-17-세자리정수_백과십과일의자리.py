num = int(input('세 자리 정수를 입력하세요. : '))

print('백의 자리 : ', num // 100)
print('십의 자리 : ', (num // 10) % 10)
print('일의 자리 : ', num % 10)

print('   ')

print('일의 자리 : ', num % 10)
print('십의 자리 : ', (num // 10) % 10)
print('백의 자리 : ', num // 100)



# 선생님 풀이
num = int(input('세 자리 정수를 입력하세요 : '))

print('백의 자리 : ', num // 100)

num = num - (num//100) * 100

print('십의 자리 : ', num // 10)
print('일의 자리 : ', num % 10)


num2 = int(input('세 자리 정수를 입력하세요 : '))
print('백의 자리 : ', num % 10)
num2 = num // 10
print('십의 자리 : ', num % 10)
num2 = num // 10
print('일의 자리 : ', num % 10)

