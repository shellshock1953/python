class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(self.name, self.age)
person1 = Person('Bob',11)
person1.info()
