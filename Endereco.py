import requests

cep=input("Digite seu CEP: ")
if len(cep) != 8:
   print("CEP inválido")
   exit()
link=f"https://viacep.com.br/ws/{cep}/json/"
requisicao=requests.get(link)
endereco=requisicao.json()

cep1=endereco['cep']
logradouro=endereco['logradouro']
complemento=endereco['complemento']
bairro=endereco['bairro']
localidade=endereco['localidade']
uf=endereco['uf']

print(endereco)
