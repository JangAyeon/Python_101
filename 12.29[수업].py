#!/usr/bin/env python
# coding: utf-8

# In[10]:


x=5
X=10
print("x:",x)
print("X:",X)

#x와 X는 각각 다른 값을 보여줌 -> 같은 변수가 아님


# In[7]:


word_count=6
_Max=10
print("word_count:",word_count)
print("_Max:",_Max)

#밑줄 문자 변수에 사용 가능


# In[9]:


space2020='space2020'
print("space2020:",space2020)

#변수명에서 숫자가 맨 앞에 등장하는 것 아니면 사용가능
#변수에 문자열도 대입 가능 -> 숫자 문자에 따른 형식을 따로 지정할 필요없음


# In[14]:


no-way!=100
no-way

# !는 변수 이름으로 사용 불가한 특수 문자


# In[15]:


2nd=10
2nd
#변수 이름 숫자로 시작할 수 없음


# In[19]:


a b c="abc"
a b c
#변수 이름에 공백 사용 불가


# In[20]:


True="real"
True
#예약어 변수 이름으로 사용 불가 (이미 다른 용도로 사용되고 있기 때문)


# 

# In[22]:


#Syntax error (구문 오류): 코드, 문법적인 규칙 안 지켜서 생긴 오류
#Semantic error (의미 오류): 구문 자체는 오류 없지만 현재 못 하는 일을 시켰을 때
    3+abc #NameError: name 'abc' is not defined
    5/0 #ZeroDivisionError: division by zero


# #변수 생성
# ->형식 제한/선언 없이 변수에 값을 할당하여 새 변수 생성
# -> = 는 동등의 의미가 아니라 대입연산자 , 할당한다는 의미
# -> 변수이름 = 값

# In[24]:


Korean = 90
English = 80
Math = 85

Math


# In[ ]:


sum = Korean + English + Math
sum


# #값,변수,메모리
#  ->메모리:컴퓨터 장치 중 정보를 저장하기 위한 장치 
#  ->주소를 이용해서 값을 구분
#  
#  #값은 메모리 주소를 가지게 되고 변수는 그 메모리 주소가 할당됨 따라서 변수는 값을 참조함

# In[ ]:


x=10
sum=x
name="이화인"


# #할당문
#  -> 변수 = 표현식
#  -> (1) 표현식의 값을 먼저 계산함 (2)계산된 최종 값을 메모리에 저장함 (3) 그 값을 가지는 메모리 주소를 변수에 저장
#  -> 새로운 변수면 생성하고 기존에 있던 변수면 메모리 주소를 변경해줌

# In[26]:


variable=3+5
variable
#variable은 8이 저장된 주소를 가지고 있다가 값을 쓸 때 주소를 가지고 찾아가서 값을 출력함


# #변수에 재할당
# -> 변수 x를 이용해 다른 변수 y에 값을 할당하더라도 원래 변수 x의 값 변경이 다른 변수 y에 영향을 미치지 않음

# In[28]:


x=10
y=2*x
print("x:",x,"y:",y)
x=5
print("x:",x,"y:",y)


# In[29]:


z=10
print("z:",z)
z=z+z
print("z:",z)

