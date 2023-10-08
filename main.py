import numpy as np
import random
import os
import time
import variables as va
import funciones as fu


# inicializa tableros
# tab_user = fu.inicializar_tablero()
# tab_comp = fu.inicializar_tablero()
# tab_shoo = fu.inicializar_tablero()

tab_user = fu.poblar_tablero()
tab_comp = fu.poblar_tablero()

# bucle principal
i = 0
while True:
    i += 1
 
    # dispara el user manualmente
    while True:
        tablero = tab_comp
        tab_shoo = tab_comp
        tab_shoo = np.where(tab_shoo == 'O', ' ', tab_shoo)
        os.system('clear')
        print(tab_user, 'Tus barcos')
        print('\n')
        print(tab_shoo, 'Tus disparos')
        x = int(input('Introduce fila de disparo: '))
        y = int(input('Introduce columna de disparo: '))

        disparo = fu.disparar(x, y, tablero)
        acierto = disparo[1]
        
        if acierto:
            continue
        if acierto == False:
            break

   
    tab_comp = tablero
    tab_shoo = tab_comp
    tab_shoo = np.where(tab_shoo == 'O', ' ', tab_shoo)

 
    # comprobación de la flota enemiga
    barco_comp = np.count_nonzero(tab_comp == 'O')

    if barco_comp == 0:
        os.system('clear')
        print('Has ganado en', i, 'movimientos')
        print('\n')
        print(tab_user, 'Tu flota')
        print('\n')
        print(tab_comp, 'Tu enemigo')
        break


    # dispara la máquina de forma aleatoria
    while True:
        tablero = tab_user
        disparo = fu.random_shoot(tablero)
        acierto = disparo[1]
        
        if acierto:
            continue
        if acierto == False:
            break
    
    tab_user = tablero
    
    # comprobación de la flota del user
    barco_user = np.count_nonzero(tab_user == 'O')

    if barco_user == 0:
        os.system('clear')
        print('Has perdido en ', i, 'movimientos')
        print('\n')
        print(tab_user, 'Tu flota')
        print('\n')
        print(tab_comp, 'Tu enemigo')
        break
    
    os.system('clear')
    print('Movimiento ', i)
    # print('\n')
    print(tab_user, 'Tus barcos')
    print('\n')
    print(tab_shoo, 'Tus disparos')
    time.sleep(1)