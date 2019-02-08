while True:
	try:
		s,a,n=input("").split()
		s=int(s)
		a=int(a)
		n=int(n)
		break
	except:
		print("invalid input")
		break
if(s>n):
	if(s>n):
		print(s)
	elif(n>s):
		print(n)
elif(a>s):
	if(a>n):
		print(a)
	elif(n>a):
		print(n)
