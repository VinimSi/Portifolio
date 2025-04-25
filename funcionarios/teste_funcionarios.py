from funcionario import Funcionario

funcionario = Funcionario("Matheus","matheus@tank.com.br")

funcionario.cadastro_hora("Jan",300)
funcionario.cadastro_hora("Fev",200)
funcionario.cadastro_salario_hora("Jan",30)
funcionario.cadastro_salario_hora("Fev",30)
print(funcionario.nome)
print(funcionario.calcula_salario("Jan"))
print(funcionario.calcula_salario("Fev"))