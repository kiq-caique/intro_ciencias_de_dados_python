quantidade_passos = int(input())
andar = 0
if quantidade_passos > 0:
  while andar < quantidade_passos:
    andar += 1
    if andar == 1:
      print(f"Explorador: {andar} passo")
    else:
        print(f"Explorador: {andar} passos")
else:
  print("Nenhum passo dado na floresta.")