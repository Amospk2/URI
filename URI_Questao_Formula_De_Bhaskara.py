#Fórmula de Bhaskara

from math import sqrt
listValues = input("")
listValues = listValues.split(" ")
listValues = [float(value) for value in listValues]

delta = (listValues[1]**2) - (4*listValues[0]*listValues[2])

if(listValues[0] == 0 or delta <= 0):
  print("Impossivel calcular")
else:
  x1 = (-listValues[1] + sqrt(delta))/(2*listValues[0])
  x2 = (-listValues[1] - sqrt(delta))/(2*listValues[0])
  print(f"R1 = {x1:.5f}")
  print(f"R2 = {x2:.5f}")
