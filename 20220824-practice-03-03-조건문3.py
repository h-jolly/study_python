# if-elif-else 문
speed_input = int(input('자동차의 속도를 입력하세요(단위 : km/h):'))
speed = '저속'

if speed_input >= 100:
    speed = '고속'
elif speed_input >= 60 :
    speed = '중속'

print(speed)
