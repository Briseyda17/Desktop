#Agregar que si escribe la palabra "saludo" le mande un saludo bonito
 
 

while True:
    data = imput("Escribe 'salir' para finalizar en bucle")
    if data.lower() =="salir":
        print("Saliendo del bucle")
        break
    else:
            print(f"Sorry papi, escribiste {data}")
 