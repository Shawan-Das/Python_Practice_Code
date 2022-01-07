# -*- coding: utf-8 -*-
"""Practice.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x4H5Muujq7RzBWa-JY08k5QT1sq9Gu2n

#Condition

##Problem 1

1. Take a 4 digit number as year (example 2021) from user.
2. Check if the input year is leap year or not. [Use nested if]
3. Write the same program using multiple conditions [ do not use nested if]
4. Write the same program in 2 using short hand if statement
"""

year = int(input())
if year%4 == 0:
  if year %100 == 0:
    if year%400 ==0:
      print("leap year")
    else:
      print("not leap year")
  else:
    print("leap year")
else: 
  print("not leap year")

year = int(input())

if year% 400 ==0 or (year%100 !=0 and year%4 ==0):
  print("leap year")
else:
  print("not leap year")

year = int(input())
# if year%4 == 0:
#   if year %100 == 0:
#     if year%400 ==0:
#       print("leap year")
#     else:
#       print("not leap year")
#   else:
#     print("leap year")
# else: 
#   print("not leap year")

#[[print("leap year") if year% 400 == 0 else print("not leap year")] if year %100 == 0 else print("leap year")] if year%4 == 0 else print("not leap year")
print("leap year") if year% 400 == 0 else print("not leap year") if year %100 == 0 else print("leap year") if year%4 == 0 else print("not leap year")

"""##Problem 2

1. Take 3 integer number as user input
2. Draw a flow chart to find the second maximun number from these 3 numbers. [do not use any multi-condition]
3. Write a program to find out the second maximun number from these 3 numbers
4. Write the same program in 3 using short hand if statement [optional]
"""

a = int(input())
b = int(input())
c = int(input())

if a>b:
  if a>c:
    if b>c:
      print(b)
    else:
      print(c)
  else:
    print(a)
else:
  if b>c:
    if a>c:
      print(a)
    else:
      print(c)
  else:
    print(b)

a = int(input())
b = int(input())
c = int(input())

# if a>b:
#   if a>c:
#     if b>c:
#       print(b)
#     else:
#       print(c)
#   else:
#     print(a)
# else:
#   if b>c:
#     if a>c:
#       print(a)
#     else:
#       print(c)
#   else:
#     print(b)

#[[print(b) if b>c else print(c)] if a>c else print(a)] if a>b  else [[print(a) if a>c else print(c)] if b>c else print(b)]
print(b) if b>c else print(c) if a>c else print(a) if a>b  else print(a) if a>c else print(c) if b>c else print(b)

"""#Looping

##Problem 1
"""

1. Take an integer n as user input
2. Write a program to print the following figure.

input: 4
output:
*
**
***
****
***
**
*

n = int(input())

for i in range(1,n+1):
  for j in range(1,i+1):
    print("*", end = "")
  print()
for i in range(n-1,0,-1):
  for j in range(1,i+1):
    print("*", end = "")
  print()

"""##Problem 2

1. Take an integer n from user.
2. Print the first n fibonaaci numbers [Use for loop]
3. Do the same task using while loop
"""

0   1    1    2   3   5 
a   b 
   a=b  b=a+b

n = int(input())

a = 0
b = 1
for i in range(n):
  print(a)
  temp =a+b
  a = b
  b =temp

"""##Problem 3

1. Take an integer number n from user [ where 10<=n<=20.
2.  Write a while loop iterate from 1 to n and break the program after n=5.

3. Write a program to print 1 to n except 5.
"""

n = int(input())

i = 1

while i<=n:
  print(i)
  if i==5:
    break
  i = i+1

n = int(input())

i = 1

while i<=n:
  if i==5:
    i = i+1
    continue
  print(i)
  i = i+1

"""#Function

##Problem 1

1. Write a function which can take arbitrary number of integer and return the sum of all the integer.
"""

def sum_all_number(*numbers):
  sum = 0
  for i in range(len(numbers)):
    sum = sum+numbers[i]

  return sum

print(sum_all_number(1,2,3))
print(sum_all_number(1,2,3,4))

"""##Problem 2

1 . Write a program which can take arbitrary number of keyword arguments.  Example: 
1. func1(first_name = "abdur", last_name = "rashid",roll = 50)
2. func1(first_name = "abdur", last_name = "rashid",roll = 50,cgpa =3.81)
"""

def func1(**student):
  for key in student.keys():
    print(key, " : ",student[key])

func1(first_name = "abdur", last_name = "rashid",roll = 50)
print()
func1(first_name = "abdur", last_name = "rashid",roll = 50,cgpa =3.81)

"""##Problem 3

1. Write a program which can take 3 integers as user input and return the summation and muliplication of these integers.
"""

def func1(a,b,c):
  return a+b+c,a*b*c

a =int(input())
b =int(input())
c =int(input())

sum , multi = func1(a,b,c)
print(sum)
print(multi)

"""## Problem 4

1. Write a recursive function to find the value of nCr.
"""

# nCr = (n-1)Cr + (n-1)C(r-1)
def ncr(n,r):
  if r ==0:
    return 1
  if n==r:
    return 1
  return ncr(n-1, r)+ncr(n-1, r-1)

n =int(input())
r =int(input())
if n>=r:
  print(ncr(n,r))
else:
  print("wrong input")

"""#Lambda function

##Problem 1

1. Write a Lambda function which can take 3 numbers as input and return the summation of these 3 numbers.
"""

sum  = lambda a,b,c: a+b+c
print(sum(1,2,3))