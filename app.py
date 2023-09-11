import tkinter as tk
import customtkinter as ctk

if __name__ == '__main__':
    #Configuracion de la venta.
    ctk.set_appearance_mode("light")
    ventana = ctk.CTk()
    ventana.geometry('1000x700')

    #Creacion de los objetos en la interfaz grafica
    lb_titulo = ctk.CTkLabel(ventana,text='COTIZADOR CASA RENEE S.A.',font=('Arial',30,'bold'))
    lb_titulo.pack()

    #Creando Frame para captar datos del cliente.
    frame_cliente = ctk.CTkFrame(ventana)
    frame_cliente.pack()
    lb_cliente = ctk.CTkLabel(frame_cliente,text='CLIENTE',font=('Arial',20))
    lb_cliente.grid()
    et_cliente = ctk.CTkEntry(frame_cliente,placeholder_text='Inserte el nombre del cliente',width=500)
    et_cliente.grid()


    #Creando Frame para aplicar CRUD a los datos de la cotización
    frame_crud = ctk.CTkFrame(ventana,width=1000,height=300)
    frame_crud.pack()
    lb_descripcion = ctk.CTkLabel(frame_crud,text='Descripción Producto',font=('Arial',20))
    lb_descripcion.grid(row=0,column=0,padx=10)
    et_descripcion = ctk.CTkEntry(frame_crud,placeholder_text="Introduce el nombre del producto aquí",width=500)
    et_descripcion.grid(row=0,column=1)

    lb_cantidad = ctk.CTkLabel(frame_crud,text='Cantidad',font=('Arial',20))
    lb_cantidad.grid(row=1,column=0)
    et_cantidad = ctk.CTkEntry(frame_crud,placeholder_text="Introduce cantidad",width=500)
    et_cantidad.grid(row=1,column=1)

    lb_precio = ctk.CTkLabel(frame_crud,text='Precio Unitario',font=('Arial',20))
    lb_precio.grid(row=2,column=0)
    et_precio = ctk.CTkEntry(frame_crud,placeholder_text='Introduce precio unitario',width=500)
    et_precio.grid(row=2,column=1)
    ventana.mainloop()