# ------------------------ Ejercicio 4: Asignación mínima de salones ------------------------
def asignar_minimo_salones(actividades):
    if not actividades:
        return 0

    actividades.sort(key=lambda x: x[0])
    salones = []

    for inicio, fin in actividades:
        asignado = False
        for i in range(len(salones)):
            if salones[i] <= inicio:
                salones[i] = fin
                asignado = True
                break
        if not asignado:
            salones.append(fin)

    return len(salones)

print("\n--- Prueba Ejercicio 4 ---")
actividades = [
    (0, 6),
    (1, 4),
    (5, 7),
    (3, 8),
    (8, 9)
]
print("Mínimo número de salones necesarios:", asignar_minimo_salones(actividades))

# ------------------------ Ejercicio 5a: Asignación sin interrupciones ------------------------
def asignar_sin_interrupciones(tiempos):
    tiempos.sort()
    tiempo_actual = 0
    suma_tiempos_finales = 0
    for tiempo in tiempos:
        tiempo_actual += tiempo
        suma_tiempos_finales += tiempo_actual
    return suma_tiempos_finales / len(tiempos)

print("\n--- Prueba Ejercicio 5a ---")
tiempos = [5, 1, 3]
print("Tiempo promedio de terminación (sin interrupciones):", asignar_sin_interrupciones(tiempos))

# ------------------------ Ejercicio 5b: Asignación con interrupciones y valor relativo ------------------------
def asignar_con_interrupciones(tareas):
    tareas.sort(key=lambda x: -x[1] / x[0])
    tiempo_actual = 0
    suma_ponderada = 0
    for duracion, valor in tareas:
        tiempo_actual += duracion
        suma_ponderada += tiempo_actual * valor
    return suma_ponderada

print("\n--- Prueba Ejercicio 5b ---")
tareas = [(3, 6), (2, 3), (1, 2)]
print("Tiempo ponderado total (con interrupciones):", asignar_con_interrupciones(tareas))