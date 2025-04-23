import numpy as np
import matplotlib.pyplot as plt

# Datos (incluyendo monto inicial)
monto_inicial = 59956087  # Egreso en t=0
egresos = np.array([
    6493621.46, 6205621.46, 6205621.46, 26320621.46,
    6570621.46, 6570621.46, 6570621.46, 2716301.58,
    2716301.58, 2716301.58, 2716301.58, 4616301.58
])
ingresos = np.array([
    1, 1, 1, 1,
    1, 1, 1, 2000000,
    2000000, 2000000, 2000000, 2000000
])

# Parámetros financieros
i = 0.015  # Tasa mensual
n = 12     # Número de meses

# Cálculo del VPN (incluyendo monto inicial)
flujos_netos = ingresos - egresos
vpn = -monto_inicial + sum(flujos_netos[t] / (1 + i)**(t + 1) for t in range(n))

# Cálculo de la serie uniforme equivalente (A)
A = vpn * (i * (1 + i)**n) / ((1 + i)**n - 1)

# Crear arrays para el gráfico
meses = np.arange(0, 13)  # Mes 1 a 12
# serie_uniforme = np.full(13, A)  # Aplicamos A desde Mes 1 (opcional: Mes 0 puede ser 0)

# Gráfico comparativo
fig, ax = plt.subplots(figsize=(14, 7))

# --- Barras de Egresos/Ingresos originales (solo para referencia) ---

# Egresos mensuales (Meses 1-12)
ax.bar(meses[1:], -11500000, color='salmon', alpha=0.3, label='Egresos Mensuales (Original)', width=0.4)
# Ingresos mensuales (Meses 1-12)
ax.bar(meses[1:], 11500000, color='limegreen', alpha=0.3, label='Ingresos Mensuales (Original)', width=0.4)

#gresos mensuales
for i in range(1, 13):
    if egresos[i-1] != 0:
        ax.text(i, -11500000 - 1e6, f'{-11500000/1e6:,.1f}M', ha='center', va='top', fontsize=7, color='darkred')
# Ingresos mensuales
for i in range(1, 13):
    if ingresos[i-1] != 0:
        ax.text(i, 11500000 + 1e5, f'{11500000/1e6:,.1f}M', ha='center', va='bottom', fontsize=7, color='darkgreen')

# Línea de referencia y=0
ax.axhline(0, color='black', linewidth=0.8)

# Ajustes estéticos
ax.set_title('Serie Uniforme Equivalente', fontsize=14, pad=20)
ax.set_xlabel('Mes', fontsize=12)
ax.set_ylabel('Monto (Millones $)', fontsize=12)
ax.set_xticks(meses)
ax.set_xticklabels([f'Mes {m}' for m in meses], rotation=45)
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(loc='upper right')

# Ajustar límites del eje Y
ax.set_ylim(min(-egresos.min(), A * 1.5) if A < 0 else ax.set_ylim(-monto_inicial * 0.1, max(ingresos.max(), A) * 1.5))

plt.tight_layout()
plt.show()