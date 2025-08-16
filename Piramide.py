'''
Crie um programa em Python que peça ao usuário um número positivo. 
Com esse número, exiba duas pirâmides utilizando laço de repetição for: uma com o número da linha repetido 
e outra com uma sequência crescente de 1 até o número da linha.
'''

n=int(input("Digite um número positivo para exibir pirâmides numéricas: "))
for x in range(1,n+1):
  for y in range(0,x):
    print(x , end=" ")
  print()

print()

for x in range(1,n+1):
  for y in range(1,x+1):
    print(y , end=" ")
  print()
