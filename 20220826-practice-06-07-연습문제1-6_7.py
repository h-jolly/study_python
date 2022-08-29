list_info = (100, 121, 120, 130, 140, 120, 122, 123, 190, 125)
cnt = 0
prev_num = list_info[0]

for i in list_info:
    if (prev_num > i):
        cnt += 1
    prev_num = i

print('일일 매출 기록:', list_info)
print('지난 10일 동안 전일대비 매출이 감소한 날은 {}일입니다.'.format(cnt))
