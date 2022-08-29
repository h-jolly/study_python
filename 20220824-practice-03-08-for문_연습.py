print(' -------------------- 연습 1 -------------------- ')
selected = None
while selected not in ['가위', '바위', '보'] :
    selected = input('가위, 바위, 보 중에서 선택하세요. : ')
print('선택한 값은 : ', selected)

print()
print(' -------------------- 연습 2 -------------------- ')
n = int(input('합계를 구할 양의 정수를 입력하세요 : '))
s = 0
for i in range(1, n+1) :
    s += i
print('1부터 {}까지의 합은 {}'.format(n, s))

print()
print(' -------------------- 연습 3 -------------------- ')
n = -1
while n <= 0 :
    n = int(input('합계를 구할 양의 정수를 입력하세요 : '))
s = 0
for i in range(1, n+1) :
    s += i
print('1부터 {}까지의 합은 {}'.format(n, s))
