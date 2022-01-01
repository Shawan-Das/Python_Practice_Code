#part of ans 4


#------------


# Ans: 1
n=int(input("Enter a positive number: "))


#Ans: 2
list=[]
for i in range(n):
    list.append(int(input()))


#Ans: 3
new_List=[]

for i in list:
    if i>0:
        new_List.append(i*i)
    else:
        new_List.append(abs(i))

print(new_List)
new_List.clear()

#Ans: 4
new_list=[i*i if i>0 else abs(i) for i in list]
print(new_list)



#Ans: 5
def fun(num):
    return num*num


sorted_List=list.copy()

sorted_List.sort(key=fun)

print(sorted_List)