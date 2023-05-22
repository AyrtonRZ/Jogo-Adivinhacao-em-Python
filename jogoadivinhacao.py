print("")
print("######################################")
print("#                                    #")
print("#  Bem vido ao Jogo de adivinhacao   #")
print("#                                    #")
print("######################################")

numSecreto = 42
totalTentativa = 5
rodada = 1

while(rodada <= totalTentativa):
  print("")
  print("Tentativa: {} de {}.".format(rodada, totalTentativa))
  chute_str = input("Digite seu numero: ")
  print("Voce digitou: ", chute_str)
  #forma simplificada
  #chute = int(input("Digite o seu numero: "))

  #melhor forma
  chute = int(chute_str)
  acertou = chute == numSecreto
  numMaior = chute > numSecreto
  numMenor = chute < numSecreto

  if(acertou):
    print("Voce acertou!!!!")
    print("PARABENS!!")
  else:
    if(numMaior):
      print("Voce errou!, seu chute foi maior que o Secreto.")
    elif(numMenor):
      print("Voce errou!, seu chute foi menor que o Secreto.")

  rodada = rodada +1
  print("")
  print("######################################")

print("#           Fim do jogo              #")
print("######################################")
