#1970078 장아연


def display_list(): #연락처 목록 출력 함수
  with open("contact.txt",'r') as file: 
    print("이름 전화번호")
    for line in file:
        print(line,end="") #연락처 목록에서 한 줄씩 받아서 읽어서 출력

def rewrite(lines): #연락처를 새롭게 갱신하는 함수
    with open("contact.txt",'w') as file:
      for num in lines:
        file.write(str(num))
      file.close()
        
def sort_list(): #연락처 목록 이름 순서들로 정렬하는 함수
    file=open("contact.txt",'r')
    lines=file.readlines() #연락처 목록을 한 줄씩 리스트로 받기
    file.close()
    lines.sort() #리스트 정렬을 통해 이름 순서대로 정렬
    rewrite(lines) #새롭게 정렬한 순서대로 연락처 갱신
 


  

def add_list(): #연락처에 새로운 이름과 전화번호 추가 함수
    name=input("연락처에 추가할 이름을 입력하세요: ") #이름 입력받기
    num=input("연락처에 추가할 전화번호를  입력하세요: ") #전화번호 입력받기
    print("\n")
    file=open("contact.txt",'a') #파일에 이어서 새로운 이름과 연락처 추가
    file.write(name+" "+num+"\n")
    file.close()

    sort_list() #연락처 이름순으로 갱신
    display_list() #화면에 출력
    print("\n")


def del_list():
  name = input('연락처에서 삭제할 이름을 입력하세요: ') #삭제할 이름 받기
  print("\n")
  with open("contact.txt",'r') as file:
    lines=file.readlines() #연락처를 파일에서 읽어오기
    for a in range(len(lines)): #연락처 전체에서 해당 이름 정보 삭제
      for i in lines:
        if name in i:
          lines.remove(i)

  rewrite(lines) #삭제 처리된 연락처 갱신
  sort_list() #이름 순으로 정렬
  display_list() #화면에 출력


def correct_list(): #이름을 받아 해당 이름의 전화번호를 수정
  name = input('수정할 이름을 입력하세요: ') #수정할 전호번호 소유자의 이름
  num = input('수정할 전화번호를  입력하세요: ') #새로운 전화번호 입력
  print("\n")
  with open("contact.txt",'r') as file:
    lines=file.readlines()
    for i in lines:
      if name in i: #리스트에서 해당 이름이 포함된 요소 찾기
        lines.remove(i) #수정 전 정보 삭제하고
        lines.append(name+" "+num+"\n") #수정된 정보로 새롭게 추가

  rewrite(lines) #수정된 연락처 갱신
  sort_list() #이름 순으로 정렬
  display_list() #화면에 출력

  


    
def contact() : # 연락처 관리 프로그램 함수
  
    file=open("contact.txt",'a+',encoding="UTF8") #연락처 파일 읽기
    #a+ 모드로 파일을 불러옴
    #해당 파일이 있으면 파일 끝에서부터 내용을 추가
    #해당 파일이 없는 경우 파일을 생성해서 데이터를 입력

    


    while True: # 키보드에서로부터 수행할 기능을 입력 받음

        print('''\n연락처 관리 프로그램]
1 : 전체 연락처  출력
2 : 새로운 연락처 추가
3 : 연락처 삭제
4 : 연락처 수정
5 : 종료''')

    
        menu = int(input('메뉴를 선택하세요[1-5]: '))
        print("\n\n")
    
        if menu == 1 : # 전체 연락처 출력
          display_list()
      
        elif menu == 2 : # 새로운 연락처 추가
          add_list()
      
        elif menu == 3 : # 연락처 삭제
          del_list()
      
        elif menu==4: #연락처 수정
          correct_list()
    
        elif menu==5: #연락처 종료
          break
    
        else :
          print('잘못 입력하셨습니다.')


contact() #연락처 관리 프로그램 실행
