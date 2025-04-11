class Main:
    pass

print("Bem vindo ao banco santo andreh")
from cliente import Cliente
from conta import Conta

c1 = Cliente ("Vini bosta","4002-8922")
conta=Conta(c1.get_nome(),6590,10)
conta.deposita(1000)
conta.saque(50)
conta.extrato()
#print("Nome: ",conta.titular,"\nNumero: ",conta.numero,"\nSaldo: ",conta.saldo)