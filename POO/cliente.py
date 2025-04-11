class Cliente:
    def __init__(self,n,fone):
        self.nome = n
        self._telefone = fone
    #metodo get
    def get_nome(self):
        return self.nome #lembrando que quando coloco o '_' atras da variavel ela se torna privada
    #metodo set
    def set_nome(self):
        self._nome = nome