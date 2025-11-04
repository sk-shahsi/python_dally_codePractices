class A:
    def state_1(self):
        print("State_1 prsent")

    def state_2(self):
        print("State_2 prsent")

    def state_3(self):
        print("State_3 prsent")

class B:
    def state_4(self):
        print("State_4 prsent")

    def state_5(self):
        print("State_5 prsent")

#multilevel Inheritance
class C(A,B):
    def state_6(self):
        print("State_6 prsent")

a=A()
a.state_1()
a.state_2()
a.state_3()
c=C()
c.state_1()
c.state_2()
c.state_3()
c.state_4()
c.state_5()
c.state_6()
