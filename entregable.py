# Recopilación de datos de entrada
print("¡¡Hola, Bienvenido a Rainbow Shop!!")
nombre = input("¿Cual es tu nombre?: ")
nombreproducto = input("Ingresa el nombre del producto que deseas comprar? :")


# se crea bucle para evitar que el usuario coloque caracteres no deseados y asi evitar errores
while True:
    
    precioUnitario=input("Cual es el precio unitario del producto?")
    if not  precioUnitario.isalpha():
        if float(precioUnitario) >0 :
            break
        else:
            print("un numero positivo mayor a cero")
            continue
    else:
        print("por favor solo numeros")

cantidadProductos = int(input("Ingrese la cantidad que desea comprar de este producto: "))

while cantidadProductos < 1:
    print(" la cantidad debe ser superior a 0" + " " + (nombreproducto))
    print(" Cantidad incorrecta, ingresa otro ")
    cantidadProductos=float(input()) 

preciototal = cantidadProductos * float(precioUnitario)  
print(f"cantidad producto-> {int(cantidadProductos)} y \tprecioUnitario es-> {str(precioUnitario)} y \tprecioTotal{preciototal}")

print(f"{nombre} el precio total del producto que deseas comprar {nombreproducto} = {preciototal}")


#Se uso una condicional para que despues de cierta cantidad de producto adquirido proporcione un descuento
if cantidadProductos >=12:
    descuento = float(input("Que porcentaje de descuento le vas a aplicar: "))
    descuentot = preciototal * (descuento/100)
    descuentoF = preciototal - descuentot
    print(f"{nombre} el precio con descuento de {nombreproducto} es : {str(descuentoF)}")

    unidadconD = descuentoF / cantidadProductos

    print("\nEsta fue tu compra: ")
    print("\nCompraste" + " " + str(cantidadProductos) + " " + str(nombreproducto))
    print("Cada unidad te salió en:" + str(unidadconD))
    print("Te ahorraste" + " " + str(descuentot))
    print("¡Gracias por tu compra!")

else:
    print("La compra minima para el descuento es de 20 unidades")  
    print("\nEsta fue tu compra: ")
    print("\nCompraste " + " " + str(cantidadProductos) + " " + str(nombreproducto))
    print("¡Gracias por tu compra!")