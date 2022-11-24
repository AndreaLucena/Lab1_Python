idade = int(input())
analf = str(input(""))

if ((idade > 18) and (idade < 75) and (analf == 'n')):
  print(f"Voto obrigatório")
elif (analf == 's'):
  print(f"Voto não obrigatório")
else:
  print(f"Voto não obrigatório")