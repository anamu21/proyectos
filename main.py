def acortar_texto(texto, max_longitud):
    # Verificar si el texto es más largo que el límite permitido
    if len(texto) > max_longitud:
        # Recortar el texto y agregar puntos suspensivos
        return texto[:max_longitud - 3] + "..."
    else:
        # Si el texto no supera el límite, devolverlo tal cual
        return texto

# Ejemplo de uso
texto_largo = "Este es un texto largo que necesita ser acortado."
texto_corto = "Hola"

# Resultados
resultado_largo = acortar_texto(texto_largo, 20)
resultado_corto = acortar_texto(texto_corto, 20)

print("Texto largo acortado:", resultado_largo)
print("Texto corto:", resultado_corto)
