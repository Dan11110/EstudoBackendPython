class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria, cidade, bairro, rua):
        self.nome = nome
        self.categoria = categoria
        self.cidade = cidade
        self.bairro = bairro
        self.rua = rua
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"\nNome: {self.nome}\nCategoria: {self.categoria}\nCidade: {self.cidade}\nBairro: {self.bairro}\nRua: {self.rua}\n"
    
    def listar_restaurantes():
            for restaurante in Restaurante.restaurantes:
                print(restaurante)

restaurante_novo = Restaurante("Teste", "Pizzaria", "Rio de janeiro", "Cachambi", "Chaves Pinheiro")
restaurante_novo = Restaurante("Teste2", "Pizzaria Nova", "Rio de janeiro", "Cachambi", "Chaves Pinheiro")

