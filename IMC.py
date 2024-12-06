nombre= input("Introduce tu nombre: ")
altura = int(input("Introduce tu altura (cm): "))
peso = float(input("Introduce tu peso (kg): "))

altura= altura/100

IMC = peso/(altura ** 2)

print("El IMC de", nombre, "es", IMC)