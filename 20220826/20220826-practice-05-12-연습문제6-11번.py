# 11번
tmp = input('5개의 수를 입력해주세요.').split()
tmp_list = []
for i in range(len(tmp)):
    tmp_list.append(int(tmp[i]))

print('합 :', sum(tmp_list))
print('평균 :', sum(tmp_list)/len(tmp))
print('최댓값 :', max(tmp_list))
print('최솟값 :', min(tmp_list))
