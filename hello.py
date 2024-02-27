a=[4,8,8,8,6,4]
k=2
n=len(a)
dic={}
if n%k:
	print('No')
else:
	
	for i in a:
						if i not in dic:
							dic[i]=0
						dic[i]+=1
	f=1
	for i in dic:
						if dic[i]>k:
							f=0
							break
	if f:
						print('Yes')
	else:
						print('No')