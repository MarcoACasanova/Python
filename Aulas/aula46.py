lista = [10, 20, 30 , 40, 50, 60]
print(lista)
print(lista[2])
numero = lista[0]
print(numero)

# CRUD = create, read, update, delete

lista[2] = 300
print(lista[2]) # se você reparar, como você alterou após 
# o primeiro print o número mudou mesmo sendo lista[2]

del lista[2] #aqui vamos deletar o indica número 2

print(lista) # dica evite ter que fazer o python refazer a lista (envolve muito processamento)
lista.append(70) # aqui estamos adicionando um item a mais na lista
print(lista)
lista.pop() # este comando remove o ultimo lista da lista
print(lista) # lista atualizada
ultimo_valor = lista.pop() # exemplo para mostrar qual número foi excluido.
print(lista, 'Removido', ultimo_valor)
exemplo = lista.pop(2) # esse e um exemplo de que não necessariamente o pop exclui o ultimo item, podemos excluir o que indicarmos
print(lista, 'Removido', exemplo)
