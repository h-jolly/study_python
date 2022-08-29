# 14
input_tmp = input('세 수를 입력해주세요.(구분 띄어쓰기) : ').split()

def sort_tmp(tmp) :
    tmp_list = []
    for i in tmp :
        tmp_list.append(int(i))
        
    print('오름차순으로 정렬된 리스트 정보 :', sorted(tmp_list))

sort_tmp(input_tmp)

print()

# 15
def sort_tmp2(*tmp) :
    print('tmp :', sorted(tmp))

sort_tmp2(45, 3, 4, 56, 5)
sort_tmp2(9, 8, 7, 6, 5, 4, 3)

print()

# 16
def print_num(nums) :
    tmp_nums = []
    for i in nums :
        tmp_nums.append(int(i))

    print('입력된 정수 리스트:', tmp_nums)
    print('정렬된 정수의 리스트:', sorted(tmp_nums))
    
    
input_tmp = input('쉼표로 구분된 정수를 여러 개 입력해주세요. : ').split(',')

print_num(input_tmp)
