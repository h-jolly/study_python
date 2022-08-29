#21
nums = int(input('생년월일(6자리) : '))

#22
import datetime

date = datetime.datetime.now()

print('date', date)

y, m, d = date.year, date.month, date.day

print('y :', y)
print('m :', m)
print('d :', d)

print()

print('현재 시간은 {}년 {}월 {}일입니다.'.format(y, m, d))
print('지금 태어난 아이의 주민등록번호 앞자리는 : {}{}{}'.format(str(y)[2:], str(m).zfill(2), d))
