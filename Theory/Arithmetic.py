# x=42
# y=41
# z= x!=y

# age=21
# print(age<18 and age<28)

# a= input('1st Number: ')
# b= input('2nd NUmber: ')
# if a>b:
#   print("a is greater than b")
#  print("if part")
# elif a==b:
#   print("a is equals to b")
#  print("elif part")
# else:
#   print("b is greater than a")
#  print("else part")
# print("\nend line")#

# str1= input('Main String: ')
# str2= input('Sub-String: ')
# message= "String fount in "+ str(str1.count(str2))+" places"
# print(str1.endswith('mind'))

# a,sign,b= input('Numbers: ')

# if sign=='+':  print(a+b)
# elif sign=='-':print(a-b)
# elif sign =='*':print(a*b)
# elif sign=='/': print(a/b)
# elif sign=='//':print(a//b)
# elif sign=='%': print(a%b)


# str=input("Enter the string: ")
# print(len(str))
# print(str.count('A'or'a'or'E'or'e'or'I'or'i'or'o'or'O'or'u'or'U'))

# msg="Hello I'm Shan"
# print('Shan'in msg)
# month= ["Jan","Feb","Mar","Apr","May","June","July","Aug","Sep","Oct","Nov","Dec",13]
# print(month[0]/2)

# number="019101020"
# new= int(number)
# print(new)

# sets=["Anannya","Zarin","Vabna","Tanmoy","Nashra","Prachi"]
# new_set=set(sets)
# print(new_set)
# new_set.add("Shawan")
# print(new_set)
# new_set.pop()
# print(new_set)

# alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# alp=set(alpha)
# print(alp)

# dict={'Anannya':19101001,'Zarin':19101003,'Vabna':19101011,
#     'Tanmoy':19101013,'Nashra':19101018,'Kacchi':19101044}
# dict['Shawan']=[1,9,1,0,1,0,2,0]
# print(dict['Anannya'])
# print(19101020 in dict)


#x = int(input('Number: '))
#if (x%2==0):
 #   print(" is Even Number")
#else:
 #   print(" is Odd Number")

#dict={'Anannya':19101001,'Zarin':19101003,'Vabna':19101011,
 #    'Tanmoy':19101013,'Nashra':19101018,'Kacchi':19101044}
#n=int(input("Total Student: "))
#dict={}
#for i in range(n):
 #   name=input("Student Name: ")
  #  dict[name]=input("Student ID: ")

#for name in dict:
 #   print("Student Name: {}   Student ID: {}".format(name,dict[name]))

#usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

#for name in range(len(usernames)):
 #   usernames[name]= usernames[name].lower().replace(" ","_")

#print(usernames)

#for i in range(0,-5):
 #   print(i)


#book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
#counter={ }

#for books in book_title:
    #counter[books]= counter.get(books,0)+1 ///extra & easy
    #if books not in counter:
     #   counter[books]=1;
    #else:
     #   counter[books]+=1;

#print(counter)


#dict={'Anannya':19101001,'Zarin':19101003,'Vabna':19101011,
 #    'Tanmoy':19101013,'Nashra':19101018,'Kacchi':19101044,'Shawan':19101020}

#for name,id in dict.items():
#   print(str(name)+'    '+str(id))

#name=["Anannya","Zarin","Vabna","Tanmoy","Nashra","Kacchi","Shawan","Tanha"]
#id=["19101001","19101003","19101011","19101013",'19101018','19101044','19101020','19101036']

#list=[]
#list=(zip(name,id))

#print(list)
#number=[i**2 if i%2==0 else i+3 for i in range(10)]
#print(number)
#names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
#for name in names:
 #   str=name.split()
  #  print(str)

#t=int(input("Test Case: "))

#for i in range (t):
#    n=int(input('Range: '))
#    counter=0
#    for j in range(1,10):
#        k=j
#        while(k<=n):
#            #print(k)
#            counter += 1
#            k=(k*10)+j
#    print(counter)

#n= int(input("Number of Rows: "))
#count=0
#for i in range(n):
#    for j in range(i+1):
#        print(count," ",end="")
#       count+=1
#    print("\r")

#def TOH(disk,A,B,C):
#    if disk==1:
#        print("Move Disk 1 From {} to {}".format(A,C))
#    else:
#        TOH(disk-1,A,C,B)
#        print("Move Disk {} From {} to {}".format(disk,A,C))
#        TOH(disk-1,B,A,C)

#number=int(input("Number of Disk: "))

#TOH(number,'A','B','C')
"""
word='hello'
def some_function():
    #word='bye'
    print(word)
some_function()
"""
'''
list1=[]
list=[]
with open('newFile','r') as f:
    for i in f:
        id=i.split(',')[0]
        list1.append(id)
print(list1)
for i in range(len(list1[0].split(','))):
    list.append(int(list1[0].split(',')[i]))

print(list)
#print(len(list[0].split(',')))
'''

"""
file=open('newFile','r')
file_data=file.read()
file.close()
"""
'''''
dict={'Anannya':19101001,'Zarin':19101003,'Vabna':19101011,'Tanmoy':19101013,'Nashra':19101018,'Kacchi':19101044,'Shawan':19101020,'Tanha':19101036}

file=open('newFile','w')
file.write(str(dict))
file.close()
#'''
'''''
dict={}
f=open('newFile','r')
file=f.read()
f.close()
list=[]
file=str(file).replace('{','').replace('}','').replace('\'',''.replace(" ",""))
for i in range(len(file.split(','))):
    list.append(file.split(',')[i])

for i in range(len(list)):
    name = list[i].split(':')[0].replace(' ','')
    id = list[i].split(':')[1]
    dict[name] = int(id)


for name in dict:
    print('{} - {}'.format(name,dict[name]))
#print(dict)
#print(file[0])
'''
'''
for i in range(len(file)):
    name=file[i].split(':')[0]
    id=file[i].split(':')[1]
    dict[name]=int(id)

print(dict)
'''
''''
list=[]
file='newFile'
with open(file,'r') as f:
    for data in f:
        info=data.strip().split(',').remove('{')
        print(info)
'''

'''''
class person():
    def __init__(self,name,id):
        self.name=name
        self.id=id

info=[]
#n=int(input('Total Student: '))

while(True):
    name=input('Name: ')
    id=input('ID: ')
    p=person(name,id)
    info.append(p)
'''

# u=float(input("Value of u in m/s : "))
# a=float(input("Value of a in m/s2: "))
# # ans of a
# t=float(input("Total Time in sec: "))
# v= u+a*t
# print("Velocity of the car: {}".format(v))
# # ands of b
# s=(u+v)*t/2
# print("distance covered by the car: {}".format(s))

'''''
name = input("Full Name: ")
print("Number of occurrence 'a': {}".format(name.count('a')))
new_name=name
print("Replaced 'a' with 'u': {}".format(new_name.replace('a','u')))
print("First Occurrence of 'a': {}".format(name.find('a')))
print(f"first 3 cha: {name[:3]}")
print(f"2nd last char of last name: {name[-2]}")
'''

''''
number=int(input("Number: "))
print("Number: "+str(number))
print(f"Number: {number}")
print("Number: {}".format(number))
'''


# str='kamal\'s Book'
# print(str)
# str="A sample set{1,2,3}"
# print(str)
# str='''He is a very lazy boy
# He can't properly prepare his homework'''
# print(str)
'''''
info={
     'Anannya': [19101001,3.1,165,3.93],
      'Zarin': [19101003,3.1,165,3.98],
      'Vabna': [19101011,3.1,165,3.71],
      'Tanmoy': [19101013,3.1,165,3.75],
      'Nashra': [19101018,2.2,155,2.70],
      'Kacchi': [19101044,3.1,165,3.50],
      'Shawan': [19101020,3.1,165,3.79],
      'Tanha': [19101036,3.1,165,3.55]
      }

# file=open('newFile','w')
# file.write(str(info))
# file.close()
'''

# dict={}
# data=[]
# f=open('newFile','r')
# file=f.read()
# f.close()
# #file=file.replace('{','').replace('}','').replace('\'','')
# print(file)
# for info in file:
#     data.append(info.split('],'))
#     # name=info.split(':')[0]
#     # data=info.split(':')[1]
#     # dict[name]=data
#
# print(len(data))
# #print(dict)
