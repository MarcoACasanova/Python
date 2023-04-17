class A:
    X = 0
    def __init__(self, v = 0):
        self.y = v
        A.X += v

a = A()
b = A(1)
c = A(2)

print(c.X)