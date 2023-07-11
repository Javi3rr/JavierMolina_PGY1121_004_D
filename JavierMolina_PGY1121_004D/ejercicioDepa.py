import os 
import numpy as np
import funcionDepa as fa
depa=np.empty([10,4],type(int))
fa.llenar(depa)
op=0
ruts=[]
comprar=0

while(op!=5):
    os.system("cls")
    print("Casa feliz")
    print("1-Comprar departamento")
    print("2-Mostar departamentos disponibles")
    print("3-Ver listado de compradores")
    print("4-Mostar ganancias totales")
    print("5-Salir")
    op=fa.valiaOp()

    if(op==1):
        fa.mostraDisponibles(depa)
        os.system("pause")
        fa.comprar()
        fa.ruru()
        print("Su compra se ha realizado correctamente!!")
        os.system("pause")
    if(op==2):
        
        fa.mostraDisponibles(depa)
        fa.disponible(depa,comprar)
        fa.comprarPasaje(depa,comprar)
        os.system("pause")
        
    







    if(op==5):
        fa.valiop5()
        os.system("pause")

        