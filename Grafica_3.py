import numpy as np
import matplotlib.pyplot as plt

# Datos (incluyendo monto inicial)
monto_inicial = 40000000  # Egreso en t=0
egresos = np.array([
    21879746.57, 1711752.57, 2037018.57, 1857892.57, 2038744.57, 1973526.57,
    1773976.57, 1704434.57, 1839012.57, 2011062.57, 1814066.57, 1786660.57
])
ingresos = np.array([
    3250000, 2500000, 2000000, 2750000, 2250000, 5000000,
    3500000, 6250000, 3500000, 6000000, 3750000, 5500000
])

# Parámetros financieros
i = 0.015  # Tasa mensual
n = 12     # Número de meses

# Cálculo del VPN (incluyendo monto inicial)
flujos_netos = ingresos - egresos
vpn = -monto_inicial + sum(flujos_netos[t] / (1 + i)**(t + 1) for t in range(n))

# Cálculo de la serie uniforme equivalente (A)
A = vpn * (i * (1 + i)**n) / ((1 + i)**n - 1)

# Configuración del gráfico con tamaño optimizado
plt.figure(figsize=(15, 8))

# Crear arrays para el gráfico
meses = np.arange(0, 13)  # Mes 0 a 12

# --- Barras de Egresos/Ingresos originales ---
# Egresos mensuales (Meses 1-12)
bar_egresos = plt.bar(meses[1:], -A/1e5, color='limegreen', alpha=0.7, label='Egresos', width=0.4)
# Ingresos mensuales (Meses 1-12)
bar_ingresos = plt.bar(meses[1:], A/1e5, color='salmon', alpha=0.7, label='Ingresos', width=0.4)

# # --- Serie uniforme ---
# linea_serie = plt.axhline(y=A/1e6, color='blue', linestyle='--', linewidth=2, 
#                          label=f'Serie Uniforme (A = {A/1e6:,.2f} M)')

# --- Inversión inicial ---
# bar_inicial = plt.bar(0, -monto_inicial/1e6, color='darkred', label='Inversión Inicial', width=0.4)

# Añadir etiquetas de valor
for bar in bar_egresos:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height-0.5,
             f'{height:,.1f}',
             ha='center', va='top', color='white', fontsize=8)

for bar in bar_ingresos:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height+0.5,
             f'{height:,.1f}',
             ha='center', va='bottom', color='darkgreen', fontsize=8)

# Etiqueta para inversión inicial
plt.text(0, -monto_inicial/1e6-1, f'{-monto_inicial/1e6:,.1f}',
         ha='center', va='top', color='white', fontsize=8)

# Línea de referencia y=0
plt.axhline(0, color='black', linewidth=0.8)

# Ajustes estéticos
plt.title('Serie Uniforme', fontsize=14, pad=20)
plt.xlabel('Mes', fontsize=12)
plt.ylabel('Millones de $', fontsize=12)
plt.xticks(meses, [f'Mes {m}' for m in meses], rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1))

# Ajustar límites del eje Y automáticamente
max_val = max(max(ingresos/1e6), max(abs(egresos/1e6)), abs(A/1e6), abs(monto_inicial/1e6)) * 1.2
plt.ylim(-max_val, max_val)

# Mostrar el gráfico
plt.tight_layout()
plt.show()

print(f"Valor Presente Neto (VPN): {vpn:,.2f}")
print(f"Serie Uniforme Equivalente (A): {A:,.2f}")