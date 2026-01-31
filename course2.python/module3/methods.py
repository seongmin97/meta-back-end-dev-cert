class A:
    def c(self):
        return "Function inside A"

class B:
    def c(self):
        return "Function inside B"

class C(A, B):
    def c(self):
        return "Function inside C"

# class D(A, C) error: 
class D(C, A):
    pass

d = D()
print(d.c())