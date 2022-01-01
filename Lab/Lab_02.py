'''
#Problem_01
y=int(input("Enter a Year: "))


if y%400==0:
    print("Leap Year")
elif y%4==0:
    if(y%100!=0):
        print("Leap Year")
    else:
        print("Not a leap year")
else:
    print("Not a Leap Year")


if (y%400==0) or (y%100!=0 and y%4==0):
    print("Leap Year")
else:
    print("Not a leap year")

print("Leap Year") if (y%400==0)or(y%4==0 and y%100!=0) else print("Not a leap year")

'''

'''

'''

'''
#Looping Problem_01
n=int(input())


for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()


for i in range(n-1,0,-1):
    for j in range(1,i+1):
       print("*",end="")
    print()
'''


'''
#problem_02

n=int(input())
d1=0
d2=1
print(d1,d2,end=" ")
for i in range(2,n):
    print(d1+d2,end=" ")
    d1,d2=d2,d1+d2
print("")

#while Loop
j=2
d1=0
d2=1
print(d1,d2,end=" ")

while(j<n):
    print(d1 + d2, end=" ")
    d1,d2=d2,d1+d2
    j+=1

'''

'''
#Problem_03
n=int(input()) 

i=1
while(i<=n):
    if i==5: break
    print(i,end=" ")
    i+=1
print(" ")

for i in range(1,n+1):
    if i==5: continue
    print(i,end=" ")

'''

'''
def sum(*number):
    sum=0
    for i in range(len(number)):
        sum+=number[i]
    return sum


print(sum(1,2,3,4))
'''

'''
def info(**person):
    for detail in person.keys():
        print(detail," :", person[detail])

info(first_name="Shan",last_name="Saha",roll=19101020)
'''

''''
sum=lambda a,b,c: a+b+c

print(sum(1,2,3))
'''
