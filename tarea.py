"""Clasificar edades
Pide al usuario su edad y muestra:
"Eres un niño" si tiene menos de 12 años,
"Eres un adolescente" si tiene entre 12 y 17 años,
"Eres un adulto" si tiene entre 18 y 59 años,
"Eres un adulto mayor" si tiene 60 años o más."""

# Pedir al usuario que ingrese su edad
edad = int(input("Por favor, ingresa tu edad: "))

# Clasificar la edad según los rangos dados
if edad < 12:
    print("Eres un niño")
elif 12 <= edad <= 17:
    print("Eres un adolescente")
elif 18 <= edad <= 59:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")