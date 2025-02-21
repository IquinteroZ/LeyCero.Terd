def convertir_a_kelvin(temp, escala):
    """Convierte una temperatura dada a Kelvin según la escala seleccionada."""
    if escala == "C":
        return temp + 273.15  # Celsius a Kelvin
    elif escala == "F":
        return (temp - 32) * 5/9 + 273.15  # Fahrenheit a Kelvin
    elif escala == "R":
        return temp * 5/9  # Rankine a Kelvin
    elif escala == "K":
        return temp  # Kelvin ya está en la unidad correcta
    else:
        raise ValueError("Escala no válida")

def en_equilibrio(temp_a, temp_b, temp_c):
    """Comprueba si A y B están en equilibrio térmico con C (Ley Cero)."""
    if temp_a == temp_c and temp_b == temp_c:
        return "✅ A y B están en equilibrio térmico."
    else:
        return "❌ A y B NO están en equilibrio térmico."

# Selección de la escala antes de pedir temperaturas
print("\n🌡️ Bienvenido al comprobador de la Ley Cero de la Termodinámica.")
print("📌 Por favor, selecciona la escala en la que ingresarás las temperaturas:")
print("   [C] Celsius | [F] Fahrenheit | [R] Rankine | [K] Kelvin")

escala = input("\n👉 Ingresa la letra de la escala (C/F/R/K): ").upper()

# Verificar si la escala ingresada es válida
if escala not in ["C", "F", "R", "K"]:
    print("\n⚠️ Error: Escala no válida. Reinicia el programa e intenta de nuevo.")
    exit()

# Mensaje de confirmación
print(f"\n✅ Has seleccionado la escala: {escala}")

# Entrada de temperaturas
try:
    print(f"\nAhora ingresa las temperaturas en {escala}:")
    temp_a = float(input("🌡️ Temperatura del sistema A: "))
    temp_b = float(input("🌡️ Temperatura del sistema B: "))
    temp_c = float(input("🌡️ Temperatura del sistema C (referencia): "))

    # Conversión a Kelvin
    temp_a_k = convertir_a_kelvin(temp_a, escala)
    temp_b_k = convertir_a_kelvin(temp_b, escala)
    temp_c_k = convertir_a_kelvin(temp_c, escala)

    # Comprobación de la Ley Cero
    resultado = en_equilibrio(temp_a_k, temp_b_k, temp_c_k)
    print("\n🔎 RESULTADO:")
    print(resultado)

except ValueError:
    print("\n⚠️ Error: Ingresa valores numéricos válidos para las temperaturas.")
