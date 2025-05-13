import random
import numpy as np
import matplotlib.pyplot as plt

def count_if_calls(array, min_, max_):
    calls = 0
    for i in range(len(array)):
        for j in range(i, len(array)):
            for k in range(i, j+1):
                calls += 1
                if array[k] < min_ or array[k] > max_:
                    break
    return calls

Ns, Cs = [], []
for N in range(1000, 20001, 1000):
    A = [random.randint(1,1000) for _ in range(N)]
    c = count_if_calls(A, 250, 750)
    Ns.append(N);  Cs.append(c)

# Ajuste polinomial de grado 2: calls ≈ a N^2 + b N + c
coef = np.polyfit(Ns, Cs, 2)
a, b, c0 = coef
print(f"Tendencia promedio: calls ≃ {a:.3e}N^2 + {b:.3e}N + {c0:.3e}")

plt.scatter(Ns, Cs)
plt.plot(Ns, np.polyval(coef, Ns), lw=2)
plt.xlabel("N"); plt.ylabel("Número de llamadas")
plt.title("Caso promedio")

