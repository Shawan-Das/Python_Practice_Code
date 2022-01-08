import statistics

X=[]
Y=[]

for i in range(5):
    x,y=list(map(int,input().split(" ")))
    X.append(x)
    Y.append(y)

sxsy=sum(X)*sum(Y)

sxy=sum(x*y for x,y in zip(X,Y))
sx2=sum(i**2 for i in X)

b=((5*sxy)-(sxsy))/((5*sx2)-(sum(X)**2))
a=statistics.mean(Y)-(b*statistics.mean(X))

print(round(a+(b*80),3))

