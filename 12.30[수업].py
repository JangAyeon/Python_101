#!/usr/bin/env python
# coding: utf-8

# In[1]:


print(5+2)
print(5-2)
print(5*2)
print(5/2)
print(5//2)
print(5%2)
print(5**2)


# In[3]:


x=5;y=2
print("x:",x,"y:",y)
x+=y
print("x:",x,"y:",y)
x-=y
print("x:",x,"y:",y)
x*=y
print("x:",x,"y:",y)
x/=y
print("x:",x,"y:",y)


# In[4]:


x=10;y=2
print("x:",x,"y:",y)
x//=y
print("x:",x,"y:",y)
x%=y
print("x:",x,"y:",y)
x**=y
print("x:",x,"y:",y)


# In[8]:


x=25
y=2
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)
print(x!=y)
print(x==y)


# In[11]:


A=True
B=False
print(A and B)
print(A or B)
print(not A)
print(not B)


# In[18]:


X=12 #1100
Y=10 #1010

print(X&Y) #1000
print(X|Y) #1110
print(X^Y) #0110
print(~X) #0011 -> 2의 보수 뒤에서 설명함
print(~Y) #0101

print(X<<2) #110000
print(Y>>2) #10

