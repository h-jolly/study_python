# 13번
tmp_list_str = input('10개의 수를 입력해주세요.').split()
cnt = len(tmp_list_str)

sum_t = 0

for i in range(cnt):
    tmp = int(tmp_list_str[i])
    sum_t += tmp

print('합 :', sum_t)
print('평균 :', sum_t / cnt)
print('표준 편차 :', (sum_t / cnt) / cnt)


# 45 67 20 34 2 100 23 45 67 89
