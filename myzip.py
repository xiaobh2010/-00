#定义myzip函数实现zip函数功能：
def myzip(iter1,iter2):
	it1=iter(iter1)
	it2=iter(iter2)
	while True:
		try:
			x=next(it1)
			t=next(it2)
			yield (x,y)
		except StopIteration:
			break
