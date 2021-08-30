'''
#And_01
list=[]
for i in range(10):
    list.append(input())

print(type(list),len(list))
list[2]="Changed"
print(list)
list.append("New Data")
print(list)
list.remove('Changed')
print(list)

print("2nd Last element: "+list[-2])


print(list[2:6])

print(list[:6])

print(list[5:])

print(list[-8:-4])

print(list[2:-4])
'''

'''
list=list((0,1,2,3,4,5,6,7,8,9))
print(list)
list[1]="Changed"
print(list)
list[:3]=['new','new','new']
print(list)
list[:3]=['new1','new2']
print(list)
list[:3]=['new1','new2','new3','new4']
print(list)
list.insert(3,"Recent")
print(list)
list.remove("Recent")
print(list)
list.pop(-1)
print(list)
list.pop(-2)
print(list)
del list[5]
print(list)
list.clear()
print(list)
del list
'''

''''
list=list((0,1,2,3,4,5,6,7,8,9))
print(list)

for i in range(len(list)):
     print(list[i])


list=[]

for i in range(10):
     list.append(int(input()))

print(list)

new_list=[]
for i in list:
     if i%2==0:
          new_list.append(i)

print(new_list)
new_list.clear()

new_list=[i for i in list if i%2==0]
print(new_list)
new_list.clear()

for i in list:
     if i%2==0:
          new_list.append(i)
     else:
          new_list.append(0)

print(new_list)
new_list.clear()

new_list=[i if i%2==0 else 0 for i in list]
print(new_list)
'''
