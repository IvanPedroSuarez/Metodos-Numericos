# Valor real (supongamos que es el resultado teórico correcto)
valor_real = 3.141592653589793  # Valor de pi

# Valor aproximado (podría ser el resultado de un cálculo numérico)
valor_aproximado = 3.14

# Cálculo del error absoluto
error_absoluto = abs(valor_real - valor_aproximado)
print(f"Error absoluto: {error_absoluto}")

# Cálculo del error relativo
error_relativo = error_absoluto / abs(valor_real)
print(f"Error relativo: {error_relativo:.10f}")  # Mostramos 10 decimales

print('Nada de nada')