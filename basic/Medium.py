#variaveis
notaA = float(input("Nota 1: "))
notaB = float(input("Nota 2: "))

#calculando
mediafinal = (notaA+notaB)/2

#verificação
if mediafinal >= 7.0:
    print("Media: %.1f - Aprovado"% mediafinal)
else:
    print("Media: %.1f - Reprovado"% mediafinal)