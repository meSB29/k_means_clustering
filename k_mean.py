import matplotlib.pyplot as plt
t=int(input())
a=[list(map(int,input().split()))for i in range(t)]
k=2
k=[list(map(int,input().split())) for i in range(2)]
l1=[]
l2=[]
for i in range(len(a)):
	if(abs(a[i][0]-k[0][0])+abs(a[i][0]-k[0][0])<abs(a[i][0]-k[1][0])+abs(a[i][0]-k[1][1])):
		l1.append(a[i])
	else:
		l2.append(a[i])
len_old1=0
len_old2=0
len_new1=len(l1)
len_new2=len(l2)
l11=[]
l12=[]
while(len_new1!=len_old1 or len_old2!=len_new2):
	for i in range(len(a)):
		if(abs(a[i][0]-k[0][0])+abs(a[i][0]-k[0][0])<abs(a[i][0]-k[1][0])+abs(a[i][0]-k[1][1])):
			l1.append(a[i])
		else:
			l2.append(a[i])
	print(l1)
	print(l2)
	if(len(l1)!=0 and len(l2)!=0):
		l11=l1
		l12=l2
	k[0]=[sum([l1[i][0] for i in range(len(l1))])//len(l1),sum([l1[i][1] for i in range(len(l1))])/len(l1)]
	k[1]=[sum([l2[i][0] for i in range(len(l2))])//len(l2),sum([l2[i][1] for i in range(len(l2))])/len(l2)]
	len_old1=len_new1
	len_old2=len_new2
	len_new1=len(l1)
	len_new2=len(l2)
	print(len_new1)
	print(len_new2)
	l1=[]
	l2=[]
print([l11[i][1] for i in range(len(l11))])
print(l12)
print(k)
plt.scatter([l11[i][0] for i in range(len(l11))],[l11[i][1] for i in range(len(l11))],color='Red')
plt.scatter([l12[i][0] for i in range(len(l12))],[l12[i][1] for i in range(len(l12))],color='Blue')
plt.scatter([k[i][0] for i in range(len(k))],[k[i][1] for i in range(len(k))],color='Green')
plt.show()
