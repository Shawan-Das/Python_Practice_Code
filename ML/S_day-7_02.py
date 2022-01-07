n = int(input())
X = list(map(float, input().strip().split(" ")))
Y = list(map(float, input().strip().split(" ")))

X_sort = sorted(X)
Y_sort = sorted(Y)

Rank_X =[X_sort.index(i)+1 for i in X]
Rank_Y= [Y_sort.index(i)+1 for i in Y]

d_sum=sum((Rank_X[i]-Rank_Y[i])**2 for i in range(n))


SRCC=1-((6*d_sum)/((n**3)-n))
print(round(SRCC,3))