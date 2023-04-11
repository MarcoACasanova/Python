'''
A sua tarefa é alargar ligeiramente as capacidades da classe Queue . Queremos que ele tenha um método sem parâmetros que devolva True se a queue estiver vazia e False caso contrário.

Complete o código que fornecemos no editor. Execute-o para verificar se ele produz um resultado semelhante ao nosso.

Abaixo pode copiar o código que utilizámos no laboratório anterior:
'''

class QueueError(IndexError):
    pass

class Queue:
    def __init__(self):
        self.__queue = []

    def put(self, elem):
        self.__queue.insert(0, elem)

    def get(self):
        if len(self.__queue) == 0:
            raise QueueError("Queue is empty")
        return self.__queue.pop()

    def isempty(self):
        return len(self.__queue) == 0

class SuperQueue(Queue):
    pass

que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")