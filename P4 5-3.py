

def binario (numero) :
    
    binario= ""
    while numero> 0:
        binario = str (numero%2)+ binario
        numero= numero//2
    print("El valor binario es:",binario)

    
def octal (numero):
    
    octal=""
    while numero> 0:
        octal = str (numero%8)+ octal
        numero= numero//8
    return octal
    
def hexadecimal (numero):
    
    hexadecimal= ""
    while numero> 0:
        hexadecimal = convertir(numero%16)+ octal
        numero= numero//16
    return hexadecimal

def convertir(numero):
    if numero ==10
        return "A"

    elif numero ==11:
        return "B"
    elif numero == 12:
        return "C"
    elif numero == 13:
        return "D"
    elif numero == 14:
        return "E"
    elif numero == 15:
        return "F"
    elif numero

def principal ():
    while true:
        valor = int(input("Ingrese el valor que de desea convertir:"))
        print("1.De decimal a binario \n2.De decimal a octal \n3.De decimal a Hexadecimal")
        opcion = int(input("Ingrese la opcion que desea")

    if opcion == 1:
        print("Binario")
        
        return
    elif opcion == 2:
        print("Octal")

    elif opcion == 3:
    print("Hexadecimal")
principal()
    

