"""
Programa: Registro básico de un estudiante
Descripción: Este programa solicita datos básicos de un estudiante,
muestra su información y determina si es mayor de edad.
"""

# Entrada de datos
nombre_estudiante = input("Ingrese el nombre del estudiante: ")
edad_estudiante = int(input("Ingrese la edad del estudiante: "))
promedio_estudiante = float(input("Ingrese el promedio del estudiante: "))

# Evaluación booleana
es_mayor_edad = edad_estudiante >= 18

# Salida de información
print("\n--- DATOS DEL ESTUDIANTE ---")
print("Nombre:", nombre_estudiante)
print("Edad:", edad_estudiante)
print("Promedio:", promedio_estudiante)

if es_mayor_edad:
    print("Estado: Mayor de edad")
else:
    print("Estado: Menor de edad")
