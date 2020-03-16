a=11113
b=23
ret=a%b                 # %는 나머지 연산자
ret1,ret2=divmod(a,b)   #divmod 내장함수를 사용하면 몫과 나머지 연산을 한다.

print('{}를 {}로 나누면 {}가 나머지로 남습니다.'.format(a,b,ret))
print('{}를 {}로 나누면 몫{} {}가 나머지로 남습니다.'.format(a,b,ret1,ret2))

# 출처: 장삼용.2017.초보자를 위한 파이썬 200제