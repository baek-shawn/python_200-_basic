b1 = bin(97)        # bin은 2진수로 변환하여 문자열로 값을 리
b2 = bin(98)
ret1 = b1 +b2
print(ret1)
a = int(b1,2)       # b1과 b2는 문자열이기 때문에 정수형으로 변환 후 계
b = int(b2,2)
ret2 = a+b
print(bin(ret2))

# 출처: 장삼용.2017.초보자를 위한 파이썬 200제