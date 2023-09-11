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
    frame_cliente.pack(pady=20)
    lb_cliente = ctk.CTkLabel(frame_cliente,text='Cliente',font=('Arial',20))
    lb_cliente.grid(row=0,column=0,padx=10)
    et_cliente = ctk.CTkEntry(frame_cliente,placeholder_text='Inserte el nombre del cliente',width=500)
    et_cliente.grid(row=0,column=1)
    lb_ruc = ctk.CTkLabel(frame_cliente,text='RUC',font=('Arial',20))
    lb_ruc.grid(row=1,column=0,padx=10)
    et_ruc = ctk.CTkEntry(frame_cliente,placeholder_text='Inserte un RUC o el número de cédula',width=500)
    et_ruc.grid(row=1,column=1)
    lb_telefono_1 = ctk.CTkLabel(frame_cliente  ,text='Teléfono 1',font=('Arial',20))
    lb_telefono_1.grid(row=0,column=2,padx=10)
    et_elefono_1 = ctk.CTkEntry(frame_cliente,placeholder_text='999-9999',width=200)
    et_elefono_1.grid(row=0,column=3)
    lb_telefono_2 = ctk.CTkLabel(frame_cliente  ,text='Teléfono 2',font=('Arial',20))
    lb_telefono_2.grid(row=1,column=2,padx=10)
    et_elefono_2 = ctk.CTkEntry(frame_cliente,placeholder_text='999-9999',width=200)
    et_elefono_2.grid(row=1,column=3)
    lb_correo = ctk.CTkLabel(frame_cliente  ,text='Email',font=('Arial',20))
    lb_correo.grid(row=2,column=0,padx=10)
    et_elefono_1 = ctk.CTkEntry(frame_cliente,placeholder_text='correo@gmail.com',width=500)
    et_elefono_1.grid(row=2,column=1)


    #Creando Frame para aplicar CRUD a los datos de la cotización
    frame_crud = ctk.CTkFrame(ventana,width=1000,height=300)
    frame_crud.pack()
    lb_descripcion = ctk.CTkLabel(frame_crud,text='Descripción',font=('Arial',20))
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