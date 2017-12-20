class A:

    def __init__(self):
        self.attr1 = 'attrA'

    def foo(self):
        print("I'm foo!")

class A1(A):

    def __init__(self):
        super().__init__()

class B(A1):

    def __init__(self):
        super().__init__()
        self.attr2 = 'attrB'


b = B()
b.foo()
print(b.attr1)
print(b.attr2)
