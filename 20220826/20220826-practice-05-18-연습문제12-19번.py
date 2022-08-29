# 19번
s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
new_s_list = []

for i in range(len(s_list)):
    tmp = s_list[i]
    
    if tmp not in new_s_list:
        new_s_list.append(tmp)

print('정보 >', new_s_list)
