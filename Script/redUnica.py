from tkinter import *
import tkinter as tk
import os.path, os

class Despliegue_RedUnica:
    def __init__(self):
        #Forma de la ventana
        self.redUnica=tk.Tk()
        self.redUnica.title("Despliegue Red Unica")
        self.redUnica.geometry('780x110')
        #Etiqueta
        self.label1=tk.Label(self.redUnica, text="Inserta el path de desarrollo:")
        self.label1.grid(padx=10, pady=10, row=0, column=0)
        #Las cajas de entrada
        self.entrada1=tk.Entry(self.redUnica, width=60)
        self.entrada1.grid(padx=10, pady=10, row=0, column=2)
        #Boton 
        self.boton1=tk.Button(self.redUnica,text="Aceptar" , command=self.Linux,width=10).place(x=200, y=70)
        #self.boton2=tk.Button(self.redUnica,text="Cerrar" , command=self.CerrarVentana(self.redUnica),width=10).place(x=280, y=70)
        self.redUnica.mainloop()

    def Linux(self):
        dev=self.entrada1.get().replace(" ","")
        prod=dev.replace("registry.redunica.rke.dev.corp","registry.baz.redunica.rke.corp")
        prod=prod.replace("redunica-front-preprod","redunica-front")
        os.system('echo ""')
        os.system('echo "Descargando Imagen ------------------------"')
        os.system('echo ""')
        os.system('docker pull '+dev)
        os.system('docker tag '+dev+' '+prod)
        os.system('echo ""')
        os.system('echo "Subiendo Imagen ------------------------"')
        os.system('echo ""')
        os.system('docker push '+prod)
        os.system('docker rmi '+dev+' '+prod)
        os.system('echo ""')
        os.system('echo ""')
        print("Imagen en desarrollo: " +dev)
        print ("Imagen en produccion: " +prod)

Despliegue_RedUnica()
