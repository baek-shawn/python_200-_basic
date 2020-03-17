url='http://www.naver.com/news/today'
log='name:shawn age:20 sex:남자'

ret1=url.split('/')
print(ret1)

ret2=log.split()
for data in ret2:
    d1,d2=data.split(':')
    print('%s->%s'%(d1,d2))