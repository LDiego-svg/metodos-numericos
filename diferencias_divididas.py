from math import factorial

import numpy as np


def build_divided_table(x_data, y_data):
    n = len(x_data)
    table = np.zeros((n, n))
    table[:, 0] = y_data
    for j in range(1, n):
        for i in range(n - j):
            table[i, j] = (table[i + 1, j - 1] - table[i, j - 1]) / (
                x_data[i + j] - x_data[i]
            )
    return table


def diferencias_divididas(x_data, y_data, x, verbose=True):
    n = len(x_data)
    table = build_divided_table(x_data, y_data)
    letters = [chr(65 + i) for i in range(26)]
    letters_idx = 0
    label_matrix = np.full((n, n), "", dtype=object)
    for j in range(1, n):
        for i in range(n - j):
            label_matrix[i][j] = letters[letters_idx]
            letters_idx += 1
    if verbose:
        print("\n" + "=" * 70)
        print("Tabla de diferencias divididas")
        print("=" * 70)
        print(f" {'i':<4} {'xi':<10} {'D0yi':<16}", end="")
        for k in range(1, n):
            print(f"{'D' + str(k) + 'yi':<18}", end="")
        print()
        print(" " + "-" * 68)

        for i in range(n):
            print(f"  {i:<4} {x_data[i]:<10.4f} {table[i][0]:<16.4f}", end="")
            for j in range(1, n):
                if j < n - i:
                    val = table[i][j]
                    letter = label_matrix[i][j]
                    print(f"{val:.4f} --> {letter:<10}", end="")
            print()
