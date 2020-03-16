h1 = hex(97)
h2 = hex(98)
ret1 = h1 + h2
print(ret1)         # ret1은 문자열과 문자열을 더한것이기 때문에 문자열의 합
a = int(h1,16)
b = int(h2,16)
ret2 = a+b          # 16진수의 합을 구하려면 int를 이용해 숫자로 변환 후 계산
print(hex(ret2))

# 출처: 장삼용.2017.초보자를 위한 파이썬 200제