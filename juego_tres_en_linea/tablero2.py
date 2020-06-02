
import os
import random
import time
def inicio_juego():
    print("****** bienbenidos**")
    time.sleep(1)
    while True:
        ficha = input("Seleccine ficha: x/o \n")
        ficha = ficha.upper()
        if ficha=="x":
            humano="x"
            ordenador="o"
            break
        elif ficha=="o":
            humano="o"
            ordenador="x"
        else:
            print("favor introducir una ficha")
            return (humano,ordenador)
          
def tablero():
    print("tres en linea")
print("{0}------------------{}-------------------{0}".format(matriz[0],matriz[1],matriz[2]))
print("|                    |                      |")
print("|    {0}-------------{0}-------------{x}    |".format(matriz[4],matriz[5],matriz[6]))
print("|    |               |                |     |"
print("|    |      {}-------{x}------{}      |     |".format(matriz[7],matriz[8],matriz[9]))
print("|    |     |                    |     |     |")
print("|    |     |                    |     |     |")
print("{}---{0}--{x}                  {0}----{}---{8}".format(matriz[10],matriz[11],matriz[12]))
print("|    |     |                    |     |     |")
print("|    |     |                    |     |     |")
print("|    |     {}--------{0}-------{}     |     |".format(matriz[13],matriz[14],matriz[15]))
print("|    |               |                |     |")
print("|    {x}-------------{x}-------------{x}    |".format(matriz[16],matriz[17],matriz[18]))
print("|                    |                      |")
print("{x}------------------{}-------------------{x}".format(matriz[19],matriz[20],matriz[21]))
   
def empate(matriz):
    empate=True
    i=0
    while(empate==True and i<9):
        if matriz[i]==" ":
            empate=False
            i=i+1
            return empate

def victoria(matriz):
    if (matriz[0]==matriz[1]==matriz[2]!=" " or matriz[3]==matriz[4]==matriz[5]!=" " or matriz[6]==matriz[7]==matriz[8]!=" "
        or matriz[0]==matriz[3]==matriz[6]!=" " or matriz[1]==matriz[4]==matriz[7]!=" " or matriz[2]==matriz[5]==matriz[8]!=" " or
        matriz[0]==matriz[4]==matriz[8]!=" " or matriz[2]==matriz[4]==matriz[6]!=" "):
    return True
    else:
        return False

#movimientos
def movimiento_jugador():
    while True:
        posiciones=[0,1,2,3,4,5,6,7,8]
        casilla=int(input("seleccione casilla: "))
        if casilla not in posiciones:
            print("casilla no disponoble")
        else:
            if matriz[casilla-1]==" ":
                matriz[casilla-1]==humano
                break
            else:
                print("casilla no disponoble")
def movimiento_ordenador():
    posiciones=[0,1,2,3,4,5,6,7,8]
        casilla=9
        parar=False

        for i in posiciones:
            copia=list(matriz)
            if copia[i]==" ":
                copia[i]=ordenador
                if victoria(copia)==True:
                    casilla=i

            if casilla==9:
                for j in posiciones:
                    if copia[j]==" ":
                        copia[j]=humano
                    if victoria(copia)==True:
                        casilla=j

             if casilla==9:
                 while(not parar):
                     casilla=random.randint(0,8)
                     if matriz[casilla]=" ":
                         parar=True
            matriz[casilla]=ordenador
#desarrollo de partida
while True:
    matriz=[" "]*9
    os.system("cls")
    humano,ordenador=inicio_juego()
    partida=True
    ganador=0

    while partida:
        ganador=ganador+1
        os.system("cls")
        tablero()

        if victoria(matriz):
            if ganador%2==0:
                print("**gana el jugador**")
                print("**fin del juego**")
                print("\nReiniciando...")
                time.sleep(5)
                partida=False
        else:
            print("**gana el ordenador**")
                print("**fin del juego**")
                print("\nReiniciando...")
                time.sleep(5)
                partida=False
        elif empate(matriz):
            print("**empate**")
                print("**fin del juego**")
                print("\nReiniciando...")
                time.sleep(5)
                partida=False
        elif ganador%2==0:
            print("el ordenador esta pensando")
            time.sleep(5)
            movimiento_ordenador()
            else:
                movimiento_jugador()



            