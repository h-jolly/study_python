# 연습문제 9
num = int(input('정수를 입력해주세요. : '))
tmp2 = num % 2 == 0
tmp3 = num % 3 == 0

print(num,'는(은) 2(으)로 나뉨 여부 : ', tmp2)
print(num,'는(은) 2(으)로 나뉨 여부 : ', tmp3)
print(num,'는(은) 2와(과) 3 모두로 나뉨 여부 : ', tmp2 and tmp3)
