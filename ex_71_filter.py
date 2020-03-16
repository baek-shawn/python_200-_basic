# filter를 이용해서 특정 조건을 만족하는 값을 추출
def getPrime(x):            # 소수만 추출하는 함수
    if x%2 ==0:
        return

    for i in range(3,int(x/2),2):
        if x % i == 0:
            break
    else:
        return x

listdata = [117,119,1113,11113,11119]
ret = filter(getPrime,listdata)
print(list(ret))

# 출처: 장삼용.2017.초보자를 위한 파이썬 200제