def fen(n=10):
	o = 0
	for i in range(2,n):
		if  n % i == 0:
			o = 1
			break
		else:
			o = 0
	if o == 1:
		print i,"*",
		return fen(n/i)
	else:
		print n
		return n

n = 999
print "%d =" % n,
fen(n)
