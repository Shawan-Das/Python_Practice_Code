import math
def fact(x,n,p):
    s1= (p**x)*((1-p)**(n-x))

    return (math.factorial(n)/((math.factorial(x))*math.factorial(n-x)))*s1



a,b= list(map(float,input().split(" ")))

p= round(a/b,3)
p=p/(p+1)
ans=0
n=6 #total 6 trials

for i in range(3,7):
    ans+=fact(i,n,p)

print(round(ans,3))


#equation is :
#  b(x,n,p)= (n p).p^x . q^(n-x)  where q=1-p
#The number of success x
#The total number of trials is n
#The probability of success 1 of trial is p.
#The probability of failure of 1 trial q, where q=1-p
#b(x,n,p) is the binomial probability, meaning the probability of having exactly x successes out of n trial
