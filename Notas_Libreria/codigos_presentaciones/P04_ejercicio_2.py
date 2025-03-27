import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
from time import perf_counter
from tqdm import tqdm  # Importar barra de progreso

# algoritmo suma de sumas con contador
def sums_sum_count(array: list[int]) -> int:
    sum_s = 0
    count = 0  
    for m in range(len(array)):  # se itera por el arreglo con m
        sum_m = 0
        for k in range(m + 1):
            sum_m += array[k]  # se suman los elementos en el arreglo de k a m + 1
            count += 1 # se cuenta una suma mas
        sum_s += sum_m # datos experimental
        count += 1  # se cuenta una suma mas
    return sum_s, count # se devuelve la suma de sumas y su contador

# datos experimentales
SIZES = [100 * (2 ** i) for i in range(8)]  # 100, 200, 400, ..., 51200
counts = [None] * len(SIZES)  # Lista para guardar cantidad de sumas

# eejecutar y contar sumas con barra de progreso
with tqdm(total=len(SIZES), desc="Ejecutando SUMS-SUM", unit="iter") as pbar:
    for i, n in enumerate(SIZES):
        array = np.random.randint(-10, 10, n)  # Generar arreglo aleatorio
        _, counts[i] = sums_sum_count(array)  # Ejecutar algoritmo y obtener conteo
        pbar.update(1)  # Actualizar barra de progreso

# modelo cuadrático para contar sumas
curve = lambda x, a, b, c: a * x**2 + b * x + c
opt_params, _ = curve_fit(curve, SIZES, counts)
a, b, c = opt_params

# imprimir valores obtenidos
print("\nValores obtenidos (n, c):")
for i in range(len(SIZES)):
    print(f"n = {SIZES[i]:5}, c = {counts[i]}")

# DataFrame para graficar los datos experimentales
df = pd.DataFrame({"n": SIZES, "c": counts})

# valores ajustados para la gráfica
df_fit = pd.DataFrame({
    "n": range(50_000),
    "c_fit": [curve(x, *opt_params) for x in range(50_000)]
})

# grafica
ax = df.plot.scatter("n", "c", label="Datos experimentales")
df_fit.plot(ax=ax, x="n", y="c_fit", ls="--", color="red", label="Ajuste cuadrático")

plt.title("Cantidad de sumas vs. Tamaño del problema")
plt.xlabel("Tamaño del arreglo (n)")
plt.ylabel("Cantidad de sumas")
plt.grid()
plt.show()

# mostrar coeficientes de la ecuación cuadrática
print("\nEcuación ajustada: c(n) = {:.2e} * n^2 + {:.2e} * n + {:.2e}".format(a, b, c))
