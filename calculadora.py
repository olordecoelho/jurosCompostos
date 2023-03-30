

capitalinicial = 0
juros = 0
tempo = 0



while True:
    capitalinicial = float(input("Insira o capital inicial: "))
    if capitalinicial <0:
        print("Capital inicial não pode ser menor do que 0")
    else:
        break

while True:
    juros = float(input("Insira a taxa de juros: "))
    if juros <0:
        print("a taxa de juros não pode ser menor do que 0")
    else:
        break
        
while True:
    tempo = int(input("Insira por quanto tempo seu capital ficará aplicado: "))
    if tempo <0:
        print("tempo não pode ser menor do que 0")
    else:
        break


total = capitalinicial * pow((1 + juros / 100), tempo)
print(F"Seu saldo depois de {tempo} anos será R${total:.2f}")
