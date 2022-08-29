#17
def sum_range(n1, n2) :
    sum = 0
    
    for i in range(n1, n2+1) :
        sum += i

    print('{}에서 {}까지의 정수의 합 : {}'.format(n1, n2, sum))

sum_range(10, 20)
sum_range(40, 100)
