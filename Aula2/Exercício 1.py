"""
Programa soma ou multiplica dois números
"""

a = int(input("Digite um número"))
b = int(input("Digite outro número"))
operacao = input("Soma ou Multiplicação?")
soma = a+b;
mult = a*b;

if operacao == 'soma':
    print(soma)
else:
    print(mult)