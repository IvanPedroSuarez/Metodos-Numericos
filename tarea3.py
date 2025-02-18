import math

print('Ejemplo 1 de error de precision en Python')
# Este ejemplo busca demostrar cómo la suma repetida de números decimales muy pequeños puede llevar a un error de precisión debido a la forma en que se almacenan los números en punto flotante.
suma = 0.0
for i in range(1000000):
  suma += 0.000001

print("Suma obtenida:", suma)
print("Suma esperada:", 10**7 * 0.0000001)

print(suma)
# Debería dar como resultado 1, pero no lo hace
valor_real = 1.0
error_absoluto = abs(suma - valor_real)
error_relativo = abs(suma - valor_real) / valor_real

print("Error absoluto:", error_absoluto)
print("Error relativo:", error_relativo)



print('\nEjemplo 2 de error de precision en Python')
# Este ejemplo muestra cómo la suma alternada de números puede afectar la precisión.
suma = 0.0
for i in range(1, 1000000):
    suma += ((-1)**i) * 0.000001

print("Suma alternada:", suma)
suma = 1e10 + 1e-5 - 1e10
print("Resultado:", suma)


print('\nEjemplo 3 de error de precision en Python')
suma = 0.0
for i in range(1, 1000000):
    suma += ((-1)**i) * 0.000001

print("Suma alternada:", suma)


print('\nEjemplo 4 de error de precision en Python')
suma = 1e10 + 1e-5 - 1e10
print("Resultado:", suma)

print('\nEjemplo 1 de error de redondeo en Python')
# Este ejemplo demuestra cómo la suma de números que no se pueden representar exactamente en punto flotante (como 0.1) puede acumular errores de redondeo.
suma = 0.0
for i in range(10):
  suma += 0.1

print(suma)
# Debería dar como resultado 1, pero no lo hace
valor_real = 1.0
error_absoluto = abs(suma - valor_real)
error_relativo = abs(suma - valor_real) / valor_real

print("Error absoluto:", error_absoluto)
print("Error relativo:", error_relativo)

print('\nEjemplo 2 de error de redondeo en Python')
# Similar al ejemplo 1, pero con restas en lugar de sumas.
resta = 1.0
for i in range(10):
    resta -= 0.1

print("Resultado de la resta:", resta)

print('\nEjemplo 3 de error de redondeo en Python')
# Este ejemplo muestra cómo la división repetida puede generar errores de redondeo.
valor = 1.0
for i in range(10):
    valor /= 3

print("División repetida:", valor)

print('\nEjemplo 1 de error de truncamiento, en Python')
# Este ejemplo aproxima el valor de e (la base del logaritmo natural) utilizando la serie de Taylor para la función exponencial truncada. Se muestra cómo el truncamiento de la serie introduce un error.
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

print('\nEjemplo 2 de error de truncamiento, en Python')
# Similar al ejemplo 1, pero para la función exponencial negativa.
def exp_neg_aproximado(x, n):
  resultado = 0.0
  for i in range(n):
    resultado += ((-x) ** i) / math.factorial(i)
  return resultado

x = 1.0
n = 6
print("Aproximación:", exp_neg_aproximado(x, n))
print("Valor real:", math.exp(-x))

print('\nEjemplo 3 de error de truncamiento, en Python')
# Aproximación de la función coseno utilizando la serie de Taylor.
def cos_aproximado(x, n):
  resultado = 0.0
  for i in range(n):
    termino = ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)
    resultado += termino
  return resultado

x = math.pi / 6  # 30 grados
n = 5
print("Aproximación:", cos_aproximado(x, n))
print("Valor real:", math.cos(x))

print('\nEjemplo 4 de error de truncamiento, en Python')
# Aproximación de la función logaritmo utilizando la serie de Taylor.
def log_aproximado(x, n):
  resultado = 0.0
  for i in range(1, n + 1):
    resultado += ((-1) ** (i + 1)) * (x ** i) / i
  return resultado

x = 0.5
n = 5
print("Aproximación:", log_aproximado(x, n))
print("Valor real:", math.log(1 + x))

print('\nEjemplo 5 de error de truncamiento, en Python')
# Otro ejemplo de aproximación de la función seno con la serie de Taylor.
import math

def seno_aproximado(x, n):
    resultado = 0.0
    for i in range(n):
        termino = ((-1)**i) * (x**(2*i + 1)) / math.factorial(2*i + 1)
        resultado += termino
    return resultado

angulo = math.pi / 4  # 45 grados
n = 5  # Términos en la serie
print("Aproximación:", seno_aproximado(angulo, n))
print("Valor real:", math.sin(angulo))
