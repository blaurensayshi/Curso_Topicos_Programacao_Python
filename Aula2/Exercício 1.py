"""
Programa soma ou multiplica dois números
"""

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
operacao = input("Soma ou Multiplicação? ")
soma = a+b;
mult = a*b;

if operacao == 'soma' or operacao == 'Soma' or operacao == 'SOMA' :
    print(soma)
else:
    print(mult)
