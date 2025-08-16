import random
class JogoVelha:
  def __init__(self):
    self.tabuleiro = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

  def exibir_tabuleiro(self):
    for linha in self.tabuleiro:
        print(linha)

  def verificar_vitoria(self, simbolo):
    # Verificar linhas
    for linha in self.tabuleiro:
      if all(spot == simbolo for spot in linha):
        return True

    # Verificar colunas
    for col in range(3):
      if all(self.tabuleiro[row][col] == simbolo for row in range(3)):
        return True

    # Verificar diagonais
    if all(self.tabuleiro[i][i] == simbolo for i in range(3)) or all(self.tabuleiro[i][2 - i] == simbolo for i in range(3)):
       return True

    return False

  def verificar_empate(self):
    for linha in self.tabuleiro:
      for spot in linha:
        if spot not in ["X", "O"]:
           return False
    return True

class Jogador(JogoVelha):
  def __init__(self):
      super().__init__()
      self.vencedor = False

  def jogar(self):
    self.exibir_tabuleiro()
    turno = 1

    while not self.vencedor:
      if turno % 2 == 1:
         simbolo = "X"
         jogador = "Você"
      else:
         simbolo = "O"
         jogador = "Maquina"
         
      jogada_valida = False
      while not jogada_valida:
        try:
          if jogador=="Você":
             jogada = int(input("Digite um número para marcar o jogo da velha: "))
             if jogada < 1 or jogada > 9:
                raise ValueError("Número fora do intervalo")
          else:
             jogada=random.randint(1,9)
          linha = (jogada - 1) // 3
          coluna = (jogada - 1) % 3

          if self.tabuleiro[linha][coluna] not in ["X", "O"]:
               self.tabuleiro[linha][coluna] = simbolo
               jogada_valida = True
               print(f"{jogador} jogou na posição {jogada}")
          else:
               print(f"{jogador} tentou marcar uma posição já ocupada.")
        except ValueError as e:
          print(f"Entrada inválida: {e}. Tente novamente.")
        print("="*30)
        self.exibir_tabuleiro()

      if self.verificar_vitoria(simbolo):
         print(f"{jogador} venceu!")
         self.vencedor = True
      elif self.verificar_empate():
         print("O jogo empatou!")
         self.vencedor = True

      turno += 1


j1 = Jogador()
j1.jogar()
