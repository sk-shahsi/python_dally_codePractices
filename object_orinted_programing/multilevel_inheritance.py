


class A:
    print("class A first print")
    def step_1(self):
        print("step_1 from A class")


class B(A):
    print("class B first print")
    def step_2(self):
        print("step_2 from B")


class Cc(B):
    print("class Cc first print")

    def step_3(self):
        print("step_3 from C")


c=Cc()
c.step_1()
c.step_2()
c.step_3()

