# 22번
flag = True

while(flag):
    tmp_num = int(input('n을 입력해주세요.(1~10 사이) : '))
    if(0 < tmp_num and tmp_num < 11):
        flag = False

total = tmp_num ** 2
total_list = list(range(1, total+1))

result = None

if(tmp_num == 1):
    result = [1]
else:
    result = [][]

'''
result[0] = [1, 2, 3, 4, 5]
result[1] = [6, 7, 8, 9, 10]
result[2] = [11, 12, 13, 14, 15]
result[3] = [16, 17, 18, 19, 20]
result[4] = [21, 22, 23, 24, 25]
'''
print('total_list >>>', result)

#[[for i in range(11)] for row in range(10)]
