class Add:
    def add(self,n1,n2):
        return n1+n2

class Calculator(Add):              # 클래스의 상속
    def sub(self,n1,n2):
        return n1-n2

obj = Calculator()
print(obj.add(1,2))
print(obj.sub(1,2))

# 출처: 장삼용.2017.초보자를 위한 파이썬 200제