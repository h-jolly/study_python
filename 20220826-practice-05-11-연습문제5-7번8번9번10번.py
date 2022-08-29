n_list = [10, 20, 30, 50, 60]

sum_t = 0
mult_t = 1
max_t = n_list[0]
min_t = n_list[0]
for i in range(len(n_list)):
    tmp = n_list[i]
    
    sum_t += tmp
    mult_t *= tmp
    if(tmp > max_t):
        max_t = tmp
    if(tmp < max_t):
        min_t = tmp
    
print('리스트 원소들 :', n_list)

print()

# 7번
print('리스트 원소들의 합 :', sum_t)

# 8번
print('리스트 원소들의 곱 :', mult_t)

# 9번
print('리스트 원소들 중 최댓값 :', max_t)

# 10번
print('리스트 원소들 중 최솟값 :', min_t)
