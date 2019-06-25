# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 19:44:13 2019

@author: mark146
"""

#%%
# 리스트 생성
fruits = ["banana", "apple", "orange", "grape"]

# 리스트의 항목의 수를 반환
len(fruits)

print(fruits)

numbers_2d = [[1,2,3,4,5], [10,20,30,40,50],[1,3,5,7,9],[2,4,6,8,10]]

print(numbers_2d)

#%%
# len() : 길이(항목의 수)
numbers = [1,2,3,4,5]
numbers_2d = [[1,2,3,4,5], [10,20,30,40,50],[1,3,5,7,9],[2,4,6,8,10]]

len(numbers)

#%%

# min(), max() : 최댓값, 최솟값
min(numbers)

# 2차원 리스트에선 부분 리스트 중에서 첫 항목이 가장 큰 값을 갖는 리스트를 반환
max(numbers_2d)

# + 에 의한 연결
print(numbers + numbers)

# * 곱한 수만큼 반복
print(3*numbers)

#%%

# append() : 리스트의 맨 뒤에 새로운 항목 추가
numbers.append(10)
print(numbers)

numbers.append([20,30,40,50])
numbers

# extend(): 리스트로 항목 추가
numbers2 = [1,2,3,4,5]
numbers2.extend([10,20,30,40,50])
numbers2

# extend() : 사용시 문자열을 이용하면 문자열이 리스트로 바뀌고 문자 하나씩 리스트에 추가
numbers2 = [1,2,3,4,5]
numbers2.extend('hello')
numbers2

# insert(index, data): index 위치에 data 항목 삽입
numbers2.insert(5,100)
numbers2

#%%
# 인덱싱

# count() : 리스트에서 데이터의 개수를 센다.
numbers2 = [1,3,5,7,9,1,2,3,4,5]
numbers2.count(1)

# index() : 해당 항목의 위치를 반환
numbers2.index(5)

numbers2.index(5,3)

#%%
# 슬라이싱
numbers = [1,2,3,4,5]
numbers_2d = [[1,2,3,4,5], [10,20,30,40,50],[1,3,5,7,9],[2,4,6,8,10]]

numbers[2:4]
numbers[2:]
numbers[:4]
numbers[:]

#%%
numbers[::2]

# step이 음수면 역순으로 출력
numbers[::-1]

#%%
# 데이터 수정
numbers = [1,3,5,7,9,1,2,3,4,5]

numbers[0:5] = [2,4,6,8,10]
numbers

#%%
# step을 이용해 일정 구간마다 항목을 변경
numbers[::2] = [10,20,30,40,50]
numbers

#%%
# 데이터 삭제

# pop() : 맨 뒤의 항목을 반환하고 해당 데이터를 삭제
numbers.pop()
print(numbers)

# 2차원 리스트에서의 pop()은 맨 마지막 리스트를 삭제
numbers_2d.pop()
print(numbers_2d)

#%%
# remove() : 해당 항목 삭제

numbers.remove(4)
print(numbers)

# 2차원 리스트에서 부분 리스트를 삭제하려면 삭제할 리스트를 추가
numbers_2d.remove([1,2,3,4,5])
print(numbers_2d)

#%%
# del() : 리스트의 특정 항목을 삭제할 때 사용
numbers = [1,2,3,4,5,6,7,8,9,10]
del numbers[3]
print(numbers)

# 슬라이싱을 이용한 삭제
numbers = [1,2,3,4,5,6,7,8,9,10]
del numbers[3:8]
print(numbers)

numbers = [1,2,3,4,5,6,7,8,9,10]
del numbers[::2]
print(numbers)

# 변수 삭제
del numbers

#%%
# clear() : 리스트의 모든 항목 삭제

numbers = [1,2,3,4,5,6,7,8,9,10]
numbers.clear()
print(numbers)

#%%
# 정렬

# sort() : 리스트 정렬, 기본 오름차순
numbers = [10,4,3,6,7,9,5,1,8,2]
numbers.sort()
print(numbers)

# reverse 속성을 사용시 내림차순
numbers.sort(reverse=True)
print(numbers)

# reverse() : 리스트를 역순으로 변경
numbers.reverse()
print(numbers)

# [from_index : to_index : step] 에서 step이 음수면 역순으로 출력할 수 있다.
print(numbers[::-1])

#%%
# 리스트 복제

numbers = [10,4,3,6,7,9,5,1,8,2]
new_numbers = numbers.copy()
print(numbers)
print(new_numbers)

#%%
# = : 주소를 복사해 같은 객체 참조
numbers = [10,4,3,6,7,9,5,1,8,2]
new_numbers = numbers
print(numbers)
print(new_numbers)

