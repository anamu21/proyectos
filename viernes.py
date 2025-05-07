def menu():
    print("Bienvenido al sistema de calificaciones")
    print("\nMenú principal:")
    print("1. Verificar estado de aprobación")
    print("2. Calcular promedio de calificaciones")
    print("3. Contar calificaciones mayores a un valor")
    print("4. Verificar y contar calificaciones específicas")
    print("5. Salir")
        
    opcion = input("Seleccione una opción (1-5): ")
    
    if opcion == "1":
        verificacion()
    elif opcion == "2":
        promedio()
    elif opcion == "3":
        mayores()
    elif opcion == "4":
        contador()
    elif opcion == "5":
        print("Gracias por usar el sistema. ¡Hasta luego!")

    else:
        print("Opción no válida. Por favor, seleccione 1-5.")

# Verificar si aprobaste o reprobaste
def verificacion():
    while True:
        verificacion = float(input("Ingresa una calificacion: "))
        if verificacion >=60:
            print("¡Felicidades! Has aprobado.")
        else:
            print("Has reprobado. Necesitas esforzarte más.")


calificaciones = []

# Calcular y mostrar el promedio
def promedio () : 
    # Obtener las calificaciones
    inicio = input("Ingrese las calificaciones separadas por comas (0-100): ")
    calificaciones = [float(c.strip()) for c in inicio.split(",")]
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"\nEl promedio de las {len(calificaciones)} calificaciones es: {promedio:.2f}")

def mayores():
    #Asegurar de que el valor esté entre 0 y 100
    valor = float(input("\nIngrese un valor válido para contar cuántas calificaciones son mayores: "))

    mayores = sum(1 for c in calificaciones if c > valor)
    print(f"Hay {mayores} calificaciones mayores que {valor}.")

def contador():
    #Buscar una calificación específica y contar cuántas veces aparece
    especifica = float(input("\nIngrese una calificación específica a buscar: "))

    contador = calificaciones.count(especifica)
    if contador > 0:
        print(f"La calificación {especifica} aparece {contador} veces.")
    else:
        print(f"La calificación {especifica} no aparece en la lista.")

menu()
# se cambia de main a menu 