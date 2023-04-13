class SimpleClass:
    def other(self):
        print("other")

    def method(self):
        print("method")
        self.other()

obj = SimpleClass()
obj.method()