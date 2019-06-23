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
