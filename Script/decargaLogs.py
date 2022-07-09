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


    def OnPremise(self):
        self.cierraVentana() 
        if self.estado:
            self.estado=False
            self.vchild=tk.Toplevel(self.ventana)
            self.vchild.geometry('430x350')
            tk.Label(self.vchild, text="On Premise").grid(padx=10, pady=10, row=0, column=0)
            tk.Label(self.vchild, text="Ambiente: ").grid(padx=10, pady=10, row=1, column=0)
            tk.Label(self.vchild, text="Api: ").grid(padx=10, pady=10, row=2, column=0)
            tk.Label(self.vchild, text="Revision: ").grid(padx=10, pady=10, row=3, column=0)
            tk.Label(self.vchild, text="Fecha: ").grid(padx=10, pady=10, row=4, column=0)
            


    def AWs(self):
        self.cierraVentana() 
        \
        if self.estado:
            self.estado=False
            self.vchild=tk.Toplevel(self.ventana)
            self.vchild.geometry('430x100')
        

    def BeneficiosFinancieros(self):
        self.cierraVentana() 
        if self.estado:
            self.estado=False
            self.vchild=tk.Toplevel(self.ventana)
            self.vchild.geometry('430x100')
        

    def Tibco(self):
        self.cierraVentana() 
        if self.estado:
            self.estado=False
            self.vchild=tk.Toplevel(self.ventana)
            self.vchild.geometry('430x100')
        
    

DescargaLogs()
