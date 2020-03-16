class MyClass:              #class 선언
    var ='안녕하세요'
    def sayHello(self):     #클래스내에 메서드(함수와 같다)
        print(self.var)     # 매서드 내에 인자 self는 인스턴스 객체를 나타낸다.

obj=MyClass()               # 클래스에 대한 인스턴스(객체)를 만든다.
print(obj.var)
obj.sayHello()

# 출처: 장삼용.2017.초보자를 위한 파이썬 200제