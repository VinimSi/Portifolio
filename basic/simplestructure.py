a = input("Valor de A: ")
b = input("Valor de B: ")

if(a>b):
    aux=a;
    a=b;
    b=aux;
print("Valor atual de A: ", a)
print("Valor atual de B: ", b)