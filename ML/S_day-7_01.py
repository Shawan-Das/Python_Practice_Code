import statistics

def StandardDivition(L,mean):
    t_sum=sum((i-mean)**2 for i in L)
    return (t_sum/len(L))**0.5

n= int(input())
X= list(map(float, input().strip().split(" ")))
Y= list(map(float, input().strip().split(" ")))

x_mean= statistics.mean(X) #mean of X
y_mean= statistics.mean(Y) #mean of Y

part1= sum((X[i]-x_mean)*(Y[i]-y_mean) for i in range(n))
part2= part1/(n*StandardDivition(X,x_mean)*StandardDivition(Y,y_mean))
print(round(part2,3))


#Equation:
# PCC= (sum(xi-x_meam)(yi-y_mean))/n*SD_x*SD_y
#SD -> Standard Divition