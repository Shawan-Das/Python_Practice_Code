'''
Class & objects
'''
# class Student:
#     count =0 #Class Attribute
#     #Constructor Function
#     def __init__(self):
#         Student.count +=1
#
# print(Student.count)
# std1 =Student()
# print(Student.count)



# class Student():
#     def __init__(self, name="guest", age=-1):
#         self.name=""  #instance attributes
#         self.age=-1   #instance attributes



# class Student:
#     def __init__(self, name="guest", age=-1):
#         self.name=name  #instance attributes
#         self.age=age   #instance attributes
#
#     def info(self):
#         print("Name: ",self.name, " Age: ",self.age)
#
#
# std1=Student("Shawan Das", 21)
# std1.info()


'''        -----------------!!!!!!--------------         '''


'''        inheritance      '''

# class qdrl:
#
#     def __init__(self,a,b,c,d):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
#
#     def perimeter(self):
#         print(self.a + self.b + self.c + self.d)
#
#
# class Rectangle(qdrl):
#
#     def __init__(self,a,b):
#         super().__init__(a,b,a,b)
#
#     def area(self):
#         print("Area of a rectangle: ",self.a * self.b)
#     def perimeter(self):
#         print("Rentangular part: perimeter: ", 2*(self.a+self.b))
#
#
# class Square(Rectangle):
#     def __init__(self,a):
#         super().__init__(a,a)
#
#     def area(self):
#         print("Area of a Square: ",self.a * self.a)
#
#     def perimeter(self):
#         print("Squre part: perimeter: ", 4*self.a)
#
#
# q1= Square(4)
# q1.perimeter()
# q1.area()


'''
-----------------!!!!!!!!!!!!!!!---------------
'''


'''------------Practice Portion--------------'''

# class information:
#
#     def __init__(self, name=" ",ID="--",semester=" ",dept=''):
#         self.name=name
#         self.id=ID
#         self.semester=semester
#         self.dept=dept
#
#     def print_info(self):
#         print("Name      : ",self.name)
#         print("ID        : ",self.id)
#         print("Semester  : ",self.semester)
#         print("Department: ",self.dept)
#         print()
#
#
# n=int(input("Total Student: "))
#
# info=dict()
# for i in range(n):
#     name=    input("Name       : ")
#     id=      input("ID         : ")
#     Semester=input("Semester   : ")
#     dept=    input("Department : ")
#
#
#     temp=information(name,id,Semester,dept)
#     info[id]=temp
#
#
# for i in info.keys():
#     info[i].print_info()
#
# info["19101001"].print_info()

'''-----------------------!!!!!!!!!!!!!!!!!!!---------------------'''

#part of ans 4


#------------



'''-------------------Other Portion----------------------------'''

# class student():
#
#     department = "CSE"
#
#     def __init__(self):
#         self.Name="Shawan Das"
#         self.ID="19101020"
#         self.Semester="3-1"
#
#
#     def printInfo(self):
#         print(f"Name : {self.Name} ID: {self.ID} Semester: {self.Semester} Department: {self.department}")
#
#
# std=student()         #Student class object
#
# std.department="EEE"
# std.Name="Tanmoy"
# std.ID="19101013"
#
#
# std.printInfo()



# x=69
#
# def fun():
#     y= globals() ['x']
#     y+= 10
#     print(y,end=":")
#     x=100
#     print(x)
#
#
# fun()
# x=70
# print(x)
# fun()
'''
    *
   * *
  * * *
 * * * *
* * * * *
.........
'''

#n=int(input())
'''-----------------------------------------'''
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
#
# print()
#
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
'''-------------------------------------------'''

'''-------------------------------------------'''
# space = 0
# for i in range(n,0,-1):
#     for s in range(space,0,-1):
#         print(" ",end="")
#
#     space+=2
#
#     for j in range(1,(i*2)):
#         print("*",end=" ")
#
#     print()
# space-=3
# for i in range(2,n+1):
#     for s in range(1,space):
#         print(" ",end="")
#
#     space-=2
#
#     for j in range(1,(i*2)):
#         print("*",end=" ")
#
#     print()
'''------------------------------------------'''
'''-----------------------------------------'''
# space=n
# for i in range(1,n+1):
#     for s in range(1,space):
#         print(" ",end="")
#
#     space-=1
#
#     for j in range(1,i+1):
#         if (i==1 or i==2) or (i>2 and (j==1 or j==i) or i==n):
#             print("*", end=" ")
#         else:
#             print(" ",end=" ")
#
#     print()
#
# space=(n*2)-1
# for i in range(1,n+1):
#     for s in range(1,space):
#         print(" ",end="")
#
#     space-=2
#
#     for j in range(1,(i*2)):
#         if i==1 or i==n or (i>1 and (j==1 or j==i*2-1)):
#             print("*", end=" ")
#         else:
#             print(" ",end=" ")
#
#     print()
'''------------------------------------------'''
'''------------------------------------------'''
# space = 0
# for i in range(n*2,0,-2):
#     for s in range(space,0,-1):
#         print(" ",end="")
#
#     space+=2
#
#     for j in range(1,i):
#         print("*",end=" ")
#
#     print()
# space-=3
# for i in range(3,n*2,+2):
#     for s in range(1,space):
#         print(" ",end="")
#
#     space-=2
#
#     for j in range(1,i+1):
#         print("*",end=" ")
#
#     print()
'''--------------------------------------'''

'''----------------------------------'''
# space = 0
# for i in range(n*2,0,-2):
#     for s in range(space,0,-1):
#         print(" ",end="")
#
#     space+=1
#
#     for j in range(1,i):
#         print("*",end="")
#
#     print()
# space-=1
# for i in range(3,n*2,+2):
#     for s in range(1,space):
#         print(" ",end="")
#
#     space-=1
#
#     for j in range(1,i+1):
#         print("*",end="")
#
#     print()

'''----------------------------------'''


















# ignore part

#
# class school():
#     def __init__(self, name, year):
#         self.school_name=name
#         self.passing_year=year
#
#     def infoS(self):
#         print(f"School: {self.school_name}  SSC Batch: {self.passing_year}")
#
# class college():
#     def __init__(self, name, year):
#         self.college_name=name
#         self.passing_year=year
#
#     def infoC(self):
#         print(f"College: {self.college_name}  HSC Batch: {self.passing_year}")
#
# class university():
#     def __init__(self, name, year):
#         self.university = name
#         self.year = year
#
#     def infoU(self):
#         print(f"College: {self.university}  HSC Batch: {self.year}")
#
#
# class student(school,college,):
#     def __init__(self,name,id,sName,sYear,cName,cYear):
#         super().__init__(sName,sYear)
#         super().__init__(cName,cYear)
#         self.name=name
#         self.id=id
#     def printInfo(self):
#         print(f"Name: {self.name}  ID: {self.id}")
#
#
#
# temp=student("Shawan Das","19101020","K.L.Jubilee School & College","2016","Dhaka Imperial College","2018")
#
# temp.printInfo()
# temp.infoS()
# # temp.infoC()
# print()
# x =input()









# class Student:
#     age = '20' #class attribute
#     def __init__(self, name):
#         self.__name= name   #instance attribute
#
#     @property
#     def name(self):
#         print("getter function called") # Getter method
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         print("Setter method")
#         self.__name = value
#
#     @name.deleter
#     def name(self):
#         print("Deleting")
#         del self.__name
#
#     @classmethod
#     def tostring(cls):
#         print("Class attribute, age = ", cls.age) #only class attribute will work properly
#
#
# std= Student("abc")
# print(std.name)
# std.name= "xyz"
# print(std.name)
# del std.name
# Student.tostring()


# class Employee:
#     def __init__(self):
#         self.name='Shan'
#         self.salary= 50000
#     def __str__(self):
#         return 'name = '+ self.name+' salary = '+str(self.salary)+" $"

  # deleting something:
  # def __del__(self):
  #     pass

# Python program to demonstrate
# multiple inheritance

# Base class1
# https://www.geeksforgeeks.org/multiple-inheritance-in-python/
# Python Program to depict multiple inheritance
# when method is overridden in both classes

# class Class1:
#     def m(self):
#         print("In Class1")
#
#
# class Class2(Class1):
#     def m(self):
#         print("In Class2")
#
#
# class Class3(Class1):
#     def m(self):
#         print("In Class3")
#
#
# class Class4(Class3, Class2):
#     def m(self):
#         print("In Class4")
#
#
# print(Class2.mro())  # This will print list
# print(Class2.__mro__)  # This will print tuple


'''------------- Destructor function------------------------'''

# class Employee:
#
#     def __init__(self):
#         print("EMP Created")
#     def __del__(self):
#         print("EMP deleted")
'''-------------------------------------------'''


'''---------------------inheritance--------------------------------------------'''

'''-------------single inheritance-----------'''
# class parent:
#     def fn1(self):
#         print("Parent Class")
# class child(parent):
#     def fn2(self):
#         print("Child class")
# object = child()
# object.fn1()
# object.fn2()
'''----------------------------'''

'''-------------MULTIPLE INHERITANCE--------------'''
#A+B ---> C

# class Mother:
#     mother_name="XX"  # class attribute
#     def mother(self):
#         print(self.mother_name)
#
# class Father:
#     father_name="XY"
#     def father(self):
#         print(self.father_name)
#
# class Son(Mother,Father):
#     def parent(self):
#         print(self.mother_name)
#         print(self.father_name)
#
# s= Son()
# s.parent()
'''---------------------------------------'''

'''-------------Multilevel Inheritance------------'''
#A-->B-->C

# class Grandpa:
#     def __init__(self,grandpa_name):
#         self.grandpa_name= grandpa_name   #instance attribute
#
# class Father(Grandpa):
#     def __init__(self, father_name, grandpa_name):
#         super().__init__(grandpa_name)
#         self.father_name= father_name
#
# class Son(Father):
#     def __init__(self,name, father_name, grandpa_name):
#         super().__init__(father_name, grandpa_name)
#         self.name=name
#
#     def print(self):
#         print(self.name)
#         print(self.father_name)
#         print(self.grandpa_name)
#
# s= Son('G3','G2','G1')
# s.print()

'''-------------------------------------------'''

'''---------------Association--------------'''
# class teacher:
#   def __init__(self,name):
#     self.name = name
#   def get_name(self):
#     return self.name
#
# class student:
#   def __init__(self,name):
#     self.name = name
#   def get_name(self):
#     return self.name
#
# t1 = teacher("HMD")
# s1 = student("xyz")
# print(f"{t1.get_name()} teaches {s1.get_name()}")

'''---------------------------------------'''

'''-------------Aggregation---------------'''
# class engine:
#     def __init__(self):
#         self.model = -1
#         self.rpm = -1
#
#     def set_engine(self):
#         self.model = int(input("Enter engine model: "))
#         self.rpm = int(input("Enter engine's rpm model: "))
#
#     def get_engine(self):
#         print(f"Engine model: {self.model}")
#         print(f"Engine rpm: {self.rpm}")
#
#
# class car:
#     def __init__(self, brand, engine):
#         self.brand = brand
#         self.engine = engine
#
#     def get_car(self):
#         print(f"Car brand: {self.brand}")
#         self.engine.get_engine()
#
#     def __del__(self):
#         print("deleting car object")
#
#
# e1 = engine()
# e1.set_engine()
# c1 = car("Tesla", e1)
# c1.get_car()
# del c1
# e1.get_engine()

'''--------------------------------------------'''
'''--------------------Composition-------------------'''
# class engine:
#     def __init__(self):
#         self.model= -1
#         self.rpm = -1
#
#     def set_engine(self):
#         self.model= int(input("Engine Model Number: "))
#         self.rpm= int(input("RPM Model: "))
#
#     def get_engine(self):
#         print(f"Engine Model: {self.model}")
#         print(f"RMP Model: {self.rpm}")
#
# class car:
#     def __init__(self, brand):
#         self.brand= brand
#         self.engine= engine()
#
#     def set_engine(self):
#         self.engine.set_engine()
#
#     def get_car(self):
#         print(f"Car brand: {self.brand}")
#         self.engine.get_engine()
#
#     def __del__(self):
#         print("delete car ")
#         print(engine.get_engine())
#
#
# c1 = car("BMW")
# c1.set_engine()
# c1.get_car()
# del c1
'''-----------------------------------------------------'''

