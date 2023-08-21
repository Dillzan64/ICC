#Exercicio 5.16 Dá erro em cada valor
#Exercicio 5.17 Ocorre um erro "0 cedulas de 100"
#Exercicio 5.18
#Exercicio 5.19
#Exercicio 5.20
#Exercicio 5.21
valor = float(input("Digite o valor a pagar: Ou digite 0 para sair "))
while True:
    atual = 100
    cédulas = 0    
    
    apagar = valor 
    if valor == 0:
        break
    if atual <= apagar:
        apagar = apagar - atual
        cédulas +=1 
    else:
        print("%d cédula(s) ou moeda(s) de R$%5.2f" % (cédulas, atual))
        if apagar == 0:
            break 
        elif atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        elif atual == 1:
            atual = 0.50
        elif atual == 0.50:
            atual = 0.10
        elif atual == 0.10:
            atual = 0.05
        elif atual == 0.05:
            atual = 0.02
        elif atual == 0.02:
            atual = 0.01
        cédulas = 0