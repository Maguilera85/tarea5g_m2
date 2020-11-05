
import random
import time



''' Coordenadas del tablero. Inicia vacio '''

theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)


''' Se le asigna una función al tablero para ser llamado facilmente '''

def printBoard(board):
    # Este es el tablero
    vacio = ["   "]
    ancho_pantalla = 80 
    ancho_texto = len(vacio) 
    ancho_caja = ancho_texto +  5
    margen_izquierdo  = (ancho_pantalla -ancho_caja) // 2
# superior
    print(' ' * margen_izquierdo + ' ' + ' ' * (ancho_caja -2) + ' +' + ' ' * (ancho_caja -2) + ' +' + ' ' * (ancho_caja -2) + '')
    print(' ' * margen_izquierdo + '   ' + ' ' * ancho_texto + '  |' + ' ' * ancho_texto + '    |' + ' ' * ancho_texto + '    ')
    print(' ' * margen_izquierdo , ' ' , theBoard['7'] , ' | ' , theBoard['8'] , ' | ' , theBoard['9'] , '  ')
    print(' ' * margen_izquierdo + '   ' + ' ' * ancho_texto + '  |' + ' ' * ancho_texto + '    |' + ' ' * ancho_texto + '    ')
    print(' ' * margen_izquierdo + ' +' + '-' * (ancho_caja -2) + '+' + '-' * (ancho_caja -2) + '-+'+ '-' * (ancho_caja -2) + '+')
# medio
    print(' ' * margen_izquierdo + '   ' + ' ' * ancho_texto + '  |' + ' ' * ancho_texto + '    |' + ' ' * ancho_texto + '    ')
    print(' ' * margen_izquierdo + '  ' , theBoard['4'] , ' | ' , theBoard['5'] , ' | ' , theBoard['6'] , '  ')
    print(' ' * margen_izquierdo + '   ' + ' ' * ancho_texto + '  |' + ' ' * ancho_texto + '    |' + ' ' * ancho_texto + '    ')
    print(' ' * margen_izquierdo + ' +' + '-' * (ancho_caja -2) + '+' + '-' * (ancho_caja -2) + '-+'+ '-' * (ancho_caja -2) + '+')
# inferior
    print(' ' * margen_izquierdo + '   ' + ' ' * ancho_texto + '  |' + ' ' * ancho_texto + '    |' + ' ' * ancho_texto + '    ')
    print(' ' * margen_izquierdo , ' ' , theBoard['1'] , ' | ' , theBoard['2'] , ' | ' , theBoard['3'] , '  ')
    print(' ' * margen_izquierdo + '   ' + ' ' * ancho_texto + '  |' + ' ' * ancho_texto + '    |' + ' ' * ancho_texto + '    ')
    print(' ' * margen_izquierdo + ' ' + ' ' * (ancho_caja -2) + ' +' + ' ' * (ancho_caja -2) + ' +' + ' ' * (ancho_caja -2) + '')


# El juego y lógica
def game():

    turn = 'X'
    count = 0
    

    for _i in range(10):
        printBoard(theBoard)
        print("Es tu turno," + turn + ".¿Dónde deseas mover?")

        move = input()        

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("\nEsta posición ya se encuentra ocupada\nSelecciona una opción vacía")
            continue

        # Aca se busca un ganador, luego de las primeras 5 jugadas. Antes de eso no hay ganador. 
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # parte superior del tablero
                printBoard(theBoard)
                print("\nFin del juego.\n")                
                print(" **** " +turn + " ganó. ****")                
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # parte medio del tablero
                printBoard(theBoard)
                print("\nFin del juego.\n")                
                print(" **** " +turn + " ganó. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # parte inferior del tablero
                printBoard(theBoard)
                print("\nFin del juego.\n")                
                print(" **** " +turn + " ganó. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # columna izquierda
                printBoard(theBoard)
                print("\nFin del juego.\n")                
                print(" **** " +turn + " ganó. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # columna medio
                printBoard(theBoard)
                print("\nFin del juego.\n")                
                print(" **** " +turn + " ganó. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # columna derecha
                printBoard(theBoard)
                print("\nFin del juego.\n")                
                print(" **** " +turn + " ganó. ****")
                break 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal superior izquierda a inferior derecha
                printBoard(theBoard)
                print("\nFin del juego.\n")                
                print(" **** " +turn + " ganó. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal inferior izquierda a superior derecha
                printBoard(theBoard)
                print("\nFin del juego.\n")                
                print(" **** " +turn + " ganó. ****")
                break 

        # Si el tablero esta completo y no hay ganador se declara un empate.
        if count == 9:
            print("\nFin del juego.\n")                
            print("Es un empate")

        # Asignamos el siguiente turno.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # Pregunta al usuario si quiere volver a jugar.
    restart = input("¿Quieres volver a jugar?(S/N)")
    if restart == "s" or restart == "S":  
        for key in board_keys:
            theBoard[key] = " "

        game()

if __name__ == "__main__":
    game()