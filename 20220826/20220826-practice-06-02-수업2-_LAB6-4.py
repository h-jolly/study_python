# LAB 6-4 : 딕셔너리의 항목 추가와 삭제
fruits_dic = {'apple': 6000, 'melon': 3000, 'banana': 5000, 'orange': 7000}

print('keys = ', fruits_dic.keys())
print('values = ', fruits_dic.values())
fruits_dic.pop('apple')
print('keys = ', fruits_dic)
fruits_dic.clear()
print('keys = ', fruits_dic)
