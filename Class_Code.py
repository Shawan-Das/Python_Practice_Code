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