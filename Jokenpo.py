import random

escolhas=["pedra","papel","tesoura"]
jogada=""

def escolher(z):
   escolha=""
   for x in escolhas:
      for y in range(0,3):
         escolha=escolhas[z-1]
      return escolha

def jogar():
   n1=int(input("Digite:\n1 para jogar pedra\n2 para jogar papel\n3 para jogar tesoura\n"))
   while n1<1 or n1>3:
     n1=int(input("Valor incorreto, digite novamente:"))
   jogada=escolher(n1)
   print("="*40)
   print(f"Você jogou {jogada}")

   n2=random.randint(1,3)  
   jogada=escolher(n2)
   print(f"\nA máquina jogou {jogada}")
   print("="*40) 

   if n1==n2:
      print("Empate")
   elif (n1-n2)%3==1:
      print("Você venceu")
   else:
      print("A máquina venceu")

jogar()
