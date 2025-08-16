class Menu:
    def __init__(self):
        self.__usuarios_cadastrados=["Alex","Bruno","Caio"]
        self.__senhas_cadastradas=["11","12","13"]
    
    def exibir_menu(self):
        while True:
            try:
              menu=int(input("Digite 1 para realizar login \nDigite 2 para cadastrar\nDigite 3 para sair\n"))
              if menu==1:
                  self.__logar()
                  return False
              elif menu==2:
                  self.__cadastrar() 
              elif menu==3:
                  return False
            except ValueError as e:
                 print("\nValor inválido, digite novamente.\n")
                                 
    def __logar(self):
        usuario=input("Digite o nome do usuario:\n")
        senha=input("Digite a senha:\n")
        for contagem, cadastro in enumerate(self.__usuarios_cadastrados):
            if usuario==cadastro and senha==self.__senhas_cadastradas[contagem]:
               print(f"Bem-vindo {usuario}")
               break
            elif contagem==len(self.__usuarios_cadastrados)-1:
               print("Usuario ou senha incorretos")
               
    def __cadastrar(self):
        nome=input("Crie o nome do usuario: \n")
        for cadastro in self.__usuarios_cadastrados:
          while cadastro==nome:
            nome=input("Usuario já existe, tente outro nome.\n")
        self.__usuarios_cadastrados.append(nome)
        senha=input("Crie uma senha: ")
        self.__senhas_cadastradas.append(senha)
        print("\nUsuario cadastrado com sucesso!\nVoltando ao menu...\n")
    
