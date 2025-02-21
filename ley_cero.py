def en_equilibrio(temp_a, temp_b, temp_c):
    """
    Comprueba si A y B están en equilibrio térmico según la Ley Cero.
    """
    if temp_a == temp_c and temp_b == temp_c:
        return "A y B están en equilibrio térmico."
    else:
        return "A y B NO están en equilibrio térmico."

# Definir temperaturas de A, B y C
temp_a = float(input("Temperatura del sistema A: "))
temp_b = float(input("Temperatura del sistema B: "))
temp_c = float(input("Temperatura del sistema C (referencia): "))

# Comprobación de la Ley Cero
resultado = en_equilibrio(temp_a, temp_b, temp_c)
print(resultado)
