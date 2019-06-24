# -*- coding: utf-8 -*- # 이 코드는 파이썬 파일의 맨 위에 입력합니다.

"""
Spyder Editor

This is a temporary script file.
"""

#%%
# 변수에 값 할당
a = 12
b = 20

print(a, b) 
print(a+b)

#%%
# id(): 객체의 주소값 조회 

print(id(a))

#%%
# 변수 삭제
del a

print(a)
 
#%%
# 도움말 기능

help(print)

#%%
# input() : 데이터를 입력받기 위한 함수
# int() : 인수를 숫자 타입으로 변경

read_message = input("prompt_message")
first_number = input('첫 번째 숫자:')
second_number = input('두 번째 숫자:')

print(int(first_number) + int(second_number))

#%%
# print() : 화면 출력 함수
# end 속성은 데이터 출력 후 마지막에 포함될 문자를 지정

print("Hello", "World")
print("Hello", "World", sep=",")
print("Hello", end="\t")
print("World")

#%%
# type(): 자료형을 확인하는 함수
i = 10

type(i)

#%%
# 파이썬은 단일문자와 문자열을 구분하지 않는다. 
# 문자열은 겹따옴표("")와 또는 홑따옴표('')로 묶어서 사용합니다.

name = "JinKyoung"
address = '서울시 강남구'

print(name, address)

text = '''
여러 줄의 문자열을 
작성시 사용 
'''

print(text)

text2 = '''\ 
줄 바꿈도 그대로 적용해서 
여러 줄의 문자를 작성할 수 있다.
\ '''

print(text2)

text3 = '\\n을 이용하면 \n줄 바꿈을 \n적용 시킬 수 있다.'

print(text3)

text4 = "Hello \n" + "World"

print(text4)

#%%
# 문자열 인덱싱

str_ = 'Python'

str_[0:6]


#%%
# raw 문자열: 문자열 앞에 r을 붙이면 역슬래시 문자를 해석하지 않고 남겨둔다.
import re

data = "이름:홍길동, 주소:서울시, 전화번호:010-1234-4567, 특징:동해,서해"
phone_pattern = r'[\n]{3,4}=[\d]{4}-[\d]{4}'
phone = re.findall(phone_pattern, data)
print(phone)

#%%
# encode(): 인코딩 변경 함수

type('가'.encode('utf-8'))
type('가'.encode('euc-kr'))

#%%
# 논리형

g = True
print(type(g))
#%%
# False

if 0:
    print(True)
else:
    print(False)

#%%
# 포맷팅

name="홍길동"
age=20
print(name, '님의 나이는 ', age, '세입니다.', sep='')

print('{}님의 나이는 {}입니다.'.format(name, age))

#%%
# 순서 지정
a, b, c = 10, 20, 30

print('출력 : {}, {}, {}'.format(a,b,c))
print('출력 : {0}, {1}, {2}'.format(a,b,c))
print('출력 : {2}, {1}, {0}'.format(a,b,c))

#%%
# 순자 출력
# ‘d’는 10진수 정수, ‘f’는 실수(부동소수점), ‘o’(8진수, octal), ‘x’(16진수, hexadecimal)을 의미합니다. ‘f’는 소수점 이하 6자리까지만 출력
d = 12345
e = 12345.123456789

print('출력: [{}], [{:10}], [{:3}]'.format(d, d, d))
print('출력: [{:d}], [{:f}], [{:b}], [{:o}], [{:x}]'.format(d, d, d, d, d))
print('출력: [{}], [{:f}], [{:15f}], [{:10.2f}], [{:20.10f}]'.format(e, e, e, e, e))

#%%
# 문자열 출력
f = 'Hello World'

print('출력: [{}], [{:s}], [{:20}], [{:5}]'.format(f,f,f,f))
print('출력: [{}], [{:5}], [{:10.5s}]'.format(f,f,f))

#%%
# 정렬방법 지정

print('출력: [{:>5d}], [{:<5d}], [{:^5d}]'.format(a,b,c))
print('출력: [{:>10d}], [{:<10d}], [{:^10d}]'.format(a,b,c))

#%%
# 공백 대체 문자

a = 10
b = 'Hello'
c = 123
d = -123

print("출력: {:$>10}, {:*<20}, {:_<10.5s}".format(a,b,b))

# 음수의 경우엔 맨 앞에 -가 표시되며, 부호 표시도 전체 자릿수에 포함됩니다.
print("출력: [{:05}], [{:05}]".format(c,d))

# + 를 붙이면 양수의 경우 숫자 앞에 + 부호를 붙여줌
print("출력: [{:5}], [{:+5}], [{:+05}]".format(c,c,c))

# '='를 붙이면 전체 자릿수만 큼 출력하는 문자열의 맨 앞에 부호를 표시해줍니다.
print("출력: [{:=10}], [{:=+10}], [{:=+010}]".format(c,c,c))
print("출력: [{:=10}], [{:=+10}], [{:=+010}]".format(d,d,d))

# '='는 채울 문자와 같이 사용할 수 있습니다.
print("출력: [{:*=10}], [{:*=+010}], [{:*>+010}]".format(c,c,c))
print("출력: [{:*=10}], [{:*=+010}], [{:*>+010}]".format(d,d,d))

#%%
# 날짜 출력
from datetime import datetime
print('{:%Y-%m-%d %H:%M}'.format(datetime(2001, 2, 3, 4, 5)))

#%%
# 파라미터를 갖는 format
a = 2.7182818284

print("출력: [{:{}{}.{}}]".format(a, '>',10, 3))
print("출력: [{:{}{sign}{}.{}}]".format(a, '>',10, 3,sign='+'))

#%%
# 논리 연산자
a = False

if not a:
    print(True)
    
#%%
# 비교 연산자
score = 80

if(score> 60):
    print("합격")
else:
    print("불합격")
    
#%%
# instanceof  

isinstance(10, int)

#%%
# String

temp = 'python is easy'
temp

print(temp)

# 문자열 길이 반환
len(temp)

temp[0:6]
temp.split()

#%%

temp2 = ['python', 'java', 'R','SAS']

# 배열의 문자열들을 연결
','.join(temp2)

# 소문자 변환(첫글자 대문자)
temp.capitalize()

# 소문자 변환
temp.lower()

# 대문자 변환
temp.upper()

#%%
# find, index : 특정 문자 위치 검색

temp.find('t')

#%%
# 문자열 타입 확인

temp.isnumeric()
temp.isalpha()

#%%
# 문자열 대체

temp.replace("python", "nice")

#%%
# 문자열을 다룰 수 있는 함수들 목록 출력

dir(str)

#%%
# 날짜 다루기
from datetime import date

today = date(2015,11,26)
today2 = date.today()

print(today2.year)
print(today2.month)
print(today2.day)
print(today2)

#%%
# 시간을 지정하거나 알 수 있음
from datetime import time

t = time(7)

print(t)

t2 = time(8, 14, 20, 3000)

print(t2)

t3 = time(hour = 3,second = 12)

print(t3)

#%%
# 날짜와 시간을 지정하거나 알 수 있음

from datetime import datetime, date, time

dt = datetime.now()

print(dt)

dt2 = datetime(2019, 11, 26, 16, 24, 15)

print(dt2)

dt3 = datetime.utcnow()

print(dt3)

d = date(2019, 12, 25)
t = time(15, 20, 15)
dt4 = datetime.combine(d, t)

print(dt4)

