# LAB 4-10 : 가변 인자의 활용
# 1번 문제
def sum_nums(*nums) :
    sum = 0
    length = len(nums)
    for i in nums :
        sum += i
    print('{}개의 인자 {}'.format(length, nums))
    print('합계 : {}, 평균 : {}'.format(sum, sum / length))

sum_nums(10, 20, 30)
sum_nums(10, 20, 30, 40, 50)

print()

# 2번 문제
def min_nums(*nums) :
    min = nums[0]
    
    for i in nums :
        if(i < min) :
            min = i
    print('최솟값은 {}'.format(min))

min_nums(20, 40, 50, 10)
