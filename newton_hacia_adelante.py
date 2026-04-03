import numpy as np
from math import factorial

#construi la tabla para los datos#
def build_table(y_data):
    n = len(y_data)
    table = np.zeros((n, n))
    table[:, 0] = y_data
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = table[i + 1][j - 1] - table[i][j - 1]
    return table

def newton_adelante(x_data, y_data, x):
    n = len(x_data)
    h = round(x_data[1] - x_data[0], 10)
    for i in range(1, n - 1):
        if not np.isclose(x_data[i + 1] - x_data[i], h, rtol=1e-5):
            print('Los puntos no estan equiespaciados')
            break

        table = build_table(y_data)

#poner las letras a la tabla como en la calculadora la memoria ps#
        letters =[chr(65 + i) for i in range(26)]
        letters_idx = 0
        label_matrix = np.full((n, n), '', dtype=object)
        for j in range(1, n):
            for i in range(n - j):
                label_matrix[i][j] = letters[letters_idx]
            letters_idx += 1
    
    #imprimi la tabla ni perra idea como se ve#
    print('\n' + '=' * 70)
    print('Tabla de diferencias')
    print('=' * 70)
    print(f' {'i':<4} {'xi':<10} {'D0yi':<16}', end='')
    for k in range(1, n):
        print(f'{'D' + str(k) + 'yi':<18}', end='')
    print()
    print('  ' + '-' * 68)

    for i in range(n):
        print(f'  {i:<4} {x_data[i]:<10.4f} {table[i][0]:<16.4f}', end='')
        for j in range(1, n):
            if j < n - 1:
                val = table[i][j]
                letter = label_matrix[i][j]
                print(f'{val:.4} --> {letter:>10}', end='')
            else:
                print(f'{'':<18}', end='')
        print()