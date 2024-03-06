# 1. Elabore un programa en Python que permita convertir de pesos a dólares, de
# pesos a euros, de euros a pesos, de pesos a yenes. (10 ptos)
# 1 yen = 26.30 pesos
# 1 dólar = 3944 pesos
# 1 euro = 4279 pesos
import tabulate

def pesos_a_dolares ():  
     dolar = 3944
     monto = input("ingrese el monto a convertir:"+"\n>>>")
     montototal = dolar / monto
     print("\nEl monto es de $" + montototal)

def pesos_a_euros ():  
    euro = 4279
    monto = input("ingrese el monto a convertir:"+"\n>>>")
    montototal = euro / monto
    print("\nEl monto es de $" + montototal)

def euros_a_pesos ():  
     euro = 4279
     monto = input("ingrese el monto a convertir:"+"\n>>>")
     montototal = euro * monto
     print("\nEl monto es de $" + montototal)

def pesos_a_yenes ():  
     yen = 26.3
     monto = input(float("ingrese el monto a convertir:"+"\n>>>"))
     montototal = yen / monto
     print("\nEl monto es de $" + montototal)


def convertidor_de_divisas (): 
    titulo = [["Convertidor De Divisas"]]
    print(tabulate(titulo,tablefmt="double_grid"))
    opciones = [["1. pesos a dolares\n"],["2. pesos a euros\n"],["3.euros a pesos\n"],["4.yenes apesos "]]
    print(tabulate(opciones,tablefmt="doublegrid"))
    input("ingrese la opcion\n>>")
    if opciones == "1":
            pesos_a_dolares()        
    elif opciones == "2":
            pesos_a_euros ()
    elif opciones == "3":
            euros_a_pesos()
    elif opciones == "4":
            pesos_a_yenes()
    else: convertidor_de_divisas
    

    

convertidor_de_divisas()