n= int(input())

a=[]
a.append(-1)
for i in range(1,n+1):
    a.append( int(input()) )

for i in range(1,n+1):
    if(i==1):
        print(max(a[i+1],a[n]))
    elif (i==n):
        print(max(a[1],a[i-1]))
    else:
        print(max(a[i+1],a[i-1]))

