#!/usr/bin/env python
# coding: utf-8

# 1970078 장아연 201230 실습

# In[1]:


#1번

temp=float(input())
temp=temp*1.8+32
print(temp)


# In[11]:


#2번 - case 1


X=int(input())
Y=int(input())

print("X:",X,"Y",Y)

print('X>Y:',X>Y)
print('X<Y:',X<Y)
print('X>=Y:',X>=Y)
print('X<=Y:',X<=Y)
print('X!=Y:',X!=Y)
print('X==Y:',X==Y)


# In[10]:


#2번 - case 2
X=int(input())
Y=int(input())

print("X:",X,"Y",Y)

print('X>Y:',X>Y)
print('X<Y:',X<Y)
print('X>=Y:',X>=Y)
print('X<=Y:',X<=Y)
print('X!=Y:',X!=Y)
print('X==Y:',X==Y)


# In[9]:


#2번 - case 3
X=int(input())
Y=int(input())

print("X:",X,"Y",Y)

print('X>Y:',X>Y)
print('X<Y:',X<Y)
print('X>=Y:',X>=Y)
print('X<=Y:',X<=Y)
print('X!=Y:',X!=Y)
print('X==Y:',X==Y)


# In[15]:


#3번 

X=True
Y=True
print("X:",X,"Y",Y)
print('X and Y:',X and Y)
print("X or Y:",X or Y)
print('not X:',not X)
print("\n")
X=True
Y=False
print("X:",X,"Y",Y)
print('X and Y:',X and Y)
print("X or Y:",X or Y)
print('not X:',not X)
print("\n")
X=False
Y=True
print("X:",X,"Y",Y)
print('X and Y:',X and Y)
print("X or Y:",X or Y)
print('not X:',not X)
print("\n")
X=False
Y=False
print("X:",X,"Y",Y)
print('X and Y:',X and Y)
print("X or Y:",X or Y)
print('not X:',not X)
print("\n")


# In[20]:


#4번 - case 1

X=12 #1100
Y=3 #0011

print("X:",X,"Y:",Y)
print('X&Y:',X&Y) #0000
print('X|Y:',X|Y) #1111
print('X^Y:',X^Y) #1111
print('~X:',~X) #0011


# In[22]:


#4번 - case 2

X=10 #1010
Y=10 #1010

print("X:",X,"Y:",Y)
print('X&Y:',X&Y) #1010
print('X|Y:',X|Y) #1010
print('X^Y:',X^Y) #0000
print('~X:',~X) #0101


# In[24]:


#4번

X=10 #1010
Y=3 #0011

print("X:",X,"Y:",Y)
print('X<<Y:',X<<Y) #1010 -> 1010000 : 원래 숫자에 000 추가됨
print('X>>Y:',X>>Y) #1010 -> 1 : 원래 숫자에 010 삭제됨

