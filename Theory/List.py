'''
first_name=input()
last_name=input()

full_name=f"{first_name} {last_name}"
print(full_name)
'''


# set1={1,2,3,4,5}
# set2={4,5,6,7,8,9}
#
# print(set1.symmetric_difference(set2))

# def nList(new_list):
#     print(new_list)


# list=[0,1,2,3,4,5,6,7,8,9]
#
# list.insert(1,1)
# print(list)


# list[2:4]=0,1
# print(list)
# newList=list[2:8]
# print(newList)

# for i in range(5):
#     data = input()
#     list.append(data)
#
#
# nList(" next ".join(list))


# list=[i**2 for i in range(10)]
# print(list)


# fruits=["apple","banana","cherry","kiwi","mango"]
# list=[fruit if 'a' in fruit else "orange" for fruit in fruits ]
# print(list)


# list=[]
# #list[1]=[j for j in range(3)]
# for i in range(9):
#     for j in range(i):
#         list[list[i]].append(j)
# print(list)

# list=[[0],[0,1],[0,1,2],[0,1,2,3],[0,1,2,3,4],[0,1,2,3,4,5]]
#
# print(list[4][4])


# tuples= (200,10,1,43,5,5,6)
# tuples=(250,)+tuples[1:]
# tuples=tuples+(100,)
# print(tuples)

# list=[]
#
# for i in range(1,5):
#     for j in range(1,i):
#         list[i].append(j)
#
#
# print(list)

'''
# list=[[i for i in range(5)]for j in range(5)]
# print(list)
'''


# list=[]
#
# for i in range(5):
#     lst=[]
#     for j in range(i+1):
#         lst.append(j)
#     list.append(lst)
#
#
# for i in range(5):
#     for j in range(i+1):
#         print(list[i][j],end=" ")
#     print(" ")

#fruits=("apple","banana","cherry","kiwi","mango")

'''
# name=("Shan",'marani','shit')
#
# new=fruits+name
# print(new)
'''
# (fruit1,fruit2, *new_fruits)=fruits

# print(fruit1)
# print(fruit2)
# print(new_fruits)

# for i in range(len(fruits)):
#     print(fruits[i])

# list=[1,2,3,4,5]
# sets=set(list)
# sets.add(7)
# print(sets(0))

'''
set1={1,2,3,4,5}
set2={4,5,6,7,8,9}
#
set3=set1.difference(set2)
print(set3)
set1.update(set2)
print(set1)
'''

# y=int(input("Year: "))
#
# if (y%400==0) or (y%100!=0 and y%4==0):
#     print("Leap Year")
# else:
#     print("Not a leap year")
#

# a=5
# b=6
# print("In Range") if a in range(10,21) else print("Out or range")
#
# if a<=b:
#     print("Hacked")
# else:
#     print("Access ")

# a=int(input("1st Number: "))
# b=int(input("2nd Number: "))
# c=int(input("3rd Number: "))
# d=int(input("4th Number: "))
#
# if a>b:
#     if a>c:
#         if a>d:
#             print(f"Max Value: {a}")
#         else:
#             print(f"Max Value: {d}")
#     else:
#         if c>d:
#             print(f"Max Value: {c}")
#         else:
#             print(f"Max Value: {d}")
# else:
#     if b>c:
#         if b>d:
#             print(f"Max Value: {b}")
#         else:
#             print(f"Max Value: {d}")
#     else:
#         if c>d:
#             print(f"Max Value: {c}")
#         else:
#             print(f"Max Value: {d}")



#n=int(input())
#
#
# for i in range(1,n+1):
#     for j in range(1,i):
#         print("*",end="")
#     print("")
#
#
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print("")


# for i in range(10,0,-1):
#     print(i)




# Function

# def function(name):
#     print("Hello ",name)
#
#
# for i in range(10):
#     function("Mominna")
# def func(*student):
#     print("Hello",student[3])


# def func(student):
#     print("Hello",student[3]," "+"Something")
#
#
# touple=("Mominna","Anondo","Kacchi","Pika")
# func(touple)
#func("Mominna","Anondo","Kacchi","Pika")


# def fun(x,y=1/2):
#     print(x**y)
#
# fun(2)

# def fun(list1):
#     list2=list1.copy()
#     list2[1]=2
#     return list2
#
#
# list1=[1,3,3,4,5]
#
# print(fun(list1))

# x= lambda a,b: a**b
#
# print((x(2,3))


# def f1(multiplier):
#     return lambda a: a**multiplier

# df=f1(2)
# print(df(5))
# tf=f1(3)
# print(tf(5))

'''
n=5
space=2*(n-1)
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end=" ")

    s=space
    for k in range(s,0,-1):
        print(" ",end=" ")
    space-=2

    for j in range(1,i+1):
        print("*",end=" ")

    print()
'''

'''
a=7
b=7
c=9

if a in range(b,c) or a in range(c,b): print(a)
elif b in range(a,c) or b in range(c,a): print(b)
elif c in range(a,b) or c in range(b,a): print(c)
'''


a=int(input())
b=int(input())
print(a-b)