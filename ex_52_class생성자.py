class MyClass:
    def __init__(self):             # 클래스의 인스턴스 객체가 생성될 때 자동적으로 호출되는 메소드인 클래스 생성
        self.var ='안녕하세요!'       # 인스턴스 멤
        print('MyClass 인스턴스 객체가 생성되었습니다')

obj = MyClass()
print(obj.var)

# 출처: 장삼용.2017.초보자를 위한 파이썬 200제