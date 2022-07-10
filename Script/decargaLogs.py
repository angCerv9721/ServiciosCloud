from cProfile import label
from re import T
from tkinter import *
from tkinter import ttk
import tkinter as tk
import os.path, os

class DescargaLogs:
    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Descarga de logs")
        self.ventana.geometry('430x100')
        #Botones de menu
        self.Label1=tk.Label(self.ventana,text="Sistema: ")
        self.Label1.grid(padx=10, pady=10, row=0, column=0)
        self.Sistema=ttk.Combobox(self.ventana,state="readonly", values=["On Premise", "AWS", "Beneficios Financieros", "Tibco"])
        self.Sistema.grid(padx=10, pady=10, row=0, column=2)
        self.Boton=tk.Button(self.ventana,text="Aceptar",command=self.menuSistema)
        self.Boton.grid(padx=10, pady=10, row=0, column=3)
        self.estado=True
        self.ventana.mainloop()        
        #Botones de menu
    
    def menuSistema(self):
        opcion=self.Sistema.current()
        if (opcion==0): self.OnPremise()
        if (opcion==1): self.AWs()
        if (opcion==2): self.BeneficiosFinancieros()     
        if (opcion==3): self.Tibco()
    
    def cierraVentana(self):
        if(self.estado==False):
            self.vchild.destroy()
            self.estado=True
    def Obtener_Datos(self,x):
        return x.get()

    def Logs_OnPremise(self):
        Ambiente=self.Obtener_Datos(self.ent1)
        Api=self.Obtener_Datos(self.ent2)
        Revision=self.Obtener_Datos(self.ent3)
        Fecha=self.Obtener_Datos(self.ent4)

    def Log_AWS(self):
        Ambiente=self.Obtener_Datos(self.ent1)
        Api=self.Obtener_Datos(self.ent2)
        Revision=self.Obtener_Datos(self.ent3)
        Fecha=self.Obtener_Datos(self.ent4)


    def Logs_Tibco(self):
        Ruta=self.Obtener_Datos(self.ent1)

    
    def Logs_BeneficiosFinancieros(self):
        Microservicio=self.Obtener_Datos(self.ent1)
        Fecha=self.Obtener_Datos(self.ent2)


    def OnPremise(self):
        self.cierraVentana() 
        if self.estado:
            self.estado=False
            self.vchild=tk.Toplevel(self.ventana)
            self.vchild.geometry('600x300')
            tk.Label(self.vchild, text="On Premise").grid(padx=10, pady=10, row=0, column=0)
            tk.Label(self.vchild, text="Ambiente: ").grid(padx=10, pady=10, row=1, column=0)
            tk.Label(self.vchild, text="Api: ").grid(padx=10, pady=10, row=2, column=0)
            tk.Label(self.vchild, text="Revision: ").grid(padx=10, pady=10, row=3, column=0)
            tk.Label(self.vchild, text="Fecha: ").grid(padx=10, pady=10, row=4, column=0)
            self.ent1=ttk.Combobox(self.vchild,state="readonly",width=55, values=["prod-ext", "prod-int"])
            self.ent1.grid(padx=10, pady=10, row=1, column=1)
            self.ent2=tk.Entry(self.vchild, width=60)
            self.ent2.grid(padx=10, pady=10, row=2, column=1)
            self.ent3=tk.Entry(self.vchild, width=60)
            self.ent3.grid(padx=10, pady=10, row=3, column=1)
            self.ent4=tk.Entry(self.vchild, width=60)
            self.ent4.grid(padx=10, pady=10, row=4, column=1)
            self.Boton=tk.Button(self.vchild,text="Descargar",command=self.Logs_OnPremise)
            self.Boton.grid(padx=10, pady=10, row=5, column=0)    


    def AWs(self):
        self.cierraVentana() 
        if self.estado:
            self.estado=False
            self.vchild=tk.Toplevel(self.ventana)
            self.vchild.geometry('600x300')
            tk.Label(self.vchild, text="AWS").grid(padx=10, pady=10, row=0, column=0)
            tk.Label(self.vchild, text="Ambiente: ").grid(padx=10, pady=10, row=1, column=0)
            tk.Label(self.vchild, text="Api: ").grid(padx=10, pady=10, row=2, column=0)
            tk.Label(self.vchild, text="Revision: ").grid(padx=10, pady=10, row=3, column=0)
            tk.Label(self.vchild, text="Fecha: ").grid(padx=10, pady=10, row=4, column=0)
            self.ent1=ttk.Combobox(self.vchild,state="readonly",width=55, values=["prod-ext", "prod-int"])
            self.ent1.grid(padx=10, pady=10, row=1, column=1)
            self.ent2=tk.Entry(self.vchild, width=60)
            self.ent2.grid(padx=10, pady=10, row=2, column=1)
            self.ent3=tk.Entry(self.vchild, width=60)
            self.ent3.grid(padx=10, pady=10, row=3, column=1)
            self.ent4=tk.Entry(self.vchild, width=60)
            self.ent4.grid(padx=10, pady=10, row=4, column=1)
            self.Boton=tk.Button(self.vchild,text="Descargar")
            self.Boton.grid(padx=10, pady=10, row=5, column=0)    


    def BeneficiosFinancieros(self):
        self.cierraVentana() 
        if self.estado:
            self.estado=False
            self.vchild=tk.Toplevel(self.ventana)
            self.vchild.geometry('430x200')
            tk.Label(self.vchild, text="Beneficios Financieros: ").grid(padx=10, pady=10, row=0, column=0)
            tk.Label(self.vchild, text="Microservicio: ").grid(padx=10, pady=10, row=1, column=0)
            tk.Label(self.vchild, text="Fecha: ").grid(padx=10, pady=10, row=2, column=0)
            self.ent1=ttk.Combobox(self.vchild,state="readonly",width=25, values=["prod-ext", "prod-int"])
            self.ent1.grid(padx=10, pady=10, row=1, column=1)
            self.ent2=tk.Entry(self.vchild, width=30)
            self.ent2.grid(padx=10, pady=10, row=2, column=1)
            self.Boton=tk.Button(self.vchild,text="Descargar")
            self.Boton.grid(padx=10, pady=10, row=5, column=0) 


    def Tibco(self):
        self.cierraVentana() 
        if self.estado:
            self.estado=False
            self.vchild=tk.Toplevel(self.ventana)
            self.vchild.geometry('600x150')
            tk.Label(self.vchild, text="Tibco").grid(padx=10, pady=10, row=0, column=0)
            tk.Label(self.vchild, text="Ruta: ").grid(padx=10, pady=10, row=1, column=0)
            self.ent1=tk.Entry(self.vchild, width=60)
            self.ent1.grid(padx=10, pady=10, row=1, column=1)
            self.Boton=tk.Button(self.vchild,text="Descargar")
            self.Boton.grid(padx=10, pady=10, row=5, column=0) 
               

DescargaLogs()
