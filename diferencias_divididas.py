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
    formula_letters = [label_matrix[0][j] for j in range(1, n)]
    if verbose:
        print("\nFORMULA:")
        terms_letters = ["y0"]
        for j in range(1, n):
            x_part = "·".join([f"(x-x{k})" for k in range(j)])
            terms_letters.append(f"{formula_letters[j - 1]}·{x_part}")
        print(f"  g(x) = {' + '.join(terms_letters)}")

    result = table[0][0]
    terms_values = [f"{table[0][0]:.4f}"]

    for j in range(1, n):
        numerator = 1.0
        x_nums = []
        for k in range(j):
            numerator *= x - x_data[k]
            x_nums.append(f"{x - x_data[k]:.4f}")
        diff_val = table[0][j]
        contribution = diff_val * numerator
        result += contribution

        if verbose:
            terms_values.append(f"{diff_val:.4f}·{'·'.join(x_nums)} = {contribution:.4f}")

    if verbose:
        print(f"\n g({x}) = {terms_values[0]}")
        for t in terms_values[1:]:
            print(f"         + {t}")
        print(f"\n  {'─' * 45}")
    print(f"  g({x}) = {result:.4f}")
    print("=" * 70)
    return result


def get_data():
    while True:
        try:
            n = int(input("\nCuántos puntos tiene la tabla? "))
            if n >= 2:
                break
            print(" Mínimo debe tener 2 puntos")
        except ValueError:
            print("Ingresa un número válido")
    x_data, y_data = [], []
    print(f"\nIngresa los {n} datos pares:")
    for i in range(n):
        while True:
            try:
                x = float(input(f"  x[{i}] = "))
                y = float(input(f"  y[{i}] = "))
                x_data.append(x)
                y_data.append(y)
                break
            except ValueError:
                print(" Valor inválido, intenta de nuevo")
    while True:
        try:
            x_target = float(input("\nInterpola para x = "))
            break
        except ValueError:
            print(" Valor invalido")
    return np.array(x_data), np.array(y_data), x_target


def main():
    print("=" * 70)
    print("  INTERPOLACION - DIFERENCIAS DIVIDIDAS")
    print("=" * 70)

    while True:
        x_data, y_data, x_target = get_data()
        diferencias_divididas(x_data, y_data, x_target)

        again = input("\nQuiere resolver otra tabla? (y/n): ").strip().lower()
        if again != "y":
            print("\nListo")
            break


main()
