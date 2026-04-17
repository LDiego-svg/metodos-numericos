import numpy as np
from math import factorial

#construir la tabla para los datos#
def build_table(y_data):
    n = len(y_data)
    table = np.zeros((n, n))
    table[:, 0] = y_data
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = table[i + 1][j - 1] - table[i][j - 1]
    return table

def newton_adelante(x_data, y_data, x, verbose=True):
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
    
    if verbose:
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
                if j < n - i:
                    val = table[i][j]
                    letter = label_matrix[i][j]
                    print(f'{val:.4} --> {letter:>10}', end='')
                else:
                    print(f'{'':<18}', end='')
            print()
    
    #calculo s#
    s = (x - x_data[0]) / h
    
    if verbose:
        print(f'\n h = {h}')
        print(f' s  = (x - x0) / h = ({x} - {x_data[0]}) / {h} = {s:.4f}')
        for k in range(1, n - 1):
            print(f' s{k + 1} = s - {k} = {round(s - k, 4):.4f}')

    #datos de la primera fila#
    formula_letters = [label_matrix[0][j] for j in range(1, n)]

    if verbose:
        print(f'\n FÓRMULA: ')
        terms_letters = ['y0']
        for j in range(1, n):
            s_part = '·'.join(['s'] + [f's{k + 1}' for k in range(1, j)])
            terms_letters.append(f'{formula_letters[j - 1]}·{s_part}/{factorial(j)}')
        print(f'  g(x) = {" + ".join(terms_letters)}')

    result = table[0][0]
    terms_values = [f'{table[0][0]:.4f}']
    for j in range(1, n):
        numerator = 1.0
        s_nums = []
        for k in range(j):
            numerator *= (s - k)
            s_nums.append(f'{s - k:.4f}')
        
        denom = factorial(j)
        diff_val = table[0][j]
        contribution = (numerator/denom) * diff_val
        result += contribution
        
        if verbose:
            s_part_num = '.'.join(s_nums)
            terms_values.append(f'{diff_val:.4f}·{s_part_num}/{denom} = {contribution:.4f}')
        
    if verbose:
        print(f'\n g({x}) = {terms_values[0]}')
        for t in terms_values[1:]:
            print(f'         + {t}')
        print(f"\n  {'─' * 45}")
    print(f"  g({x}) = {result:.4f}")
    print("=" * 70)

    return result
        
def get_data():
    while True:
        try:
            n = int(input('\nCuántos puntos tiene la tabla?'))
            if n >= 2:
                break
            print(' Mínimo debe tener 2 puntos.')
        except ValueError:
            print(' Ingresa un número válido.')
        
    x_data, y_data = [], []
    print(f'\nIngresa los {n} datos pares:')
    for i in range(n):
        while True:
            try:
                x = float(input(f'  x[{i}] = '))
                y = float(input(f'  y[{i}] = '))
                x_data.append(x)
                y_data.append(y)
                break
            except ValueError:
                print(' Valor inválido, intenta de nuevo.')
    while True:
        try:
            x_target = float(input('\nInterpola para x = '))
            break
        except ValueError:
            print(' Valor inválido.')
    
    return np.array(x_data), np.array(y_data), x_target

def main():
    print('=' * 70)
    print('  INTERPOLACION - NEWTON HACIA ADELANTE')
    print('=' * 70)

    while True:
        x_data, y_data, x_target = get_data()
        newton_adelante(x_data, y_data, x_target)

        again = input('\nQuiere resolver otra tabla? (y/n):').strip().lower()
        if again != 'y':
            print('\nListo.')
            break

main()