#1
numeros = list(map(int, input("Ingresa 5 números separados por espacios: ").split()))

if numeros == sorted(numeros):
    print("Orden ascendente")
elif numeros == sorted(numeros, reverse=True):
    print("Orden descendente")
else:
    print("Orden aleatorio")


#2
lista = list(map(int, input("Ingresa una lista de números separados por espacios: ").split()))
buscar = int(input("Ingresa el número que deseas buscar: "))

if buscar in lista:
    print("Número encontrado")
else:
    print("Número no encontrado")


#3

numero = input("Ingresa un número entero: ")

pares = 0
impares = 0

for digito in numero:
    if int(digito) % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Dígitos pares:", pares)
print("Dígitos impares:", impares)


#4 

equipoA = list(map(int, input("Ingresa los 5 resultados del Equipo A: ").split()))
equipoB = list(map(int, input("Ingresa los 5 resultados del Equipo B: ").split()))

promA = sum(equipoA) / len(equipoA)
promB = sum(equipoB) / len(equipoB)

if promA > promB:
    print("El equipo A tuvo mejor rendimiento")
elif promB > promA:
    print("El equipo B tuvo mejor rendimiento")
else:
    print("Ambos equipos tuvieron el mismo rendimiento")


#5

from itertools import combinations

numeros = list(map(int, input("Ingresa 4 números separados por espacios: ").split()))

mayor = 0
for a, b in combinations(numeros, 2):
    producto = a * b
    if producto > mayor:
        mayor = producto

print("Mayor producto:", mayor)


#6 

meta = int(input("Ingresa la meta de ahorro: "))

ahorro_diario = 5
total_ahorrado = 0
dias = 0

while total_ahorrado < meta:
    total_ahorrado = total_ahorrado+ ahorro_diario
    ahorro_diario =ahorro_diario + 2
    dias += 1

print("Meta alcanzada en", dias, "días")


#7

numero = input("Ingresa un número: ")

if numero == numero[::-1]:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")


#8

numeros = list(map(int, input("Ingresa 4 números separados por espacios: ").split()))

print("Combinaciones posibles:")
for i in range(len(numeros)):
    for j in range(i + 1, len(numeros)):
        print(f"({numeros[i]}, {numeros[j]})")



#9

numero = int(input("Ingresa un número: "))
es_primo = True

if numero <= 1:
    es_primo = False
else:
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break

if es_primo:
    print("Es un número primo")
else:
    print("No es un número primo")



#10

numeros = list(map(int, input("Ingresa una lista de números: ").split()))

suma_pares = 0

for num in numeros:
    if num % 2 == 0:
        suma_pares += num

print("Suma de los números pares:", suma_pares)
