#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1970078 장아연

#실습 1번

name=input()
birth_mon=int(input()) #문자열->정수
birth_day=int(input()) #문자열->정수
print("나의 이름은 %s이고, 생일은 %d월 %d일 입니다."%(name,birth_mon,birth_day))


# In[6]:


#실습 2번

베릴륨=4
마그네슘=12
스트론튬=38
바륨=56
라듐=88

alkaline_earth_metal=[베릴륨,마그네슘,스트론튬,바륨,라듐]
print("라듐의 원자번호의 인덱스: ",alkaline_earth_metal.index(라듐))

칼슘=20
alkaline_earth_metal.append(칼슘)
print("칼슘 추가 후 alkaline_earth_metal: ",alkaline_earth_metal)

alkaline_earth_metal.sort()
print("원자번호에 맞게 정렬: ",alkaline_earth_metal)

