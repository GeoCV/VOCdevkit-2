f = open('train.txt', 'w')
for i in range (601):
	s=str(i)
	s=s.zfill(4)
	f.write(s+'\n')

