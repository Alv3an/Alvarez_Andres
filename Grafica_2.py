import numpy as np
import matplotlib.pyplot as plt

# Datos ajustados (incluyendo Mes 0)
monto_inicial = 59956087  # Positivo para graficar como egreso (lo convertiremos a negativo)
egresos = np.array([
    6493621.46, 6205621.46, 6205621.46, 26320621.46,
    6570621.46, 6570621.46, 6570621.46, 2716301.58,
    2716301.58, 2716301.58, 2716301.58, 4616301.58
])
ingresos = np.array([
    0, 0, 0, 0,
    0, 0, 0, 2000000,
    2000000, 2000000, 2000000, 2000000
])

# Parámetros financieros
i = 0.015  # Tasa mensual
n = 12     # Número de meses

# Meses (0 a 12)
meses = np.arange(0, 13)  # Mes 0: Inversión inicial; Meses 1-12: flujos mensuales

# Cálculo del VPN (incluyendo monto inicial)
flujos_netos = ingresos - egresos
vpn = -monto_inicial + sum(flujos_netos[t] / (1 + i)**(t + 1) for t in range(n))

# Cálculo de la serie uniforme equivalente (A)
A = vpn * (i * (1 + i)**n) / ((1 + i)**n - 1)

# Configuración del gráfico
fig, ax = plt.subplots(figsize=(14, 7))

# --- Barras de Egresos (rojas, hacia abajo) ---
# Egreso inicial (Mes 0)
ax.bar(0, -monto_inicial, color='tomato', label='Egreso Inicial (Mes 0)', width=0.6)
# Egresos mensuales (Meses 1-12)
ax.bar(meses[1:], -egresos, color='salmon', label='Egresos Mensuales', width=0.6)

# --- Barras de Ingresos (verdes, hacia arriba) ---
ax.bar(meses[1:], ingresos, color='limegreen', label='Ingresos Mensuales', width=0.6)

# Línea de referencia y=0
ax.axhline(0, color='black', linewidth=0.8)

# --- Etiquetas de valores ---
# Monto inicial (Mes 0)
ax.text(0, -monto_inicial - 3e6, f'{-monto_inicial/1e6:,.1f}M', ha='center', va='top', fontsize=8, color='darkred')
# Egresos mensuales
for i in range(1, 13):
    if egresos[i-1] != 0:
        ax.text(i, -egresos[i-1] - 1e6, f'{-egresos[i-1]/1e6:,.1f}M', ha='center', va='top', fontsize=7, color='darkred')
# Ingresos mensuales
for i in range(1, 13):
    if ingresos[i-1] != 0:
        ax.text(i, ingresos[i-1] + 1e6, f'{ingresos[i-1]/1e6:,.1f}M', ha='center', va='bottom', fontsize=7, color='darkgreen')

# A = -1701302  # Ejemplo (recalcula con el VPN correcto)
ax.axhline(A, color='blue', linestyle='--', label=f'Serie Uniforme Equivalente (A = {A/1e6:,.1f}M)')
ax.legend(loc='upper right')

# --- Ajustes estéticos ---
ax.set_title('Flujo de Caja Completo: Inversión Inicial + Egresos/Ingresos Mensuales', fontsize=14, pad=20)
ax.set_xlabel('Mes', fontsize=12)
ax.set_ylabel('Monto (Millones $)', fontsize=12)
ax.set_xticks(meses)
ax.set_xticklabels([f'Mes {m}' for m in meses], rotation=45)
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(loc='upper right')

# Ajustar límites del eje Y para mejor visualización
ax.set_ylim(-monto_inicial * 1.1, max(ingresos) * 1.5)

plt.tight_layout()
plt.show()