# 공식: (화씨온도 - 32) ÷ 1.8 = 섭씨온도
def celsius(fahrenheit):
        return str((fahrenheit - 32) / 1.8)

fahrenheit = int(input('화씨온도를 입력하세요. : '))
print(섭'씨'+ str(fahrenheit) +'를 섭씨로 변환 : ' + celsius(fahrenheit))
