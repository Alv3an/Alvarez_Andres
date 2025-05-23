import numpy as np
from numpy_financial import irr
import matplotlib.pyplot as plt

# Datos proporcionados
egresos = np.array([
    -21879746.57, -1711752.57, -2037018.57, -1857892.57, -2038744.57, -1973526.57,
    -1773976.57, -1704434.57, -1839012.57, -2011062.57, -1814066.57, -1786660.57
])
ingresos = np.array([
  3250000, 2500000, 2000000, 2750000, 2250000, 5000000,
    3500000, 6250000, 3500000, 6000000, 3750000, 5500000
])

# Inversión inicial (egreso en Mes 0)
monto_inicial = -40000000  # Ajusta según tu caso

# Flujos netos (Mes 1 a 12) y agregar Mes 0
flujos_netos = ingresos + (egresos * -1)  # Versión explícita
flujos_completos = np.insert(flujos_netos, 0, monto_inicial)

# Calcular TIR
tir = irr(flujos_completos)
tir_porcentual = tir * 100

# --- Gráfico ---
meses = np.arange(0, 13)  # Meses 0 a 12
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), gridspec_kw={'height_ratios': [3, 1]})

# 1. Gráfico de barras (flujos netos)
bars = ax1.bar(meses, flujos_completos, color=np.where(flujos_completos >= 0, 'limegreen', 'tomato'))
ax1.axhline(0, color='black', linewidth=0.8)
ax1.set_title('Flujos de Caja Netos por Mes (Inversión Inicial + Operación)', fontsize=14, pad=20)
ax1.set_xlabel('Mes')
ax1.set_ylabel('Monto ($)')
ax1.grid(axis='y', linestyle='--', alpha=0.6)

# Etiquetas de valores en las barras
for bar in bars:
    height = bar.get_height()
    if height >= 0:
        ax1.text(bar.get_x() + bar.get_width()/2, height + 1e5, f'{height/1e6:,.1f}M',
                ha='center', va='bottom', fontsize=8)
    else:
        ax1.text(bar.get_x() + bar.get_width()/2, height - 1e5, f'{height/1e6:,.1f}M',
                ha='center', va='top', fontsize=8)

# 2. Gráfico de TIR (texto y línea horizontal)
ax2.axis('off')  # Ocultar ejes del subplot inferior
ax2.text(0.5, 0.5, f'Tasa Interna de Retorno (TIR): {tir_porcentual:.2f}%',
         ha='center', va='center', fontsize=12,
         bbox=dict(facecolor='gold', alpha=0.8, edgecolor='orange', boxstyle='round'))

plt.tight_layout()
plt.show()