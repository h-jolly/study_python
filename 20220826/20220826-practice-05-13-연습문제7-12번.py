# 12번
tmp = int(input('n(정)을 입력해주세요.'))
tmp_list_str = input('6개의 수를 입력해주세요.').split()

sum_t = 0
min_t = -1
max_t = -1

cnt = len(tmp_list_str)

for i in range(cnt):
    tmp = int(tmp_list_str[i])
    sum_t += tmp

    if(min_t == -1):
        min_t = tmp
    if(max_t == -1):
        max_t = tmp
    
    if(min_t > tmp):
        min_t = tmp
    if(max_t < tmp):
        max_t = tmp

print('합 :', sum_t)
print('평균 :', sum_t / cnt)
print('최댓값 :', max_t)
print('최솟값 :', min_t)



    
