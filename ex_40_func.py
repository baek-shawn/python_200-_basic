# 함수인자
def add_txt(t1,t2='파이썬'):   # 인자에 기본값을 지정 할 수 있다.
    print(t1+':'+t2)

add_txt('베스트')              # 함수를 호출 시 값이 차례로 대입된다.
add_txt(t2='대한민국',t1='1등')  # 키워드 인자의 순서를 바꿀 수 있다.

def func1(*args):             # 인자의 개수가 불명확한 경우 가변인자를 사용한다.
    print(args)               # 가변인자는 앞에 인자이름 앞에 *를 붙이고 함수내부는 튜플로 처리된다.

def func2(width,height,**kwargs):   # 키워드 인자가 불명확한 경우 **kwargs와 같은 인자를 사용
    print(kwargs)                   # 함수 내부에서는 딕셔너리로 사

func1()
func1(3,5,1,5)
func2(10,20)
func2(10,20,depth=50,color='blue')

# 출처: 장삼용.2017.초보자를 위한 파이썬 200제