
def lernotas():
    n=float(input("Digite uma nota para o aluno merda: "))
    return n

def resultado(n1,n2):
    media=(n1+n2)/2
    print(f"Nota 1: {n1}")
    print(f"Nota 2: {n2}")
    print(f"Media: {media} \nResultado: ", end="")
    if media >= 7:
        print("Aprovado!")
    else:
        print("Rodou!")

a = lernotas()
b = lernotas()
resultado(a,b)