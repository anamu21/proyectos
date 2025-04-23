def calculadora():
    print("Bienvenido a la calculadora")
    print("Selecciona una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    while True:
        try:
            operacion = int(input("Ingresa el número de la operación (1-4): "))
            if operacion in [1, 2, 3, 4]:
                break
            else:
                print("Opción no válida. Intenta de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor ingresa un número.")

    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if operacion == 1:
        resultado = num1 + num2
        operacion_str = "suma"
    elif operacion == 2:
        resultado = num1 - num2
        operacion_str = "resta"
    elif operacion == 3:
        resultado = num1 * num2
        operacion_str = "multiplicación"
    elif operacion == 4:
        if num2 != 0:
            resultado = num1 / num2 
            operacion_str = "división"
        else:
            return "Error: División por cero no permitida."

    return f"El resultado de la {operacion_str} es: {resultado}"
if __name__ == "__main__":
    print(calculadora())
