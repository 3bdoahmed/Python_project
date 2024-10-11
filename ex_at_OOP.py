from datetime import date
class Student: 
    no_of_object=0 # to Know How object is Created 
    def __init__(self, name, age, courses): # init func 
        # object(inastance) atrbute 
        self.__name = name
        self.__age = age
        self.__courses = courses
        Student.no_of_object +=1 # incrase the counter when object is created 
    
    @classmethod 
    def initFormDirthyear(cls, name, birthyear, co): # must be as aan init func (the same arguments and ......)
        return cls(name, date.today().year - birthyear,co)
    def describe(self): # describe function to get atrebute 
        print(f"name of student is : {self.__name} and the age is {self.__age} and he has {self.__courses}")
    
    # Seters and Geters Methode  
    def get_name(self): 
        return self.__name
    def set_name(self, new_name):
        self.__name = new_name
    def get_age(self):
        return self.__age
    def set_age(self, new_age):
        self.__age = new_age
    def get_courses(self):
        return self.__courses
    def set_courses(self, new_cours):
        self.__courses = new_cours  

#__________________________________________________

# ex at static methode 
class math:
    @staticmethod
    def add(x,y):
        return x+y
    def add5(num):
        return num+5
    def add10(num):
        return num+10
    def pi():
        return 3.14

x = math.add(5,10)
y = math.add5(10)
z = math.pi()
print (x,y,z)       
#_____________________________________________________

# create an object foem class Student and pass the atrbute
student_1 = Student("Abdo", 21, {"C", "C++", "python", "OOP", "CCNA"})  
student_2 = Student.initFormDirthyear("AbdelRahman", 2002, "nothing") 
# set atrbute by use Seters Methode 
student_1.set_name("Ahmed")
student_1.set_age(22)
student_1.set_courses({"C", "C++", "python", "OOP", "CCNA", "Lunix"})

# get atrbute by use Geter Methode 
print(student_1.get_name())
print(student_1.get_age())
print(student_1.get_courses())

# not erroe due to it create new atrbute named "name"
student_1.name="mo"
print(student_1.name)

# get the methode describe 
student_1.describe()
student_2.describe() 
# get the class atrbute 
print(student_1.no_of_object)



