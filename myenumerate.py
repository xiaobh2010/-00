#自己实现enumerate函数	
#程序如下：
def myenumerate(iter1,start=0):
    it=iter(iter1)
    while True:
        try:
            x=next(it)
            yield (start,x)
            start+=1
        except StopIteration:
            break

for i in myenumerate([1,3,5]):
    print(i)
