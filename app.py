import tkinter as tk
import customtkinter as ctk
ctk.set_appearance_mode("light")
ventana = ctk.CTk()
lb_titulo = ctk.CTkLabel(ventana,text='COTIZADOR CASA RENEE S.A.',)
lb_titulo.pack()
ventana.geometry('1000x700')
ventana.mainloop()