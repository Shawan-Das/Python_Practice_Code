# -*- coding: utf-8 -*-
"""Practice Problem.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10Zz23aEgJl2vj6HJ1NPvMQr2J0PSPDMQ

#Problem 1

1. Define an empty list
2. Append 10 element into the list by taking as user inputs [ Hints: use a for loop]
3. Find out the datatype and length of the list 
4. Show that the list is changable by writing update, add, remove operation on the list
5. Access the 2nd last element using the negative index
6. Create a new list by slicing the existing list from index 2 to 5(including)
7. Create a new list by slicing the existing list from index 0 to 5(including)
8. Create a new list by slicing the existing list from index 5 to end of the list
9. Do the same task in 6 no question using negative index
10. Do the same task in 6 no question using both positive and negative index
"""

#1. Define an empty list
list1 = []

#2. Append 10 elements into the list by taking as user inputs [ Hints: use a for loop]
for i in range(10):
  list1.append(input())
print(list1)

# list1 = [input() for i in range(10)]

#3. Find out the datatype and length of the list
print(type(list1))
print(len(list1))

#4. Show that the list is changable by writing update, add, remove operation on the list
list1[0] = 10
print(list1)

list1.append(20)
print(list1)

list1.pop(1)
print(list1)

#5. Access the 2nd last element using the negative index
print(list1[-2])

#6. Create a new list by slicing the existing list from index 2 to 5(including)
print(list1[2:6])

#7. Create a new list by slicing the existing list from index 0 to 5(including)
print(list1[:6])

#8 Create a new list by slicing the existing list from index 5 to end of the list
print(list1[5:])

#Do the same task in 6 no question using negative index
print(list1[-8:-4])
#Do the same task in 6 no question using both positive and negative index
print(list1[2:-4])

"""#Problem 2

1. Create a list of 10 elements using list constructor 
2. Replace the element in index 1 with a new value
3. Replace first 3 elements with 3 new values [Hints: use slicing]
4. Replace first 3 elements with 2 new values
5. Replace first 3 elements with 4 new values
6. Insert a new element in index 3 using insert function 
7. Remove an element from the list using remove function
8. Remove the last element from the list
9. Remove the second last element from the list
10.Remove the element at index 5 using del 
11.Clear the list 
12.Delete the list permanently from the program
"""

#Create a list of 10 elements using list constructor
list1 = list((1,2,3,4,5,6,7,8,9,10))
#Replace the element in index 1 with a new value
list1[1] =20
#Replace first 3 elements with 3 new values [Hints: use slicing]
list[:3] = [30,40,50]
#Replace first 3 elements with 2 new values
list[:3] = [30,40]
#Replace first 3 elements with 4 new values
list[:3] = [30,40,50,60]
#Insert a new element in index 3 using insert function
list1.insert(3,100)
#Remove an element from the list using remove function
list1.remove(100)
#Remove the last element from the list
list1.pop()
#Remove the second last element from the list
list1.pop(-2)
#Remove the element at index 5 using del
del list1[5]
#Clear the list
list1.clear()
#Delete the list permanently from the program
del list1

"""#Problem 3

1. Create a list of 10 elements using list constructor
2. Print all items by referring to their index number [Hints use a for loop]
3. Define an empty list
4. Append 10 Random Values (Integer Type) into the list by taking as user inputs [ Hints: use a for loop]
5. Create a new list from the existing list by taking only the even number
6. Do the same task in question 5 using List comprehension 
7. Create a new list from the existing list by taking even number directly and replacing odd number as 0
8. Do the same task in question 7 using List comprehension
"""

#Create a list of 10 elements using list constructor
list1 = list((1,2,3,4,5,6,7,8,9,10))
#Print all items by referring to their index number [Hints use a for loop]
n =len(list1)
for i in range(n):
  print(list1[i])
#Define an empty list
list1 = []
#Append 10 Random Values (Integer Type) into the list by taking as user inputs [ Hints: use a for loop]
for i in range(10):
  list1.append(int(input()))

#Create a new list from the existing list by taking only the even number
new_list =[]
for num in list1:
  if num%2 == 0:
    new_list.append(num)
#Do the same task in question 5 using List comprehension
new_list = [num for num in list1 if num%2 == 0]
#Create a new list from the existing list by taking even number directly and replacing odd number as 0
new_list =[]
for num in list1:
  if num%2 == 0:
    new_list.append(num)
  else:
    new_list.append(0)
#Do the same task in question 7 using List comprehension
new_list = [num if num%2 == 0 else 0 for num in list1 ]

"""#Problem 4

1. Create an emply list
2. Append 10 Random positive and negative integer into the list by taking as user inputs
3. Sort the list
4. Sort in reverse order
5. Sort the list using the absolute value of each integer
[Hints: Using custom function]
"""

#Create an emply list
list1 = []
#Append 10 Random positive and negative integer into the list by taking as user inputs
for i in range(10):
  list1.append(int(input()))
#Sort the list
list1.sort()
#Sort in reverse order
list1.sort(reverse = True)
#Sort the list using the absolute value of each integer [Hints: Using custom function]
def func(num):
  return abs(num)
list1.sort(key = func)

abs(-2)