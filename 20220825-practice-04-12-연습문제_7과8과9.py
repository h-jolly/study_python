def mean_n(nums) :
    sum = 0
    cnt = len(nums)
    for i in nums :
        num = int(i)
        sum += num
    
    print('평균값은', sum / cnt)

def max_n(nums) :
    max = int(nums[0])
    for i in nums :
        n_tmp = int(i)
        if max < n_tmp :
            max = n_tmp
            
    print('최댓값은', max)


def min_n(nums) :
    min = int(nums[0])
    for i in nums :
        n_tmp = int(i)
        if min > n_tmp :
            min = n_tmp
            
    print('최솟값은', min)
    

input_list = input('여러 수를 입력해주세요.(구분 띄어쓰기) : ').split()

mean_n(input_list)
max_n(input_list)
min_n(input_list)

print()

input_list = input('여러 수를 입력해주세요.(구분 띄어쓰기) : ').split()

mean_n(input_list)
max_n(input_list)
min_n(input_list)
