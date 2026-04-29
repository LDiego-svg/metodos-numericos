---
name: testing-metodos-numericos
description: >
  Genera casos de prueba y scripts de testing para métodos numéricos implementados en Python.
  Usar cuando el usuario pida hacer testing de un método, generar casos de prueba, verificar
  resultados, o crear un script que compare la salida del programa con el resultado esperado.
  También aplica cuando el usuario diga "prueba este método", "genera casos para X",
  "quiero verificar que funciona", o "crea el test para Y".
---

# Testing de Métodos Numéricos

## Contexto del proyecto

Los métodos están implementados en Python con esta firma estándar:

```python
# Métodos de interpolación
def metodo(x_data, y_data, x_target, verbose=True) -> float

# Métodos de raíces
def metodo(ecuacion, a, b, tol=0.001, verbose=True) -> float
```

Todos aceptan `verbose=False` para suprimir prints y devuelven solo el resultado numérico.

## Estructura de carpetas esperada

```
proyecto/
├── newton_adelante.py
├── newton_atras.py
├── diferencias_divididas.py
├── lagrange.py
├── biseccion.py
├── secante.py
├── newton_raphson.py
└── testing/
    ├── test_[metodo].py
    ├── resultados_[metodo].md
    └── prompt_casos_prueba.md
```

## Flujo al hacer testing de un método

### 1. Generar casos de prueba

Genera entre 15 y 25 casos de prueba. Cada caso debe:
- Cubrir escenarios variados: pocos puntos, muchos puntos, valores negativos, decimales
- Tener un resultado esperado calculado manualmente y verificado
- Estar en formato de tupla lista para copiar y pegar

**Formato por método:**

#### Interpolación (Newton adelante, atrás, Diferencias divididas, Lagrange)
```python
casos = [
    # (x_data, y_data, x_target, resultado_esperado)
    ([-3, -1, 1, 3], [125, 127, 132, 133], 0, 129.5625),
]
```

#### Raíces (Bisección, Secante, Newton-Raphson)
```python
casos = [
    # (ecuacion_str, a, b, resultado_esperado)
    ("7*x**3 + 4*x**2 + 85", -3, -2, -2.5049),
]
```

### 2. Crear el script de testing

El script debe:
- Importar la función del método con `sys.path.append('..')`
- Correr todos los casos con `verbose=False`
- Comparar resultado vs esperado con tolerancia `TOL = 0.001`
- Guardar un `.md` con tabla de resultados
- Imprimir resumen en consola

**Plantilla base:**
```python
import sys
from datetime import datetime
sys.path.append('..')

import numpy as np
from [metodo] import [funcion]

casos = [
    # pegar casos aqui
]

TOL = 0.001
resultados = []
pasados = 0

for i, (*entradas, esperado) in enumerate(casos):
    try:
        resultado = funcion(*[np.array(e) if isinstance(e, list) else e for e in entradas], verbose=False)
        diferencia = abs(resultado - esperado)
        status = "PASS" if diferencia < TOL else "FAIL"
        if status == "PASS":
            pasados += 1
        resultados.append({
            "caso": i + 1,
            "status": status,
            "resultado": round(resultado, 4),
            "esperado": round(esperado, 4),
            "diferencia": round(diferencia, 6)
        })
    except Exception as e:
        resultados.append({"caso": i + 1, "status": "ERROR", "error": str(e)})

# guardar en markdown
fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
with open("resultados_[metodo].md", "w", encoding="utf-8") as f:
    f.write(f"# Resultados — [Nombre método]\n\n")
    f.write(f"**Fecha:** {fecha}  \n")
    f.write(f"**Tolerancia:** {TOL}  \n")
    f.write(f"**Resultado:** {pasados}/{len(casos)} casos pasados\n\n")
    f.write(f"| Caso | Status | Resultado | Esperado | Diferencia |\n")
    f.write(f"|------|--------|-----------|----------|------------|\n")
    for c in resultados:
        if c["status"] == "ERROR":
            f.write(f"| {c['caso']} | ❌ ERROR | - | - | `{c.get('error')}` |\n")
        else:
            icono = "✅" if c["status"] == "PASS" else "❌"
            f.write(f"| {c['caso']} | {icono} {c['status']} | {c['resultado']} | {c['esperado']} | {c['diferencia']} |\n")

# resumen consola
print(f"\n{'=' * 50}")
print(f"  [Método] — {pasados}/{len(casos)} pasados")
print(f"{'=' * 50}")
for c in resultados:
    icono = "✅" if c["status"] == "PASS" else ("❌" if c["status"] == "FAIL" else "💥")
    print(f"  {icono} Caso {c['caso']}: {c.get('resultado', 'ERROR')} vs {c.get('esperado', '-')}")
```

### 3. Ejecutar

```bash
# activar venv
.\venv\Scripts\Activate   # Windows
source venv/bin/activate  # Mac/Linux

# correr
cd testing
python test_[metodo].py
```

## Notas importantes

- Verificar siempre 2-3 casos manualmente antes de confiar en el batch completo
- Si un caso da FAIL revisar primero si el resultado esperado está bien calculado
- La tolerancia 0.001 es la misma que usan los métodos como criterio de paro
- Para Newton adelante y atrás: `x_data` debe ser equiespaciado
- Para diferencias divididas: `x_data` puede ser no equiespaciado
- Para métodos de raíces: verificar que f(a)*f(b) < 0 antes de agregar el caso
