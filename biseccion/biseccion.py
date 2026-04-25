import re

def preparar_ecuacion(ecuacion):
    ecuacion = ecuacion.replace('^', '**')
    ecuacion = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', ecuacion)
    ecuacion = re.sub(r'(\))([a-zA-Z\d])', r'\1*\2', ecuacion)
    return ecuacion

def f(ecuacion, x):
    return eval(ecuacion)

def biseccion(ecuacion, a, b, tol=0.001, max_iter=100, verbose=True):
    if f(ecuacion, a) * f(ecuacion, b) > 0:
        print('  Error: f(a) y f(b) tienen el mismo signo, no hay raiz garantizada en el intervalo')
        return None
    
    if verbose:
        print("\n" + "=" * 70)
        print("  BISECCION")
        print("=" * 70)
        print(f"\n  Ecuacion: f(x) = {ecuacion}")
        print(f"  Intervalo inicial: a = {a}, b = {b}")
        print(f"  Tolerancia: {tol}")
        print(f"\n  {'i':<6} {'a':<12} {'b':<12} {'c':<12} {'f(c)':<15} {'|xi - xi+1|'}")
        print("  " + "-" * 65)
    
    c_anterior = None
    i = 0
    while i < max_iter:
        c = (a + b) / 2
        fc = f(ecuacion, c)
        if verbose:
            diferencia = abs(c - c_anterior) if c_anterior is not None else '-'
            if isinstance(diferencia, float):
                 print(f"  {i:<6} {a:<12.4f} {b:<12.4f} {c:<12.4f} {fc:<15.4f} {diferencia:.6f}")
            else:
                 print(f"  {i:<6} {a:<12.4f} {b:<12.4f} {c:<12.4f} {fc:<15.4f} {diferencia}")
        
        if fc == 0:
            break
        if c_anterior is not None and abs(c - c_anterior) < tol:
            break
        if f(ecuacion, a) * fc < 0:
            b = c
        else:
            a = c
        c_anterior = c
        i += 1
    else:
        print(f"\n  Advertencia: Se alcanzo el maximo de {max_iter} iteraciones sin converger.")

    if verbose:
        print(f"\n  {'─' * 45}")
    print(f"  Raiz aproximada: x = {c:.4f}")
    print(f"  f({c:.4f}) = {fc:.6f}")
    print("=" * 70)
    return c

def get_data():
    print('\nIngresa la ecuacion: ')
    print(' Ejemplo: 7x^3 + 4x^2 + 85')
    ecuacion = input('  f(x) = ')
    ecuacion = preparar_ecuacion(ecuacion)

    while True:
        try:
            a = float(input('\nIngresa el valor de a (limite inferior): '))
            break
        except ValueError:
            print('  Valor invalido')
    
    while True:
        try:
            b = float(input('\nIngresa el valor de b ( limite superior): '))
            break
        except ValueError:
            print('  Valor invalido')
    return ecuacion, a, b

def main():
    print("=" * 70)
    print("  SOLUCION DE ECUACIONES - BISECCION")
    print("=" * 70)

    while True:
        ecuacion, a, b = get_data()
        biseccion(ecuacion, a, b)
        again = input('\nQuiere resolver otra ecuacion? (y/n): ').strip().lower()
        if again != 'y':
            print('\nListo')
            break

main()
