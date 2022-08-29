s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']

min_t = s_list[0]
min_cnt = len(min_t)

max_t = s_list[0]
max_cnt = len(min_t)

for i in range(len(s_list)):
    
    nex_cnt = len(s_list[i])
    
    if(min_cnt > nex_cnt):
        min_t = s_list[i]
        min_cnt = nex_cnt
    
    if(max_cnt < nex_cnt):
        max_t = s_list[i]
        max_cnt = nex_cnt

print('1) 가장 길이가 짧은 문자열 :', min_t)
print('2) 가장 길이가 긴 문자열 :', max_t)
