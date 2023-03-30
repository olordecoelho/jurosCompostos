capitalinicial = 0
juros = 0
tempo = 0



while capitalinicial <=0:
    capitalinicial = float(input("Insira o capital inicial: "))
    if capitalinicial <=0:
        print("Capital inicial deve ser maior do que 0")
        
prit(capitalinicial)