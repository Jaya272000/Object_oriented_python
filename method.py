# Three type of method

# instance variable
# class variable
# static variable

# instance
# class student:

#   school='telusko university'
#   def __init__(self,m1,m2,m3):
#     self.m1=m1
#     self.m2=m2
#     self.m3=m3
  

#   def avg(self):
#     return(self.m1+self.m2+self.m3)/3
  
#   def get_m1(self):
#     return self.m1
  
#   def ser_m1(self,value):
#     self.m1=value 


# # object are define
# s1=student(23,43,12)
# s2=student(23,54,65)

# s1.avg()
# s2.avg(  )


# class and static
class student:

  school='telusko university'
  def __init__(self,m1,m2):
    self.m1=m1
    self.m2=m2
  @classmethod
  def info(cls):
    return cls.school
  def infoschool():
    print("this is student clsss")

print(student.info())
student.infoschool()


# inner class in python



