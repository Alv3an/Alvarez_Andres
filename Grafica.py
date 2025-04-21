import numpy as np
import matplotlib.pyplot as plt

# Datos del préstamo
prestamo_inicial = 50_000_000  # 50 millones
tasa_anual = 0.18  # 18%
tasa_mensual = tasa_anual / 12  # Tasa de interés mensual
periodos = 12  # Número de meses

# Cálculo de la cuota fija mensual (fórmula de anualidades)
cuota_mensual = (prestamo_inicial * tasa_mensual) / (1 - (1 + tasa_mensual) ** -periodos)

# Datos de ingresos y egresos (tomados de la tabla inicial y ajustados)
egresos = [
    2_442_166.57, 2_204_166.57, 2_204_166.57, 22_369_166.57, 2_569_166.57, 2_569_166.57, 2_569_166.57, 
    569_166.57, 569_166.57, 569_166.57, 569_166.57, 569_166.57
]

# Ingresos (cambiando los signos de los valores negativos de la tabla)
ingresos = [-val for val in egresos]

# Crear gráfico
meses = np.arange(len(egresos))

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(meses, ingresos, color='darkgreen', label="Ingresos")
ax.bar(meses, egresos, color='lightgreen', label="Egresos")

# Añadir etiquetas
ax.set_xticks(meses)
ax.set_xticklabels(meses + 1)
ax.set_xlabel("Mes")
ax.set_ylabel("Valor ($)")
ax.set_title("Flujo de caja mensual con préstamo de 50M y 18% anual")
ax.legend()

# Mostrar valores en las barras
for i in range(len(meses)):
    ax.text(meses[i], ingresos[i] + 100_000, f"{ingresos[i]:,.0f}", ha='center', fontsize=8, color='black')
    ax.text(meses[i], egresos[i] - 100_000, f"{egresos[i]:,.0f}", ha='center', fontsize=8, color='black')

plt.grid(axis='y', linestyle='-', alpha=0.7)
plt.show()
