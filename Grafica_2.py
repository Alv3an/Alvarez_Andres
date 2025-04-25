import matplotlib.pyplot as plt

# Datos
monto_inicial = 40000000
meses = [
    "Mes 01", "Mes 02", "Mes 03", "Mes 04", "Mes 05", "Mes 06",
    "Mes 07", "Mes 08", "Mes 09", "Mes 10", "Mes 11", "Mes 12"
]
ingresos = [
    3250000, 2500000, 2000000, 2750000, 2250000, 5000000,
    3500000, 6250000, 3500000, 6000000, 3750000, 5500000
]
egresos = [
    21879746.57, 1711752.57, 2037018.57, 1857892.57, 2038744.57, 1973526.57,
    1773976.57, 1704434.57, 1839012.57, 2011062.57, 1814066.57, 1786660.57
]

# Flujo neto promedio mensual
flujo_prom = sum([(ing - egr) for ing, egr in zip(ingresos, egresos)]) / 12

# Parámetros financieros
i = 0.015  # Tasa de interés mensual
n = 12    # Número de meses

# Cálculo de serie uniforme
def calcular_serie_uniforme(VP, i, n):
    return VP * (i * (1 + i)**n) / ((1 + i)**n - 1)

R = calcular_serie_uniforme(monto_inicial, i, n)

# Resultados
print(f"Flujo neto promedio mensual: ${flujo_prom:,.2f}")
print(f"Serie uniforme equivalente (R): ${R:,.2f} durante {n} meses a una tasa del {i*100:.2f}% mensual")

# Crear gráfica
plt.figure(figsize=(12, 6))
plt.bar(meses, ingresos, label="Ingresos", color="green")
plt.bar(meses, [-e for e in egresos], label="Egresos", color="red")

# Agregar línea de serie uniforme
# plt.plot(meses, [R] * 12, label=f"Serie Uniforme (${R:,.0f})", color="blue", linestyle='--', linewidth=2)

# Ajustes estéticos
plt.axhline(0, color='black', linewidth=0.8)
plt.title("Comparación de Ingresos, Egresos y Serie Uniforme")
plt.ylabel("Monto en Pesos ($)")
plt.legend()
plt.grid(True, axis='y', linestyle='--', alpha=0.7)

# Mostrar
plt.tight_layout()
plt.show()
