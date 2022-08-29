# LAB 6-2 : 딕셔너리의 항목 추가와 삭제
person = {'이름': '홍길동', '나이': 26, '몸무게': 82, '특기': '분신술'}
print('person = ', person)

person['아버지'] = '홍판서'
print('person = ', person)

del(person['나이'])
print('person = ', person)
