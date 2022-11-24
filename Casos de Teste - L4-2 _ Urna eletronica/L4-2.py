quantVotos = str(input("")).strip('\r')

quantidade_candidato1 = 0
quantidade_candidato2 = 0
quantidade_candidato3 = 0
quantidade_candidato4 = 0
contagem_nulos = 0
contVotos = 0

while ((quantidade_candidato1 + quantidade_candidato2 + quantidade_candidato3 + quantidade_candidato4 + contagem_nulos) < int(quantVotos)) and (quantVotos != "sair"):
    # Entrada de dados
    voto = str(input("")).strip('\r')

    if voto == "1":
        quantidade_candidato1 += 1
        contVotos = contVotos + 1
        continue
    elif voto == "2":
        quantidade_candidato2 += 1
        contVotos = contVotos + 1
        continue
    elif voto == "3":
        quantidade_candidato3 += 1
        contVotos = contVotos + 1
        continue
    elif voto == "4":
        quantidade_candidato4 += 1
        contVotos = contVotos + 1
        continue
    elif voto != "1" and voto != "2" and voto != "3" and voto != "4" and (voto != "sair"):
        contagem_nulos += 1
        contVotos = contVotos + 1
        continue
    elif voto == "sair":
        print(f'Nome--------------Votos--------------Porcentagem')
        porcentagem_candidato1 = ((quantidade_candidato1 / contVotos) * 100)
        print(f'José Alfredo ------ {quantidade_candidato1} ------------------- {porcentagem_candidato1:.2f}%')
        porcentagem_candidato2 = ((quantidade_candidato2 / contVotos) * 100)
        print(f'Maria Junqueira --- {quantidade_candidato2} ------------------- {porcentagem_candidato2:.2f}%')
        porcentagem_candidato3 = ((quantidade_candidato3 / contVotos) * 100)
        print(f'Marivaldo Silva --- {quantidade_candidato3} ------------------- {porcentagem_candidato3:.2f}%')
        porcentagem_candidato4 = ((quantidade_candidato4 / contVotos) * 100)
        print(f'Juliana Antônia --- {quantidade_candidato4} ------------------- {porcentagem_candidato4:.2f}%')
        porcentagem_nulo = ((contagem_nulos / contVotos) * 100)
        print(f'Nulo -------------- {contagem_nulos} ------------------- {porcentagem_nulo:.2f}%')
        break

else:
        print(f'Nome--------------Votos--------------Porcentagem')
        porcentagem_candidato1 = ((quantidade_candidato1 / int(quantVotos)) * 100)
        print(f'José Alfredo ------ {quantidade_candidato1} ------------------- {porcentagem_candidato1:.2f}%')
        porcentagem_candidato2 = ((quantidade_candidato2 / int(quantVotos)) * 100)
        print(f'Maria Junqueira --- {quantidade_candidato2} ------------------- {porcentagem_candidato2:.2f}%')
        porcentagem_candidato3 = ((quantidade_candidato3 / int(quantVotos)) * 100)
        print(f'Marivaldo Silva --- {quantidade_candidato3} ------------------- {porcentagem_candidato3:.2f}%')
        porcentagem_candidato4 = ((quantidade_candidato4 / int(quantVotos)) * 100)
        print(f'Juliana Antônia --- {quantidade_candidato4} ------------------- {porcentagem_candidato4:.2f}%')
        porcentagem_nulo = ((contagem_nulos / int(quantVotos)) * 100)
        print(f'Nulo -------------- {contagem_nulos} ------------------- {porcentagem_nulo:.2f}%')
