#Access Modifier
#public
class Student:
    # constructor is defined
    def __init__(self, age, name):
        self.age = age               # public variable
        self.name = name             # public variable

obj = Student(20,"Puja")
print(obj.age)
print(obj.name)


#Private
"""class Student: 
    def __init__(self, age, name): 
        self.__age = age      # An indication of private variable
        
        def __funName(self):  # An indication of private function
            self.y = 34
            print(self.y)

class Subject(Student):
    pass

obj = Student(21,"Puja")
obj1 = Subject

# calling by object of class Student
print(obj.__age)
print(obj.__funName())

# calling by object  of class Subject
print(obj1.__age)
print(obj1.__funName())"""



#Name mangling
class MyClass:
    def __init__(self):
        self._nonmangled_attribute = "I am a Engineer"
        self.__mangled_attribute = "How are You"

my_object = MyClass()

print(my_object._nonmangled_attribute)
print(my_object._MyClass__mangled_attribute)

#Protected

class Student:
    def __init__(self):
        self._name = "Puja"

    def _funName(self):      # protected method
        return "Hello"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())
