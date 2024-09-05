import os

restaurantes = ["McBurguer", "Donalds King", "Totts", "Restaurante de regatas Vasco da Gama"]

def encerrar_app():
  limpar_exibir("programa encerrado")

def listar_pedidos():
  limpar_exibir("Lista de pedidos de restaurantes cadastrados no aplicativo:\n")
  for restaurante in restaurantes:
      print(f"{restaurante}\n")
  voltar()

def cadastrar_restaurante():
  limpar_exibir("Bem vindo ao cadastro de novos restaurantes\n")
  restaurante_novo = input("Digite o nome do restaurante: ")
  restaurantes.append(restaurante_novo)
  input(f"Restaurante {restaurante_novo} adicionado com sucesso!!!")
  voltar()

def escolha_errada():
  input("Opção incorreta, digite uma tecla para voltar ao menu principal")
  voltar()

def voltar():
     input("\nAperte um botão para voltar ao menu")
     main()

#Função para limpar tela e exibir mensagem
def limpar_exibir(texto):
     os.system("cls")
     input(texto)
     
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
   os.system("cls")
   exibir_nome()
   exibir_opcoes()
   selecionar_opcoes()

if __name__ == "__main__":
  main()