
f=open('/Users/siddharth/Desktop/IR-Project-master/newdata.dat')

lines = f.readlines()
line2= set(lines)
# for lines in f:
print len(lines)
print len(line2)
f2=open('/Users/siddharth/Desktop/IR-Project-master/newdata2.dat','w')
for line in line2:
	f2.write(line)