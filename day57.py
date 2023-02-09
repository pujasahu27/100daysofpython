class Person:
    name= "Rich"
    occupation="Softwware Developer"
    networth=10
    def info(self):
        print(f"{self.name} is a {self.occupation}")
a=Person()
b=Person()
c=Person()
a.name="Ansh"
a.occupation="Accountant"
b.name="nandu"
b.occupation="HR"
a.info()
b.info()
c.info()
