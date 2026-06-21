nome = "João"
idade = 22
grana = 51.34

print("{} tem {} anos e R${} no bolso.".format(nome, idade, grana))
print("{:12} tem {:3} anos e R${:5.2f} no bolso.".format(nome, idade, grana))
print("{:12} tem {:03} anos e R${:5.2f} no bolso".format(nome, idade, grana))
print("{:<12s} tem {:<3} anos e R${:5.2f} no bolso.".format(nome, idade, grana))

# posição dos par^metros dentro dos colchetes
print("{1} {0} {2}".format("a", "b", "c"))

print("{2} {2} {0} {1}".format("a", "b", "c",))

print(f"{nome} tem {idade} anos e R${grana} no bolso.")

print(f"{nome:12} tem {idade:3} anos e R${grana:5.2f}")

print(f"{nome:12} tem {idade:03} anos e R${grana:5.2f} no bolso")

print(f"{nome:<12s} tem {idade:<3} anos e R${grana:5.2f} no bolso")