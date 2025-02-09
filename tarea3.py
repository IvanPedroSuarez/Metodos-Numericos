import math


print('Ejemplo de error de precision en Python')
#Calcular la suma de muchos números decimales pequeños.

suma = 0.0
for i in range(1000000):
  suma += 0.000001

print(suma)
#Deberia dar como resultado 1 mas no lo hace
valor_real = 1.0
error_absoluto = abs(suma - valor_real)
error_relativo = abs(suma - valor_real) / valor_real

print("Error absoluto:", error_absoluto)
print("Error relativo:", error_relativo)




print('Ejemplo de error de redondeo en Python')
#Calcular la suma de una serie de números que no se pueden representar exactamente en punto flotante.
suma = 0.0
for i in range(10):
  suma += 0.1

print(suma)
#Deberia dar como resultado 1 mas no lo hace
valor_real = 1.0
error_absoluto = abs(suma - valor_real)
error_relativo = abs(suma - valor_real) / valor_real

print("Error absoluto:", error_absoluto)
print("Error relativo:", error_relativo)


print('Ejemplo de error de truncamiento en Python')
#Aproximar el valor de e (la base del logaritmo natural) utilizando la serie de Taylor para la función exponencial truncada.
def seno_aproximado(x, n):
  """
  Calcula una aproximación de sin(x) utilizando una serie de Taylor truncada.

  Args:
    x: El valor en el que se va a evaluar la función seno (en radianes).
    n: El número de términos a utilizar en la serie de Taylor.

  Returns:
    La aproximación de sin(x).
  """
  resultado = 0.0
  for i in range(n):
    termino = (-1)**i * x**(2*i + 1) / math.factorial(2*i + 1)
    resultado += termino
  return resultado

# Ejemplo de uso
x = math.pi / 4  # pi/4 radianes (45 grados)
n = 5  # Número de términos en la serie de Taylor

aproximacion = seno_aproximado(x, n)
valor_real = math.sin(x)

print("Aproximación:", aproximacion)
print("Valor real:", valor_real)
error_absoluto = abs(aproximacion - valor_real)
error_relativo = abs(aproximacion - valor_real) / abs(valor_real)

print("Error absoluto:", error_absoluto)
print("Error relativo:", error_relativo)

