#constructor in python
class Person:
    def __init__(self, n, o):
        print("Hey I am a person")
        self.name=n
        self.occ=o
    def info(self):
        print(f"{self.name} is a {self.occ}")
a=Person("Harry", "Developer")
b=Person("Divya", "HR")
a.info()
b.info()
        
