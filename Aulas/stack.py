# abordagem processual

stack = [] # criação de uma stack

def push(val): # definição de função para alimentar a stack.
    stack.append(val)
# partimos do pressuposto que o último item armazenado
# é o item do "topo" da lista

def pop():
    val = stack[-1]
    del stack[-1]
    return val

push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())