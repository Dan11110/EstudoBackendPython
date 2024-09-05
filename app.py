import os

restaurantes = ["McBurguer", "Donalds King", "Totts", "Restaurante de regatas Vasco da Gama"]

def encerrar_app():
  os.system('cls')
  print("Programa encerrado")

def listar_pedidos():
  os.system('cls')
  print(restaurantes)    

def cadastrar_restaurante():
  os.system('cls')
  print("Bem vindo ao cadastro de novos restaurantes\n")
  
  restaurante_novo =input("Digite o nome do restaurante: ")
  restaurantes.append(restaurante_novo)
  input(f"Restaurante {restaurante_novo} adicionado com sucesso!!!\n Digite uma tecla para voltar ao menu principal")
  main()

def escolha_errada():
  input("Opção incorreta, digite uma tecla para voltar ao menu principal")
  main()


def exibir_nome():
      print("""

      ██████╗░███████╗██╗░░░░░██╗██╗░░░██╗███████╗██████╗░██╗░░░██╗
      ██╔══██╗██╔════╝██║░░░░░██║██║░░░██║██╔════╝██╔══██╗╚██╗░██╔╝
      ██║░░██║█████╗░░██║░░░░░██║╚██╗░██╔╝█████╗░░██████╔╝░╚████╔╝░
      ██║░░██║██╔══╝░░██║░░░░░██║░╚████╔╝░██╔══╝░░██╔══██╗░░╚██╔╝░░
      ██████╔╝███████╗███████╗██║░░╚██╔╝░░███████╗██║░░██║░░░██║░░░
      ╚═════╝░╚══════╝╚══════╝╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░
            
            """)

def exibir_opcoes():
      print("""
            1 - Cadastrar
            2 - Listar
            3 - Ativar
            4 - Sair
            """ 
            )

def selecionar_opcoes():
      try:
            opcao_escolhida = int(input("Selecione uma opção: "))   
            match opcao_escolhida:
                  case 1:
                        cadastrar_restaurante()
                  case 2:
                        listar_pedidos()
                  case 3:
                        print("Ativar um novo pedido")
                  case 4:
                        encerrar_app()
                  case _:
                        escolha_errada()
      except:
            escolha_errada()
                


def main():
   os.system('cls')
   exibir_nome()
   exibir_opcoes()
   selecionar_opcoes()

   

if __name__ == '__main__':
  main()