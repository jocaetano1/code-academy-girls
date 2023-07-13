from datetime import date
from time import sleep

from database import alunas, presencas


print("""

»»»»»»»»»»»»»»»»»»»» CODE ACADEMY:GIRLS ««««««««««««««««««

Sistema de registro de presenças

""")

run = True
while run:
    print("""

Menu de opções:

[1] - Inserir nova aluna
[2] - Registrar presença
[3] - Visualizar alunas
[4] - Visualizar presenças
[9] - Sair

""")

    opcao = input("Escolha uma das opções do menu: ").strip()

    if opcao == "1":
        nome = input("Digite o seu nome: ").strip()
        numero_do_bi = input("Digite o seu B.I: ").strip()
        curso = input("Digite o seu curso: ").strip()
        computador = input("Digite o seu computador: ").strip()

        formanda = {}
        formanda["nome"] = nome
        formanda["curso"] = curso
        formanda["computador"] = computador

        aluna = alunas.get(numero_do_bi)
        if aluna is None:
            alunas[numero_do_bi] = formanda
            print("\n Aluna registrada com sucesso.")
        else:
            print("\n Aluna já foi registrada.")

    if opcao == "2":
        identidade = input("Digite o número de seu B.I: ")
        resultado = identidade.strip()
        aluna = alunas.get(identidade)
        if aluna:
            if len(presencas) == 0:
                hora_da_entrada = input("Digite a hora de entrada: ")
                presenca = {
                    identidade: {
                        **aluna,
                        "hora_de_entrada": hora_da_entrada,
                        "hora_de_saida": "",
                        "data": date.today().isoformat()
                    }
                }
                presencas.append(presenca)
            else:
                for presenca in presencas:
                    if identidade in presenca.keys():
                        registro_de_presenca = presenca.get(identidade)
                        break
                    else:
                        registro_de_presenca = None
                if registro_de_presenca is None:
                    hora_da_entrada = input("Digite a hora de entrada: ")
                    presenca = {
                        identidade: {
                            **aluna,
                            "hora_de_entrada": hora_da_entrada,
                            "hora_de_saida": "",
                            "data": date.today().isoformat()
                        }
                    }
                    presencas.append(presenca)
                else:
                    hora_de_saida = registro_de_presenca.get(
                        "hora_de_saida")
                    data = registro_de_presenca.get("data")
                    hoje = date.today().isoformat()
                    if data == hoje and hora_de_saida == "":
                        hora_de_saida = input("Digite a hora de saída: ")
                        registro_de_presenca["hora_de_saida"] = hora_de_saida
                    else:
                        print("A presença já foi registrada.")
        else:
            print("\n O número do B.I não corresponde aos dados de nenhuma aluna.")

    if opcao == "3":
        for index, aluna in enumerate(alunas.values()):
            mensagem = f"{index + 1}º - {aluna.get('nome')}"
            print(mensagem)
    if opcao == "4":
        print("\n ******************* Lista de presenças ******************* \n")
        for index, presenca in enumerate(presencas):
            for _, valor in presenca.items():
                nome = valor.get("nome")
                hora_de_entrada = valor.get("hora_de_entrada")
                hora_de_saida = valor.get("hora_de_saida")
                data = valor.get("data")
                print(
                    f"{index + 1}º - {data}: {nome} == ({hora_de_entrada}, {hora_de_saida})")

    if opcao == "9":
        print("""

Sistema finalizando...

""")
        sleep(2.5)
        run = False
