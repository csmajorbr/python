# Página 107
nome = "João"
idade = 22
valor = 51.34

print("%s tem %d anos e apenas R$%5.2f no bolso." % (nome, idade, valor))
print("%s tem %d anos e R$%f no bolso" % (nome, idade, valor))
print("%12s tem %3d anos e R$%5.2f no bolso." % (nome, idade, valor))
print("%12s tem %03d anos e R$%5.2f no bolso." % (nome, idade, valor))
print("%-12s tem %-3d anos e R$%-5.2f no bolso." % (nome, idade, valor))
