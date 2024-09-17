class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria, cidade, bairro, rua):
        self._nome = nome.title()
        self._categoria = categoria
        self._cidade = cidade
        self._bairro = bairro
        self._rua = rua
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"\nNome: {self._nome}\nCategoria: {self._categoria}\nCidade: {self._cidade}\nBairro: {self._bairro}\nRua: {self._rua}\nStatus: {self.ativo}\n"
    
    def listar_restaurantes():
            for restaurante in Restaurante.restaurantes:
                print(restaurante)

    @property
    def ativo(self):
         return "✅" if self._ativo else "❎"

restaurante_novo = Restaurante("Teste", "Pizzaria", "Rio de janeiro", "Cachambi", "Chaves Pinheiro")
restaurante_novo = Restaurante("Teste2", "Pizzaria Nova", "Rio de janeiro", "Cachambi", "Chaves Pinheiro")
