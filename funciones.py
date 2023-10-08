import numpy as np
import random
import os
import time
import variables as va
# import funciones as fu


# Función Inicializar tablero
def inicializar_tablero():
    tablero = np.full((va.size + 2, va.size + 2), '*')
    tablero[1:-1, 1:-1] = ' '
    return(tablero)

# Función disparo
def disparar(x, y, tablero):
    
    if tablero[x, y] == 'O':
        tablero[x, y] = 'X'
        acierto = True
        return(tablero, acierto)
        # print('Acierto')
    elif tablero[x, y] == ' ':
        tablero[x,y] = '~'
        acierto = False
        return(tablero, acierto)
    else:
        acierto = False
        return(tablero, acierto)
        # print('Fallo')


# función disparo aleatorio:
def random_shoot(tablero):
    
    while True:
        x = random.randint(1, va.size)
        y = random.randint(1, va.size)

        if tablero[x, y] == 'X' or tablero[x, y] == '~':
            continue
        elif tablero[x, y] == 'O':
            tablero[x, y] = 'X'
            acierto = True
            return(tablero, acierto)
            # print('Acierto')
        elif tablero[x, y] == ' ':
            tablero[x,y] = '~'
            acierto = False
            return(tablero, acierto)
            # print('Fallo')

# función que genera un barco aleatorio y devuelve coordenadas de origen y orientación
# El barco ocupa 'eslora' posiciones
# Origen aleatorio
# Orientación aleatoria (N, S, E, O)

def generar_b_aleatorio(eslora):
    x = 0
    y = 0
    orien = 'S'
    while True:
        x = random.randint(1, va.size)
        y = random.randint(1, va.size)
        orien = random.choice(['N', 'S', 'E', 'O'])
        if orien == 'N':
            boundary = x - eslora
        elif orien == 'S':
            boundary = x + eslora
        elif orien == 'E':
            boundary = y + eslora
        else:
            boundary = y - eslora
        if 1 < boundary < va.size:
            break
    return(x, y, eslora, orien)
        
# función que comprueba estado de las celdas en que se va a colocar el barco
def check_feasibility(x, y, eslora, orien, tablero):

    if orien == 'N':
        for k in range(x - eslora, x + 2):
            for l in range (y - 1, y + 2):
                if tablero[k, l] == 'O':
                    return False
        return True

    elif orien == 'S':
        for k in range(x -  1, x + 1 + eslora):
            for l in range (y - 1, y + 2):
                if tablero[k, l] == 'O':
                    return False
        return True

    elif orien == 'E':
        for k in range(x - 1, x + 2):
            for l in range (y - 1, y + 1 + eslora):
                if tablero[k, l] == 'O':
                    return False
        return True

    else:
        for k in range(x - 1, x + 2):
            for l in range (y - eslora, y + 2):
                if tablero[k, l] == 'O':
                    return False
        return True


# función que coloca un barco en el tablero con coordenadas x, y, eslora y orientación
def coloca_barco(x, y, eslora, orien, tablero):
    if orien == 'N':
        tablero[x - eslora + 1 : x + 1, y] = 'O'
        return tablero
    
    elif orien == 'S':
        tablero[x : x + eslora, y] = 'O'
        return tablero
    
    elif orien == 'E':
        tablero[x, y : y + eslora] = 'O'
        return tablero

    elif orien == 'O':
        tablero[x, y - eslora + 1 : y + 1] = 'O'
        return tablero
    

# función que devuelve un tablero con barcos aleatorios
def poblar_tablero():
    t = 0
    tablero = inicializar_tablero()
    while t < 1:
        t += 1
        e = 0
        c = 0

        for u in range(len(va.barcos)):
            e = 0
            c = 0
            num_barcos = va.barcos[u][0]
            eslora = va.barcos[u][1]
            print(num_barcos, eslora)
            
            while e < num_barcos:

                b_aleatorio = generar_b_aleatorio(eslora)
                                
                if check_feasibility(b_aleatorio[0], b_aleatorio[1], eslora, b_aleatorio[3], tablero):
                    coloca_barco(b_aleatorio[0], b_aleatorio[1], eslora, b_aleatorio[3], tablero)
                    e += 1
                else:
                    print(b_aleatorio)
                    c += 1

                if c > 500:
                    print('Más de 500 iteraciones')
                    break
                
                if e == va.barcos[u][0]:
                    break
    return tablero