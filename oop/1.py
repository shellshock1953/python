class C1():
    def setname(self,who):
        self.name = who

I1 = C1()
I2 = C1()
I1.setname('bob')
I2.setname('star')
print(I1.name)
