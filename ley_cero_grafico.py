import matplotlib
matplotlib.use("Agg")  # Usa un backend sin interfaz gráfica
import matplotlib.pyplot as plt

def convertir_a_kelvin(temp, escala):
    """Convierte una temperatura dada a Kelvin según la escala seleccionada."""
    if escala == "C":
        return temp + 273.15
    elif escala == "F":
        return (temp - 32) * 5/9 + 273.15
    elif escala == "R":
        return temp * 5/9
    elif escala == "K":
        return temp
    else:
        raise ValueError("Escala no válida")

# Entrada de datos
escala = input("👉 Ingresa la escala (C/F/R/K): ").upper()
temp_a = float(input("🌡️ Temperatura A: "))
temp_b = float(input("🌡️ Temperatura B: "))
temp_c = float(input("🌡️ Temperatura C (Referencia): "))

# Conversión a Kelvin
temp_a_k = convertir_a_kelvin(temp_a, escala)
temp_b_k = convertir_a_kelvin(temp_b, escala)
temp_c_k = convertir_a_kelvin(temp_c, escala)

# Graficar
etiquetas = ["A", "B", "C"]
valores = [temp_a_k, temp_b_k, temp_c_k]

plt.bar(etiquetas, valores, color=['blue', 'green', 'red'])
plt.xlabel("Sistemas")
plt.ylabel("Temperatura en Kelvin")
plt.title("Visualización de la Ley Cero de la Termodinámica")

# Guardar la imagen en lugar de mostrarla
plt.savefig("grafico_ley_cero.png")  
print("📊 Gráfico guardado como 'grafico_ley_cero.png'. Revisa el archivo en el explorador de archivos.")


