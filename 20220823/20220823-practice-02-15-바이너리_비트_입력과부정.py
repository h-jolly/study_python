input_num = int(input('정수를 입력하시오 :'))

print(str(input_num) + '의 2진수 값 : ' + str(bin(input_num)))
print(str(input_num) + '의 2진수 값에 대한 비트단위부정 값 : ' + str(bin(~input_num)))
