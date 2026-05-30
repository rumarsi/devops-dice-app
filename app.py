import dice
import time


def lanzar_dados(amount, sides):
    resultados = []

    for _ in range(amount):
        tirada = dice.roll(f"1d{sides}")
        resultados.append(tirada[0])

    return resultados


resultados = lanzar_dados(amount=6, sides=6)

for i, resultado in enumerate(resultados, start=1):
    print(f"Lanzamiento {i} número obtenido {resultado}")
    time.sleep(5)
