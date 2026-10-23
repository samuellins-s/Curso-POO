class A:
    def ola(self):
        print('Olá de A')


class B(A):
    pass


class C(A):
    def ola(self):
        print('Olá de C')


class D(C, B):
    pass


D().ola()
print(D.__mro__)