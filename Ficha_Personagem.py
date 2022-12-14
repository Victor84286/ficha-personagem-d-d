"""
Monta uma ficha de personagem de Dangeons and Dragons
Feito por Victor Hugo Rocha, Matheus Herzog, Gabriel Esposito e Pedro Reis
"""
import random
import sys

def coleta_info():
  nome = input("Escreva o nome do seu personagem: ")
  if nome.upper() == "SAIR":
    sys.exit()
  while True:
    raca = input("Escreva a qual raça deseja pertencer\n(Humano, Anão, Elfo ou halfling)\n")
  
    if raca.upper() == "SAIR":
      sys.exit()
    if raca.lower() == "humano" or raca.lower() == "elfo" or raca.lower() == "anão" or raca.lower() == "halfling":
      rola_dados(nome, raca)
    print("Raça inválida! As opções são humano, elfo, anão, halfling")
    

def rola_dados(nome, raca):
  dados_tot = []
  for j in range(6):
    dados = []
    for i in range(4):
      dados.append(random.randint(1,6))
  
    menor = dados[0]
  
    for i in range(4):
      if menor > dados[i]:
        menor = dados[i]

    dados.remove(menor)

    dados = dados[0] + dados[1] + dados[2]
    
    dados_tot.append(dados)

  escolha_de_atributos(nome, raca, dados_tot)
  

def escolha_de_atributos(nome, raca, dados):
  dados_usados = dados.copy()
  
  atrib = {
    "STR": 0,
    "DEX": 0,
    "CON": 0,
    "INT": 0,
    "WIS": 0,
    "CHA": 0
  }
  
  for chave in atrib:
    while True:
      print(dados_usados)
      escolha = int(input("Escreva o dado que quer para " + chave + ": "))

      if escolha in dados_usados:
        atrib[chave] = escolha
        dados_usados.remove(escolha)
        break
    
      print("Valor passado é inválido! Tente novamente.")

  corrige_para_raca(nome, raca, dados, atrib)

def corrige_para_raca(nome, raca, dados, atrib):
  if raca.lower() == "humano":
    for chave in atrib:
      atrib[chave] += 1

  elif raca.lower() == "elfo":
    atrib["DEX"] += 2
    atrib["INT"] += 1

  elif raca.lower() == "anão":
    atrib["STR"] += 2
    atrib["CON"] += 2

  elif raca.lower() == "halfling":
    atrib["DEX"] += 2
    atrib["CHA"] += 1

  pergunta_certo(nome, raca, dados, atrib)
  
def pergunta_certo(nome, raca, dados, atrib):
  print("Resultados atribuídos com modificadores de raça:")
  
  for chave, valor in atrib.items():
    print(chave, valor)

  while True:
    escolha = input("Estes valores estão satisfatórios (S/N)?")
  
    if escolha.lower() == "n":
      escolha_de_atributos(nome, raca, dados)
      
    elif escolha.upper() == "S":
      salva_ficha(nome, raca, atrib)


def salva_ficha(nome, raca, atrib):
  nome_arquivo = nome + ".txt"
  print("==================")
  with open(nome_arquivo, "w") as arquivo:
    ficha = "Ficha de " + nome + " / " + raca + ":\n"
    print(ficha, end="")
    arquivo.write(ficha)

    for chave, valor in atrib.items():
      ficha = "\n" + chave + " " + str(valor)
      print(ficha, end="")
      arquivo.write(ficha)
  print("\n==================")
  sys.exit()

coleta_info()
