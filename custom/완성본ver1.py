import re
import defList as func

custlist=[]
page=-1

def choiceInput():
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    ''').upper()
    return choice

while True:
    choice = choiceInput()
    if choice=="I":
        custlist, page = func.inputI(custlist, page)
    elif choice=="C":
        custlist, page = func.inputC(custlist, page)
    elif choice == 'P':
        custlist, page = func.inputP(custlist, page)
    elif choice == 'N':
        custlist, page = func.inputN(custlist, page)
    elif choice=='D':
        custlist, page = func.inputD(custlist, page)
    elif choice=="U": 
        custlist, page = func.inputU(custlist, page)
    elif choice=="S":
        func.search()    
    elif choice=="Q":
        func.write(custlist)
        break
