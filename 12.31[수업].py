#!/usr/bin/env python
# coding: utf-8

# **type():변수 또는 값의 자료형 확인 가능**

# In[2]:


#값으로 자료형 확인

print("10 자료형: ", type(10))
print("3.14 자료형: ", type(3.14))
print("2+3j 자료형: ", type(2+3j))
print("'abc' 자료형: ", type('abc'))


# In[6]:


#변수로 자료형 확인

a=10;b=3.14;c=2+3j;d='abc'
print("a 자료형: ", type(a))
print("b 자료형: ", type(b))
print("c 자료형: ", type(c))
print("d 자료형: ", type(d))


# **진수 출력**<br><br>
# 10진수->2진수 bin(값)<BR>
# 10진수->8진수 oct(값)<br>
# 10진수->16진수 hex(값)<br>
# 
# 주의:출력 결과는 문자열 형태 

# In[45]:


print('127의 이진수: ',bin(127))
print('127의 8진수: ',oct(127))
print('127의 16진수:',hex(127))


# **~ 연산**<br>
# <br>
# 값 앞에 부호 비트 (0:양수,1:음수) 있음 <BR>
# ~X의 값: -X-1

# In[46]:


a=-4
print('4의 ~연산: ',~a)
a=0x1
print('0x1의 ~연산: ',~a)


# **문자열**<br>
# "" 또는 '' 이용<BR><br>
# **이스케이프 문자**<br>
# \n : 줄 바꿈, \t : 탭, \0 : NULL문자<BR>
# \\\ : 문자 \\, \$ : 문자 $ , \' : 문자 ' , \" : 문자 "

# In[21]:


print("ABC")
print("\"ABC\"")
print("ABC\nDEF")
print("ABC\tDEF")
print('''ABC
DEF''')

print('ABCDEF')


# **문자열 연산**<br><br>
# +:문자열 연결<br>
# 문자열 상수는 +기호 생략 가능<BR><br>
# *:문자열 반복<BR>
#    

# In[23]:


#문자열 상수
print("ABC"+"DEF")
print("ABC"*5)
print("ABC" "DEF") #문자열 상수 + 연산자 생략 가능


# In[26]:


#문자열 변수
str1="Hello"
str2="Python"
print(str1+str2)
print(str1*3)


# In[28]:


#문자열 변수는 + 연산자 생략 불가능
print(str str2)


# **인덱싱**<br>
# :문자열에서 해당 위치의 문자 선택<br><br>
# 왼쪽에서 0부터 1씩 증가<br>
# 오른쪽에서 -1부터 -1씩 증가<br>

# In[44]:


str="Hello, Python!"
print('str[0]:',str[0])
print('str[6]:',str[6])
print('str[13]:',str[13])
print('str[-2]:',str[-2])
print('str[-9]:',str[-9])


# In[34]:


#인덱스 범위 벗어나면 오류 발생
print(str[14])
print(str[-15])


# **슬라이싱**<br><br>
# 변수[시작(이상) : 끝(미만)]<br>
# 건너뛰기 : 변수[::간격]

# In[47]:


str="Hello, Python!"

print("str[7:9]",str[7:9]) # 7이상 9미만의 글자 가져오기
print("str[-7:-5]",str[-7:-5]) #음수 인덱싱도 가능 : -7이상 -5미만 : -7,-6 해당 값


# In[48]:


#시작 위치 끝 위치 생략 가능

print("str[7:]",str[7:]) # 7이상 모든 문자
print("str[:]",str[:]) # 모든 문자


# In[40]:


#건너 뛰기 가능 
str[::3] # 간격이 3으로 0 3 6 9 12 인덱스 가져옴


# **리스트
# :순서가 있는 값 나열**<br><br>
# 변수=[값,값,값, ... ]<br>
# 여러 데이터 형식으로 하나의 리스트 생성 가능<br>
# 추가,제어,수정 가능

# In[51]:


list1=[1,2,3,4,5] #정수 리스트
print("list1: ",list1)
list2=['a','b','c'] #문자 리스트
print("list2: ",list2)
list3=[3.14,'a','b','Hello',123] #복합 리스트
print("list3: ",list3)
list4=[1,2,3,'a','b','c',[0.1,0.2,0.3],list3] #복합 리스트 (리스트 안에 리스트 가능)
print("list4: ",list4)


# **리스트 인덱싱/슬라이싱**

# In[53]:


list1=[1,2,3,4,5] #정수 리스트
print("list1: ",list1)
print('list1[0]: ',list1[0])
print('list1[2]: ',list1[2])
print('list1[4]: ',list1[4])


# In[65]:


list4=[1,2,3,'a','b','c',[0.1,0.2,0.3],list3] #복합 리스트 (리스트 안에 리스트 가능)
print("list4: ",list4)
print("list4[0]: ",list4[0])
print("list4[5]: ",list4[5])
print("list4[6]: ",list4[6])
print("list4[7]: ",list4[7])

print("list4[6][0]: ",list4[6][0])
print("list4[6][2]: ",list4[6][2])

print("list4[-1]: ",list4[-1])
print("list4[-1][-1]: ",list4[-1][-1])
print("list4[-2]: ",list4[-2])
print("list4[-2][-2]: ",list4[-2][-2])


# **리스트 연산**<br>

# In[67]:


list1=[0,1,2]
list2=['a','b','c']
print("list1: ",list1)
print("list2: ",list2)

print("list1 + list2 : ",list1+list2)
print("list1 * 3 : ",list1*3)


# **리스트 관련 함수**<br><br>
# 추가 함수: 변수.append(값)<br>
# 삽입 함수: 변수.insert(위치,값)<br>
# 확장 함수: 변수.extend(리스트) : 리스트에 여러 개의 값 추가<br>
# 위치 함수: 변수.index(값,시작위치(optimal),끝위치(optimal)) : 리스트에 있는 특정 요소의 위치 확인<br>
# 요소 갯수 함수: 변수.count(값) : 리스트에 존재하는 특정 요소 갯수<br>
# 요소 꺼내기 함수: 변수.pop(꺼내려는 요소 위치(optimal))<br>
# 요소 제거 함수: 변수.remove(값)<br>
# 정렬 함수: 변수.sort(정렬방식(optimal))<br>
# 반전 함수: 변수.reverse() : 리스트를 역순으로 뒤집음<br>
# 

# In[98]:


list1=[1,2,3]
list1.append(4)
print("list1.append(4): ",list1)
list1.insert(2,2.5)
print("list1.insert(2,2.5): ",list1)
list1.extend([5,6,7,2])
print("list1.extend([5,6,7]): ",list1)
list1.index(3)
print("list1 속 3의 index값: ",list1.index(3))


# In[84]:


list1.index(3,4,6) #에러: 찾고자 하는 위치 안에 숫자 3이 없음


# In[89]:


print("값이 2인 요소의 갯수: ",list1.count(2))
print("값이 3인 요소의 갯수: ",list1.count(3))


# In[99]:


print("list1.pop(): ",list1.pop()) #가장 끝에 있는 2가 빠져나오고 그 값을 반환해줌
print("list1: ",list1)

print("list1.pop(2): ",list1.pop(2)) #빠져나올 값의 위치를 지정하여 그 위치의 값이 빠져나오고 그 값을 반환해줌
print("list1: ",list1)

print("list1.remove(5): ",list1.remove(5)) #제거할 값을 입력하여 제거하고 반환값 없음
print("list1: ",list1)


# In[102]:


list1.append(5)
print("list1.append(5): ",list1) #가장 뒤에 넣어줌

list1.sort()
print("list1.sort(): ",list1) #오름차순 정렬

list1.reverse()
print("list1.reverse(): ",list1) #역순으로 정렬 (오름차순으로 정렬- > 역순으로 정렬 = 내림차순)


# **튜플**<br><br>
# 변수=(값,값,값, ...)<br>
# 리스트와 달리 추가,제거,수정 불가<br>
# 요소가 한 개인 경우 뒤에 , 필수 : (1,)

# In[107]:


tuple1=(1,2,3,5)
tuple2=(1,) #요소가 한 개인 경우 뒤에 , 필수
tuple3=('a','b','c')
tuple4=10,20
tuple5=(1,2,3,('a','b'))
print("tuple1: ",tuple1)
print("tuple2: ",tuple2)
print("tuple3: ",tuple3)
print("tuple4: ",tuple4)
print("tuple5: ",tuple5)


# **튜플 연산**<br><br>
# +연산 : 연결<br>
# *연산 : 반복<br>

# In[108]:


tuple1=(1,2,3)
tuple2=('a','b','c')
print("tuple1+tuple2: ",tuple1+tuple2)
print("tuple2*3: ",tuple2*3)


# **문자열 서식 지정**<br><BR>
# (1)tuple 이용<br>

# In[113]:


print("제 이름은 %s이고, 나이는 %d살 입니다."%("이화인",22))


# **부울**<br><br>
# 참:True<br>
# 거짓:False<br>
# 논리 연산/비교 연산에 사용<br>
