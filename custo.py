descricao = str(input ("descricao produto"))
custo = float(input ("custo"))
margem = float(input ("margem"))
preco = custo + (custo * margem)/100
print("o preco de venda de", descricao, "é: ", preco)