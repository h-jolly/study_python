# 연습문제 11
lotto = input('세 복권번호를 입력해주세요. : ').split()

success_num = 0
for tmp in lotto :
    int_tmp = int(tmp)
    if int_tmp == 2 or int_tmp == 3 or int_tmp == 9 :
        success_num += 1

success_txt = '다음 기회에...'
if success_num > 2 :
    success_txt = '로또 당첨!!'
elif success_num > 1 :
    success_txt = '상금 1천만원'
elif success_num > 0 :
    success_txt = '상금 1만원'

print('당첨 여부 : ',success_txt)
