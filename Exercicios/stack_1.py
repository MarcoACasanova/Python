'''
introduza uma propriedade concebida para contar operações pop e nomeie-a de uma forma que garanta a sua ocultação;
inicialize-a a zero no interior do construtor;
forneça um método que devolva o valor atualmente atribuído ao contador (nomeie-o get_counter()).
'''

class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        super().__init__()
        self.__pop_count = 0

    def get_counter(self):
        return self.__pop_count  
        
    def pop(self):
        val -= super().pop()
        self.__pop_count += 1
        return val

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())