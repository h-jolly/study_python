# 3-8 : 누적 덧셈의 응용

sum1 = 0
sum2 = 0
sum3 = 0

for i in range(1, 101) :
    sum1 += i
    if i % 2 == 0 :
        sum2 += i
    else : 
        sum3 += i

print('1부터 100 전체 합 :', sum1)
print('1부터 100 짝수 합 :', sum2)
print('1부터 100 홀수 합 :', sum3)
