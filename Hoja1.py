print("-------EJERCICIO 2 -------")

b=int(input("INGRESE LA ALTURA DEL TRIANGULO QUE DESE TENER"))
for i in range(b):
    for j in range(i+1):
        print("*", end="")
    print("")



print("-------EJERCICIO 2-------")

a=int(input("INGRESE UN NUMERO: "))
def evaluar(a):
    contador=0
    resultado=True
    for i in range(1,a+1):
        if(a%i==0):
            contador+=1
            if(contador>2):
                resultado=False
                break
    return resultado
if(evaluar(a)==True):
    print("Este numero es primo")
else:
        print("Este numero no es primo")


