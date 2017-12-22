c = 0
sushu = 1
for i in range (101,200):
	for j in range(2,i):
		if i % j == 0:
			sushu = 0
			break
	if sushu == 1:
		c += 1
		print i
	sushu  = 1
print "total is %d" % c

