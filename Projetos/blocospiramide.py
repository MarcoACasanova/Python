blocks = int(input("Digite o número de blocos que os construtores têm: "))

height = 0
layer_blocks = 1
while layer_blocks <= blocks:
    height += 1
    blocks -= layer_blocks
    layer_blocks += 1

print("A altura da pirâmide construída é", height)
