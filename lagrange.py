import numpy as np


def lagrange(x_data, y_data, x, verbose=True):
    n = len(x_data)
    letters = [chr(65 + i) for i in range(26)]

    if verbose:
        print("\n" + "=" * 70)
        print("INTERPOLACION DE LAGRANGE")
        print("=" * 70)
        print(f"\n  {'i':<6} {'xi':<10} {'yi':<10}")
        print("  " + "-" * 28)
        for i in range(n):
            print(f"  {i:<6} {x_data[i]:<10.4f} {y_data[i]:<10.4f}")

    result = 0.0
    terms_values = []

    for i in range(n):
        li = 1.0
        numerator_parts = []
        denominator_parts = []

        for j in range(n):
            if j != i:
                li *= (x - x_data[j]) / (x_data[i] - x_data[j])
                numerator_parts.append(f"({x}-{x_data[j]})")
                denominator_parts.append(f"({x_data[i]}-{x_data[j]})")

        contribution = y_data[i] * li
        result += contribution

        if verbose:
            num_str = "·".join(numerator_parts)
            den_str = "·".join(denominator_parts)
            terms_values.append(
                f"{letters[i]} = {y_data[i]:.4f} · [{num_str}] / [{den_str}] = {contribution:.4f}"
            )

    if verbose:
        print(f"\n  x a interpolar = {x}")
        print(f"\n  TERMINOS:")
        for t in terms_values:
            print(f"    {t}")
        print(f"\n  {'─' * 45}")

    print(f"  g({x}) = {result:.4f}")
    print("=" * 70)

    return result


def get_data():
    while True:
        try:
            n = int(input("\nCuantos puntos tiene la tabla? "))
            if n >= 2:
                break
            print(" Mínimo debe tener 2 puntos")
        except ValueError:
            print(" Ingresa un número válido")

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
    print("  INTERPOLACION - LAGRANGE")
    print("=" * 70)

    while True:
        x_data, y_data, x_target = get_data()
        lagrange(x_data, y_data, x_target)

        again = input("\nQuiere resolver otra tabla? (y/n): ").strip().lower()
        if again != "y":
            print("\nListo")
            break


main()
