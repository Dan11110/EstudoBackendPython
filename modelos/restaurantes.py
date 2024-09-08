class Restaurantes:
    def __init__(self, nome, categoria, cidade, bairro, rua):
        self.nome = nome
        self.categoria = categoria
        self.cidade = cidade
        self.bairro = bairro
        self.rua = rua
        self.ativo = False

    def __str__(self):
        return f"\nNome: {self.nome}\nCategoria: {self.categoria}\nCidade: {self.cidade}\nBairro: {self.bairro}\nRua: {self.rua}\n"

restaurante_novo = Restaurantes("Teste", "Pizzaria", "Rio de janeiro", "Cachambi", "Chaves Pinheiro")
print(restaurante_novo)