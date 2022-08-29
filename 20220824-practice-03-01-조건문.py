# if else 문
print('if else 문 - 게임 고수 확인')
game_input = int(input('게임 점수를 입력하시오 : '))

if(game_input >= 1000):
    print('고수입니다.')
else:
    print('입문자입니다.')

print('')

print('if else 문 - 값 같은지 확인')
num1_input = int(input('한 정수를 입력하시오 : '))
num2_input = int(input('다른 정수를 입력하시오 : '))
if(num1_input == num2_input):
    print('두 값이 일치합니다.')
else: 
    print('두 값이 일치하지 않습니다.')
