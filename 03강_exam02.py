# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 21:06:29 2019

@author: mark146
"""

#%%
# 메모리 주소값 확인
i = 3
j = 3
k = 4 - 1
id(i)
id(j)
id(k)

#%%
# 메모리 주소값 확인_2
i = 3000000000000
j = 3000000000000
id(i)
id(j)
f = 0.0
g = 0.0
id(f)

#%%
# 함수 정의 문법
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

help(convert_to_celsius)

convert_to_celsius(212)

#%%

def quadratic(a, b, c, x):
    first = a * x ** 2
    second = b * x
    third = c
    return first + second + third

quadratic(2, 3, 4, 0.5)
quadratic(2, 3, 4, 1.5)

#%%

def days_difference(day1: int, day2: int) -> int:
    """
    day1과 day2 간 날짜 수 차이를 반환한다.
    이때 day1과 day2는 (그 해의 몇 번째 날인지 가리키는)
    1에서 365 사이의 값이다.    
    """
    return day2 - day1
