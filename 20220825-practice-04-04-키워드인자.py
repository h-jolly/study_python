# LAB 4-9 키워드 인자
def print_name(honorifics, first_name, last_name):
    ''' 키워드 인자를 이용한 출력용 프로그램 '''
    print(honorifics, first_name, last_name)

# 호출 1
print_name(first_name = 'Gildong', last_name = 'Hong', honorifics = 'Dr.')
# 호출 2
print_name('Gildong', 'Hong', 'Dr.')
