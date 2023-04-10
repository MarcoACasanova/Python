# stack objetiva.

class Stack:  # Definindo a class
    def __init__(self):  # definindo a construção da função.
        self.__stack_list = [] # adcionamos dois underscore para que stack_list não fique exposta.
#aqui nós encapsulamos a stack_list, tornamos ela privada, e ela só pode ser acessada diretamente pela classe.
    def push(self, val):
        self.__stack_list.append(val)
    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0
    
    def get_sum(self):
        return self.__sum
    
    def push_sum(self, val):
        self.__sum += val
        Stack.push(self, val)
    
    def pop__sum(self):
        self.__sum -= val
        return val
    
stack_object = AddingStack()

for i in range(5):
    stack_object.push(i)
print(stack_object.get_sum())

for i in range(5):
    print(stack_object.pop())
    