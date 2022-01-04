# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def fact(x,n,p):
    s1= (p**x)*((1-p)**(n-x))

    return (math.factorial(n)/((math.factorial(x))*math.factorial(n-x)))*s1



p,n= list(map(int,input().split(" ")))

p=p/100
sum1=0
for i in range(3):
    sum1+=fact(i,n,p)
print(round(sum1,3))

sum2=0
for i in range(2,n+1):
    sum2+=fact(i,n,p)
print(round(sum2,3))


#equation is :
#  b(x,n,p)= (n p).p^x . q^(n-x)  where q=1-p
#The number of success x
#The total number of trials is n
#The probability of success 1 of trial is p.
#The probability of failure of 1 trial q, where q=1-p
#b(x,n,p) is the binomial probability, meaning the probability of having exactly x successes out of n trial
