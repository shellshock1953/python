class Person():

    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def __str__(self):
        return ('Person: %s %s %s' % (self.name, self.job, self.pay))

    def surname(self):
        return self.name.split()[-1]

    def giveRaise(self, persent):
        return int(self.pay + (self.pay * persent))


class Manager(Person):

    def giveRaise(self, persent):
        return self.pay + (self.pay * persent + 100)

if __name__ == '__main__':
    bob = Person('Bob Marley', 'developer', 3600)
    sue = Manager('Sue Manager', 'manager', 4800)
    sue.giveRaise(0.2)
    print(bob)
    print(sue)
