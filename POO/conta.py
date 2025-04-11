class Conta:
    def __init__(self,titular,numero,saldo):
        self._saldo=0.0
        self._numero=numero
        self._titular=titular

    @property #Basicamente, a função Property permite que você declare uma função para obter o valor de um atributo.
    #metodo get
    def saldo(self):
        return self._saldo

    @saldo.setter
    #metodo set
    def saldo(self, saldo):
        if (saldo < 0):
            print("saldo nao pode ser negativo")
        else:
            self._saldo = saldo

    #metodo deposito/pix
    def deposita(self, valor):
        self.saldo+=valor
          
    #metodo saque
    def saque(self, valor):
        if (self.saldo>=valor):
            self.saldo-=valor
            print("Saque realizado com sucesso")
        else:
            print("Saldo insuficiente pobre de merda")

    #metodo extrato(de toumate kkj)
    def extrato(self):
        print("Cliente: ",self._titular,"\nSaldo atual: ",self.saldo)