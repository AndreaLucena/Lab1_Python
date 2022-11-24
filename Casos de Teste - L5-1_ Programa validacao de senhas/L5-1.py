
verif = False
while (verif == False):
    # Entrada de dados
    senha1 = str(input()).strip('\r')
    senha2 = str(input()).strip('\r')

    if senha1 != senha2:
        print("Senha inválida")
    elif len(senha1) < 7:
        print("Senha inválida")
    elif len(senha1) > 8:
        print("Senha inválida")
    elif senha1.isalpha():
        print("Senha inválida")
    elif senha1.islower():
        print("Senha inválida")
    else:
        verif = True
        print("Senha válida")
    continue


