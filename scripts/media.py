print("""

Visualizador de nota

1. Transita se media maior que 10.
2. Nao transita se media menor que 10

""")


media = int(input("Digite a sua media: "))
if media > 10:
    print("Transita")
else:
    print("Nao transita")
