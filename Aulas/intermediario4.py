'''
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir
Existe o escopo global e local
o escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
'''
x = 1 # essa variavel não é a mesma de dentro do escopo.
# e caso eu queira definir variavel X, tem que ser antes do escopo
# se eu definir X dentro do escopo, executar o escopo e tentar definir X após, irei causar um erro no programa
def escopo():
    x = 10
    def outra_funcao():
        y = 2
        print(x,y)
    outra_funcao()
    print(x)

print(x)
escopo()
print(x)

# se dentro do escopo eu colocar global x, eu estou dizendo ao visual
# que o x é a váriavel declarada antes do global (não tem como)
# usar o comando global sem a variável já declarada.