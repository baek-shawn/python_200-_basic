# 지역변수와 전역변수
param = 10
strdata = '전역변수'    # 전역변수는 코드 전체에 유효한 변수이.

def funcl():
    strdata ='지역변수' # 지역변수는 함수 내에서만 유효한 변수이다.
    print(strdata)

def func2(param):
    param = 1

def func3():
    global param
    param = 50

funcl()                # 지역변수 출력
print(strdata)         # 전역변수 출력
print(param)           # 전역변수 param 출력
func2(param)
print(param)
func3()
print(param)

# 출처: 장삼용.2017.초보자를 위한 파이썬 200제