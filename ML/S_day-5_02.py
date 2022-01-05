x,y= list(map(float,input().split(" ")))

x= x+ x**2
y= y+ y**2

print(round(160+(40*x),3))
print(round(128+(40*y),3))