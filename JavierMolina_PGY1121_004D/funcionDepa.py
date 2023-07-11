import os 
import numpy as np

def llenar(depa):
    p=1
    for i in range(10):
        for j in  range(4):
            depa[i,j]=p
            p+=1

def valiaOp():
    po=0
    while(True):
        try:
            po=int(input("     Elija opcion:  "))
            if(po>=1 and po<=5):
                break
            else:
                print("Debe ingresar una opcion entre 1 y 5 ")
        except ValueError:
            print("Debe ser un numero entero")
    return po


def mostraDisponibles(depa):
    os.system("cls")
    p=1
    print(       """                    TIPO 
         
         A       B       C      D""")
    for i in range (10):
        print("\n")
        for j in range(4):
            if(j==1):
                print("\t",depa[i,j], end=" ")
            else:
                print("\t",depa[i,j], end=" ")
    print("\n\n")

def comprar():
    os.system("cls")
    pa=0
    while(True):
        try:
            com=int(input("Elija departamento a comprar de 1-40: "))
            if(com>=1 and com<=40):
                break
            else:
                print("Error, ingrese departamento mostrado ")
        except ValueError:
            print("Debe ingresar un numero entero")
    return com

def ruru():
    while(True):
        try:
            rut=int(input("Ingrese rut minimo 8 digitos: "))
            if(rut<9999999):
                print("        Debe tener minimo 8 digitos")
            else:
                break
        except ValueError:
            print("Debe ser un numero entero")



def comprarPasaje(depa,comprar):
    for i in range(10):
        for j in range(4):
            if (depa[i,j]==comprar):
                depa[i,j]=0          
                if i==1:
                    pago=3800
                elif i==2:
                    pago=3000
                elif i==3:
                    pago=2800
                elif i==4:
                    pago=3500
    return pago


def valiop5():
    print("""       Gracias por comprar
            Javier Molina 11/7/2023""")
