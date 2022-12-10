k = float(input("Dê a quantidade de Km percorridos: "))
d = float(input("Dê a quantidade de dias em que o carro foi usado: "))
valor = k * 0.15 + d * 60
print("Usando o carro por {} dias e percorendo {:.2f}Km o valor final a se pagar é R${:.2f}".format(d, k, valor))