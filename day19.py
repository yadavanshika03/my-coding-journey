for i in range(12):
	if(i==10):
		break
	print("5 X",i+1,"=",5*(i+1))
print("loop ko chodkar bhago")

for i in range(12):
	if(i==10):
		continue
	print("5 X",i+1,"=",5*(i+1))
print("skip the iteration")

i=1
while True:
	print(i)
	i=i+1
	if(i%101==0):
		break


	

	