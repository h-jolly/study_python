#19와 20
def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2) # F_n = F_(n-1) + F_(n-2)

nterms = int(input('몇 개의 피보나치 수를 구할까요? : '))

# 음수인 경우 피보나치 구할 수 없음.

for i in range(nterms+1):
    fibo = fibonacci(i)
    print('fibo({}) = {}'.format(i, fibo))
    if(nterms == i):
        print('--- fibo({}) = {}'.format(i, fibo))

