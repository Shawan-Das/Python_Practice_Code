import math

def erfc(m,s,x):
    a=math.erf((x-m)/(s*math.sqrt(2)))
    return 0.5*(1+a)

x=int(input())
n=int(input())
m=int(input())
s=int(input())

m=n*m
s=math.sqrt(n)*s

print(round(erfc(m,s,x),4))

