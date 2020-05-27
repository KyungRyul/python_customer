import pickle

class viewer:
    def hello(self):
        return input('''
        다음 중에서 하실 일을 골라주세요 :
        I - 고객 정보 입력
        C - 현재 고객 정보 조회
        P - 이전 고객 정보 조회
        N - 다음 고객 정보 조회
        U - 고객 정보 수정
        D - 고객 정보 삭제
        S - 파일에서 정보 가져오기
        Q - 프로그램 종료
        ''').upper()

    def inputC(self, custlist, page):
        if page >= 0:
            print("현재 페이지는 {}쪽 입니다".format(page + 1))
            print(custlist[page])
        else:
            print("입력된 정보가 없습니다.")
        return custlist, page


    def inputP(self, custlist, page):
        if page <= 0:
            print('첫 번 째 페이지이므로 이전 페이지 이동이 불가합니다')
            print(page)
        else:
            page -= 1
            print("현재 페이지는 {}쪽 입니다".format(page + 1))
            print(custlist[page])
        return custlist, page


    def inputN(self, custlist, page):
        if page >= len(custlist)-1:
            print('마지막 페이지이므로 다음 페이지 이동이 불가합니다')
            print(page)
        else:
            page += 1
            print("현재 페이지는 {}쪽 입니다".format(page + 1))
            print(custlist[page])
        return custlist, page
    def search(self):
        fname = input('파일이름을 입력하시오.')
        with open(fname, 'rb') as f:
            data = pickle.load(f)
            print(data)
