import math

n=int(input())
m=int(input())
ss=int(input())
p=float(input())
z=float(input())

s=ss/math.sqrt(n)

A=m-(z*s)
B=m+(z*s)

print(round(A,2))
print(round(B,2))