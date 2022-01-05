import math

def erfc(m,s,x):
    a=math.erf((x-m)/(s*math.sqrt(2)))
    return 0.5*(1+a)

m,s=list(map(float,input().split(" ")))
x1=float(input())
x2=float(input())

a=(1-erfc(m,s,x1))*100
b=(1-erfc(m,s,x2))*100
c=100*erfc(m,s,x2)

print(round(a,2))
print(round(b,2))
print(round(c,2))
