# Módulo número aleatorio
from random import randrange

# lista del tablero (compresión de listas)
tablero = [[columna + 1 + fila * 3 for columna in range(3)] for fila in range(3)]
# Lista vacía, se llena en la función LugaresVacios()
libres = []
# Contador para salir del bucle secundario
numero_de_jugada = 0
# variable que se modifica en la función ganador()
# para usarla como bandera, si pasa a "x" o "o", se
# sale del bucle secundario
ganador = "ninguno"

# La función acepta un parámetro el cual contiene el estado actual del tablero
# y lo muestra en la consola.
# ASI LO HABIA HECHO:
def mostrarTablero(tablero):
    print("+-------"*3,end=("+\n"))
    print("|       "*3,end=("|\n"))
    print("|   "+str(tablero[0][0])+"   "+"|   "+str(tablero[0][1])+"   "+"|   "+str(tablero[0][2])+"   ",end=("|\n"))
    print("|       "*3,end=("|\n"))
    print("+-------"*3,end=("+\n"))
    print("|       "*3,end=("|\n"))
    print("|   "+str(tablero[1][0])+"   "+"|   "+str(tablero[1][1])+"   "+"|   "+str(tablero[1][2])+"   ",end=("|\n"))
    print("|       "*3,end=("|\n"))
    print("+-------"*3,end=("+\n"))
    print("|       "*3,end=("|\n"))
    print("|   "+str(tablero[2][0])+"   "+"|   "+str(tablero[2][1])+"   "+"|   "+str(tablero[2][2])+"   ",end=("|\n"))
    print("|       "*3,end=("|\n"))
    print("+-------"*3,end=("+\n"))
# ESTA ES LA RESOLUCION PASADA EN CLASE 13
# es la que voy a usar
def mostrar_tablero(tablero):
    print("+-------" * 3,"+", sep="")
    for fila in range(3):
        print("|       " * 3,"|", sep="")
        for columna in range(3):
            print("|   " + str(tablero[fila][columna]) + "   ", end="")
        print("|")
        print("|       " * 3,"|", sep="")
        print("+-------" * 3,"+", sep="")

# Primer movimiento de la maquina en el centro
def primer_jugada_maquina(tablero):
    print("La primer jugada es de la máquina, su lugar va a ser el centro")
    tablero[1][1] = "X"
    mostrar_tablero(tablero)

# printear
titulo = """
                                      +---------------------+
                                      |  *****************  |
                                      |  *   TA-TE-TI    *  |
                                      |  *****************  |
                                      +---------------------+
    """

gano_x = """ 
                                      ***********************
                                      ******** GANÓ *********
                                      ********* LA **********
                                      ******* MÁQUINA! ******
                                      ***********************
       """

gano_o = """
                                            #
                                        #           *       #
                                                * * * * *               #
                                            * * * * * * * *             
                                    #      *   FELICIDADES!!! *  #
                                        *       Has ganado      *
                                    #   * * * * * * * * * * * * *    #  
                                                #
                                        #                         #
                                                    #
       """

empate = """
                                      '''''''''''''''''''''''
                                      ''''''  EMPATE  '''''''
                                      '''''''''''''''''''''''             

                                   
        """ 

saludo = """  
                                         *   *   *   *
                                      *                 *
                                         Hasta luego!.      
                                      *                 *
                                         *   *   *   *
        
        """ 
  
# La función examina el tablero y construye una lista de todos los cuadros vacíos.
# La lista esta compuesta por tuplas, cada tupla es un par de números que indican 
# la fila y columna.
def LugaresVacios(tablero): 
    # Coloqué el método porq, al llamar a la función, 
    # agregaba a la ya existente, de esta manera, cada 
    #vez q se llama a la función, se crea una lista de cero.
    libres.clear() 
    for fila in range(len(tablero)):
        for col in range(len(tablero)):
            if tablero[fila][col] != "X" and tablero[fila][col] != "O":
                libres.append((fila,col))   
    
# La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
# verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
def SiguienteMovimiento(tablero):
    cuenta = len(libres)
    if cuenta > 0:# Lista vacía o no
        # Bucle al que se entra si el numero ingresado esta dentro de las posibilidades
        # que tiene el tablero (1 a 9), contando el movimiento fijo de
        # "x" en el centro.
        while True:
            # Excepciones, para q el programa no se detenga si el usuario no ingresa 
            # un entero (float, string)
            try: 
                movimiento = int(input("Selecciona tu movimiento: "))
                if movimiento < 0 or movimiento > 9: 
                    print("Posición incorrecta, elija numero del 1 al 9.")    
                elif movimiento > 0 and movimiento < 10: # Si está en el rango, dependiendo del número ingresado, es la posición
                    if movimiento == 1 and (0,0) in libres:
                        tablero [0][0] = "O"
                        break
                    elif movimiento == 2 and (0,1) in libres:
                        tablero [0][1] = "O"
                        break
                    elif movimiento == 3 and (0,2) in libres:
                        tablero [0][2] = "O"
                        break
                    elif movimiento == 4 and (1,0) in libres:
                        tablero [1][0] = "O"
                        break
                    elif movimiento == 5 and (1,1) in libres:
                        tablero [1][1] = "O"
                        break
                    elif movimiento == 6 and (1,2) in libres:
                        tablero [1][2] = "O"
                        break
                    elif movimiento == 7 and (2,0) in libres:
                        tablero [2][0] = "O"
                        break
                    elif movimiento == 8 and (2,1) in libres:
                        tablero [2][1] = "O"
                        break
                    elif movimiento == 9 and (2,2) in libres:
                        tablero [2][2] = "O"
                        break
                    else:
                        print("Posición ocupada, elija otra.")  
            # Mensaje que va a leer el usuario ante un ValueError                
            except:
                print("Debes ingresar un número entero")
       
# La función dibuja el movimiento de la máquina y actualiza el tablero
# Esta en el colab, como guía
def MovimientoMaquina(tablero): 
  print("Juega la máquina")
  cuenta = len(libres)                            
  if cuenta > 0: # Si la lista NO está vacia, elegir un lugar para que juegue la máquina 'X'
    lugar_maquina = randrange(cuenta)
    fila, col = libres[lugar_maquina]
    tablero[fila][col] = 'X'

# La función analiza el estatus del tablero para verificar si
# el jugador que utiliza las 'O's o las 'X's ha ganado el juego.   
def Ganador(tablero):
    global ganador # Para que la variable pueda ser modificada desde la función
    if tablero[0][0] == "X" and tablero[0][1] == "X" and tablero[0][2] == "X":
        ganador = "X" #Actúa como coto en el bucle secundario
        print(gano_x)
    elif tablero[1][0] == "X"and tablero[1][1] == "X" and tablero[1][2] == "X":
        ganador = "X"  #Actúa como coto en el bucle secundario
        print(gano_x)
    elif tablero[2][0] == "X"and tablero[2][1] == "X" and tablero[2][2] == "X":
        ganador = "X"  #Actúa como coto en el bucle secundario
        print(gano_x)
    elif tablero[0][0] == "X"and tablero[1][0] == "X" and tablero[2][0] == "X":
        ganador = "X"  #Actúa como coto en el bucle secundario
        print(gano_x)
    elif tablero[0][1] == "X"and tablero[1][1] == "X" and tablero[2][1] == "X":
        ganador = "X"  #Actúa como coto en el bucle secundario
        print(gano_x)
    elif tablero[0][2] == "X"and tablero[1][2] == "X" and tablero[2][2] == "X":
        ganador = "X"  #Actúa como coto en el bucle secundario
        print(gano_x)
    elif tablero[0][0] == "X"and tablero[1][1] == "X" and tablero[2][2] == "X":
        ganador = "X"  #Actúa como coto en el bucle secundario
        print(gano_x)
    elif tablero[0][2] == "X"and tablero[1][1] == "X" and tablero[2][0] == "X":
        ganador = "X"  #Actúa como coto en el bucle secundario
        print(gano_x)
    elif tablero[0][0] == "O" and tablero[0][1] == "O" and tablero[0][2] == "O":
        ganador = "O"  #Actúa como coto en el bucle secundario
        print(gano_o)
    elif tablero[1][0] == "O"and tablero[1][1] == "O" and tablero[1][2] == "O":
        ganador = "O"  #Actúa como coto en el bucle secundario
        print(gano_o)
    elif tablero[2][0] == "O"and tablero[2][1] == "O" and tablero[2][2] == "O":
        ganador = "O"  #Actúa como coto en el bucle secundario
        print(gano_o)
    elif tablero[0][0] == "O"and tablero[1][0] == "O" and tablero[2][0] == "O":
        ganador = "O"  #Actúa como coto en el bucle secundario
        print(gano_o)
    elif tablero[0][1] == "O"and tablero[1][1] == "O" and tablero[2][1] == "O":
        ganador = "O"  #Actúa como coto en el bucle secundario
        print(gano_o)
    elif tablero[0][2] == "O"and tablero[1][2] == "O" and tablero[2][2] == "O":
        ganador = "O"  #Actúa como coto en el bucle secundario
        print(gano_o)
    elif tablero[0][0] == "O"and tablero[1][1] == "O" and tablero[2][2] == "O":
        ganador = "O"  #Actúa como coto en el bucle secundario
        print(gano_o)
    elif tablero[0][2] == "O"and tablero[1][1] == "O" and tablero[2][0] == "O":
        ganador = "O"  #Actúa como coto en el bucle secundario
        print(gano_o)

# Función global para usuario
# La idea es tener una función que llame a todas las 
# funciones necesarias, y asi lograr, en el prógrama,
# un código mas corto
def funcion_global_usuario():
    LugaresVacios(tablero)
    SiguienteMovimiento(tablero)
    mostrar_tablero(tablero)
    Ganador(tablero)
# Función global para la máquina
def funcion_global_maquina():
    LugaresVacios(tablero)
    MovimientoMaquina(tablero)
    mostrar_tablero(tablero)
    Ganador(tablero)


print(titulo)
# Nombre de usuario para personalizar el juego
nombre = input("Ingrese su nombre: ")
# Presentación
print(f"Bienvenido {nombre} al juego de TA-TE-TI.")
print("Seguramente ya conoces las reglas.")
# Bucle gral, para entrar al juego o salir
while True:
    jugar = input("Si quieres comenzar el juego escribe 'si', de lo contrario 'no': ").lower() # Selecciona jugar o salir
    print("\n")                                                                                #Por si el ingreso no es en minúsculas
    # Seleccionó si
    if jugar == "si":
        tablero = [[1,2,3],[4,5,6],[7,8,9]] # NO SE SI HAY UNA MANERE MEJOR DE HACERLO:
        libres = []                         # la idea es q, cuando termine el juego, y
        numero_de_jugada = 0                # el programa pregunte "Si quieres comenzar si/no.."
        ganador = "ninguno"                 #se reinicen los valores para poder jugar otra vez.
        print("El tablero esta enumerado del 1 al 9, para que selecciones tu posición.")
        mostrar_tablero(tablero)
        print("\n")
        # La idea de este input es darle el control del tiempo de
        # ejecución al usuario
        seguir = input("Presione enter para continuar: ")
        print("\n")
        primer_jugada_maquina(tablero)
        print("\n")
        # Bucle secundario para permanecer en el juego miestras puedan realizarse movimientos
        while numero_de_jugada < 4: 
            numero_de_jugada +=1 # Contador de jugadas, cuando llega a 4 termina el bucle
            if ganador == "X" or ganador == "O": # Salir del bucle si ya hay ganador
                break
            funcion_global_usuario()
            print("\n")
            if ganador == "X" or ganador == "O": # Salir del bucle si ya hay ganador
                break
            # La idea de este input es darle el control del tiempo de
            # ejecución al usuario
            seguir = input("Presione enter para continuar: ")
            print("\n")
            funcion_global_maquina()
            if ganador == "X" or ganador == "O": # Salir del bucle si ya hay ganador
                break
            print("\n") 
        else: # Si no hay ganador y el contador es > 4, empate
            print(empate)       
    elif jugar == "no": # Seleccionó no jugar, sale del juego
        print(saludo)
        break
    else: # Seleccionó otra cosa q si/no (letra, numero, otra palabra)
        print("Respuesta incorecta.") # Vuelve para ingresar una opción correcta







    



