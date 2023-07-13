print("""

A Sistec resolveu dar um aumento de salário aos seus
colaboradores e nos contactaram para desenvolver um
programa que calcula os reajustes.

Sistema de reajuste de salários - Sistec.

1. Salários até Kz 128.000,00 (incluindo) : aumento de 20%
2. Salários entre Kz 280.000,00 e Kz 700.000,00 : aumento de 15%
3. Salários entre Kz 700.000,00 e Kz 1.500.000,00 : aumento de 10%
4. Salários de Kz 1.500.000,00 em diante : aumento de 5%

""")

salario = float(input("Informe o seu salário (Kz): "))

if salario <= 128_000.0:
    percentagem = 0.2
    aumento = salario * percentagem
    novo_salario = salario + aumento
elif 280_000.0 <= salario <= 700_000.0:
    percentagem = 0.15
    aumento = salario * percentagem
    novo_salario = salario + aumento
elif 700_000.0 <= salario <= 1_500_000.0:
    percentagem = 0.1
    aumento = salario * percentagem
    novo_salario = salario + aumento
elif salario >= 1_500_000.0:
    percentagem = 0.05
    aumento = salario * percentagem
    novo_salario = salario + aumento

print("Salário antes do reajuste: ", "Kz", salario)
print("Percentagem: ",  str(int(percentagem * 100)) + "%")
print("Valor do aumento: ", "Kz", aumento)
print("Novo Salário: ", "Kz", novo_salario)
