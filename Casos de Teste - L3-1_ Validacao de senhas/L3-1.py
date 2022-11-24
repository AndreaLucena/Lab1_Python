#Entrada de dados
senha1 = str(input()).strip('\r')
senha2 = str(input()).strip('\r')
#Verificando condição
if (senha2 != senha1):
  print(f"Senha inválida")
else:
  if ((len(senha1)) >= 4) and ((len(senha1)) <= 8):
    print(f"Senha válida")
  else:
    print(f"Senha inválida")
