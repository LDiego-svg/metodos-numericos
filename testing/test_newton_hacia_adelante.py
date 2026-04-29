import sys
from datetime import datetime
sys.path.append('..')

import numpy as np
from newton_adelante import newton_adelante

# ── Casos de prueba — Newton hacia adelante ───────────────────
# Formato: (x_data, y_data, x_target, resultado_esperado)
# Agrega aqui los casos que genere la IA con el prompt en prompt_casos_prueba.md
casos = [
    ([0, 1, 2, 3], [1, 2, 5, 10], 0.5, 1.25),
    ([0, 1, 2, 3], [1, 2, 5, 10], 1.5, 3.25),
    ([0, 1, 2, 3], [1, 2, 5, 10], 2.5, 7.25),
    ([-3, -1, 1, 3], [125, 127, 132, 133], 0, 129.5625),
    ([-3, -1, 1, 3], [125, 127, 132, 133], -2, 125.1875),
    ([-3, -1, 1, 3], [125, 127, 132, 133], 2, 133.4375),
    ([1.0, 1.5, 2.0, 2.5, 3.0], [2.7183, 4.4817, 7.3891, 12.1825, 20.0855], 1.8, 6.0522),
    ([1.0, 1.5, 2.0, 2.5, 3.0], [2.7183, 4.4817, 7.3891, 12.1825, 20.0855], 2.3, 9.9713),
    ([1.0, 1.5, 2.0, 2.5, 3.0], [2.7183, 4.4817, 7.3891, 12.1825, 20.0855], 1.2, 3.3138),
    ([0, 1, 2, 3], [-1, -3, -7, -13], 0.5, -1.75),
    ([0, 1, 2, 3], [-1, -3, -7, -13], 1.5, -4.75),
    ([0, 1, 2, 3], [-1, -3, -7, -13], 2.5, -9.75),
    ([1.0, 1.1, 1.2, 1.3, 1.4], [1.0, 1.1, 1.44, 1.69, 1.96], 1.05, 0.9822),
    ([1.0, 1.1, 1.2, 1.3, 1.4], [1.0, 1.1, 1.44, 1.69, 1.96], 1.25, 1.5797),
    ([0, 2, 4], [1, 9, 25], 1, 4.0),
    ([0, 2, 4], [1, 9, 25], 3, 16.0),
    ([10, 15, 20, 25], [100, 225, 400, 625], 12, 144.0),
    ([10, 15, 20, 25], [100, 225, 400, 625], 18, 324.0),
    ([10, 15, 20, 25], [100, 225, 400, 625], 22, 484.0),
    ([0, 1, 2, 3], [0.5, 1.5, 3.5, 7.5], 0.5, 0.9375),
]

TOL = 0.001

# ── Correr casos ──────────────────────────────────────────────
resultados = []
pasados = 0

for i, (x_data, y_data, x_target, esperado) in enumerate(casos):
    try:
        resultado = newton_adelante(np.array(x_data), np.array(y_data), x_target, verbose=False)
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
        resultados.append({
            "caso": i + 1,
            "status": "ERROR",
            "error": str(e)
        })

# ── Guardar en Markdown ───────────────────────────────────────
fecha = datetime.now().strftime("%Y-%m-%d %H:%M")

with open("resultados_newton_adelante.md", "w", encoding="utf-8") as f:
    f.write(f"# Resultados — Newton hacia adelante\n\n")
    f.write(f"**Fecha:** {fecha}  \n")
    f.write(f"**Tolerancia:** {TOL}  \n")
    f.write(f"**Resultado:** {pasados}/{len(casos)} casos pasados\n\n")

    f.write(f"| Caso | Status | Resultado | Esperado | Diferencia |\n")
    f.write(f"|------|--------|-----------|----------|------------|\n")

    for c in resultados:
        if c["status"] == "ERROR":
            f.write(f"| {c['caso']} | ❌ ERROR | - | - | `{c.get('error', '')}` |\n")
        else:
            icono = "✅" if c["status"] == "PASS" else "❌"
            f.write(f"| {c['caso']} | {icono} {c['status']} | {c['resultado']} | {c['esperado']} | {c['diferencia']} |\n")

    f.write(f"\n---\n")
    f.write(f"*Generado automáticamente por test_newton_adelante.py*\n")

# ── Resumen en consola ────────────────────────────────────────
print(f"\n{'=' * 50}")
print(f"  Newton hacia adelante — {pasados}/{len(casos)} pasados")
print(f"{'=' * 50}")
for c in resultados:
    if c["status"] == "ERROR":
        print(f"  ❌ Caso {c['caso']}: ERROR — {c.get('error')}")
    else:
        icono = "✅" if c["status"] == "PASS" else "❌"
        print(f"  {icono} Caso {c['caso']}: resultado={c['resultado']} esperado={c['esperado']} diff={c['diferencia']}")

print(f"\n  Guardado en: testing/resultados_newton_adelante.md")