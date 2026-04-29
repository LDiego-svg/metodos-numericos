# Prompt para generar casos de prueba

Pega este prompt en Claude o cualquier IA para generar casos de prueba para cada método.
Cambia [MÉTODO] y [DETALLES] según el método que quieras probar.

---

## Prompt base

```
Genera 20 casos de prueba para el método de [MÉTODO] con las siguientes condiciones:

- Cada caso debe tener entradas válidas y un resultado esperado calculado correctamente
- El resultado esperado debe ser preciso a 4 decimales
- Los casos deben cubrir diferentes escenarios (pocos puntos, muchos puntos, valores negativos, decimales, etc.)
- Devuelve los casos en formato Python como una lista de tuplas lista para copiar y pegar

Formato de salida (solo el código, sin explicaciones):
casos = [
    (entradas..., resultado_esperado),
    ...
]
```

---

## Por método

### Newton hacia adelante
```
Genera 20 casos de prueba para el método de Newton hacia adelante con estas condiciones:
- x_data debe ser equiespaciado
- Mínimo 3 puntos, máximo 6 puntos
- x_target debe estar dentro o cerca del intervalo
- Resultado esperado calculado con la fórmula de Newton hacia adelante

Formato:
casos = [
    # (x_data, y_data, x_target, resultado_esperado)
    ([-3, -1, 1, 3], [125, 127, 132, 133], 0, 129.5625),
    ...
]
```

### Newton hacia atrás
```
Genera 20 casos de prueba para el método de Newton hacia atrás con estas condiciones:
- x_data debe ser equiespaciado
- Mínimo 3 puntos, máximo 6 puntos
- x_target debe estar cerca del último punto de la tabla
- Resultado esperado calculado con la fórmula de Newton hacia atrás

Formato:
casos = [
    # (x_data, y_data, x_target, resultado_esperado)
    ([1.0, 1.1, 1.2, 1.3, 1.4], [27, 30, 32, 33, 34], 1.253, 32.6143),
    ...
]
```

### Diferencias divididas
```
Genera 20 casos de prueba para el método de diferencias divididas de Newton con estas condiciones:
- x_data NO necesita ser equiespaciado
- Mínimo 3 puntos, máximo 5 puntos
- x_target puede estar dentro o fuera del intervalo
- Resultado esperado calculado con la fórmula de diferencias divididas

Formato:
casos = [
    # (x_data, y_data, x_target, resultado_esperado)
    ([28, 30, 33, 35], [215, 222, 227, 230], 32, 225.6857),
    ...
]
```

### Lagrange
```
Genera 20 casos de prueba para el método de interpolación de Lagrange con estas condiciones:
- x_data puede tener cualquier espaciado
- Mínimo 3 puntos, máximo 5 puntos
- x_target puede estar dentro del intervalo
- Resultado esperado calculado con la fórmula de Lagrange

Formato:
casos = [
    # (x_data, y_data, x_target, resultado_esperado)
    ([1.5, 2.5, 3.5, 4.5], [2.76, 3.4, 4.09, 4.23], 3, 3.7762),
    ...
]
```

### Bisección
```
Genera 20 casos de prueba para el método de bisección con estas condiciones:
- La ecuación debe tener al menos una raíz real
- El intervalo [a, b] debe contener un cambio de signo (f(a)*f(b) < 0)
- Tolerancia: 0.001
- Resultado esperado es la raíz aproximada

Formato:
casos = [
    # (ecuacion_str, a, b, raiz_esperada)
    ("7*x**3 + 4*x**2 + 85", -3, -2, -2.5049),
    ...
]
```

---

## Notas

- Verifica siempre al menos 2-3 casos manualmente antes de correr el script completo
- Si la IA da resultados incorrectos, pídele que recalcule caso por caso
- La tolerancia para comparar resultados en el script es 0.001
