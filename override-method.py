class A:
    def a(self, msg):
        print("From A : " + msg)


class B(A):
    def a(self, msg, new):
        print(msg + " & " + new)


a = A()
a.a("new")

b = B()
b.a("hello", "new")
