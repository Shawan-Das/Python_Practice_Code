import math


def erfc(m,s,x):
    a=math.erf((x-m)/(s*math.sqrt(2)))
    return 0.5*(1+a)


m,s=list(map(float,input().split(" ")))
x=float(input())
x1,x2=list(map(float,input().split(" ")))

print(round(erfc(m,s,x),3))
print(round(erfc(m,s,x2)-erfc(m,s,x1),3))
