import tkinter #IMPORTAR LA LIBRERIA

ventana = tkinter.Tk() #CREA LA VENTANA
ventana.geometry("400x300") #PERMITE DEFINIR MEDIDAS DE VENTANA

etiqueta = tkinter.Label(ventana, text = "Hola Mundo", bg="blue") #SE DEFINE UNA ETIQUETA
etiqueta.pack() #PERMITE MOSTRAR LA ETIQUETA.

def saludo(nombre): #FUNCION DE PRUEBA PARA SER EJECUTADA POR UN BOTON
    print(f"Hola {nombre} :)")

boton1 = tkinter.Button(ventana, text = "Presiona", command = lambda: saludo("David")) #SE DEFINE UN BOTON. CON "command" SE PUEDE DAR FUNCIONES
boton1.pack() #MUESTRA EL BOTON EN LA VENTANA

cajaTexto = tkinter.Entry(ventana)
cajaTexto.pack()

ventana.mainloop() #REGISTRA LOS EVENTOS DE LA VENTANA