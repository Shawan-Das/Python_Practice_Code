a,b = list(map(int,input().split(" ")))
n= int(input())
p=a/b
g=0
for i in range(1,n+1):
    g+=p*(1-p)**(n-i)
#g= sum(p*(1-p)**(n-i)) for i in range(1,n+1)
print(round(g,3))




#equation is :
#  b*(x,n,p)= (n-1 x-1).p^x . q^(n-x)  where q=1-p
#The number of success to be observed is x
#The total number of trials is n
#The probability of success 1 of trial is p.
#The probability of failure of 1 trial q, where q=1-p
#b*(x,n,p) is the negative binomial probability, meaning the probability
# of having x-1 successes after n-1 trial and having x success after n trials.
