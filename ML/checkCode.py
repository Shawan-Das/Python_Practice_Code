import math
def nCr(x):
    ans= math.factorial(35)/(math.factorial(x)*math.factorial(35-x))
    return ans*(0.1**x)*((0.9)**(35-x))

s=0
for i in range(11):
   print(round(nCr(i),4))
   s+=nCr(i)

print(round(s,4))
print(round(1-s,4))

