#Funcion con retorno
saludo =""
def saludarRetorno():
    print ("1.Saludo personalizado \n2.Saludo generico")
    opcion= int(input("Seleccione una opcion:"))
    if opcion==1:
        nombre= input("Ingrese su nombre:")
        saludo="!Hola",nombre,"bienvenido a pythom!"
    else:
        saludo = "Hola usuario, bienvenido a python!"
        
        
    return saludo
print(saludarRetorno())
print(saludo)
