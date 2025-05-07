password = "python123"

userpass = input ("ingrese su contraseña: ")

while password != userpass : 
    userpass = input (" Clave incorrecta")
    if userpass == password :
       break    

if userpass == password : 
    print("Clave correcta")    