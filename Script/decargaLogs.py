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
        Ambiente=self.Obtener_Datos(self.ent1).replace(" ","")
        Api=self.Obtener_Datos(self.ent2).replace(" ","")
        Revision=self.Obtener_Datos(self.ent3).replace(" ","")
        Fecha=self.Obtener_Datos(self.ent4).replace(" ","")
        Ruta='/opt/apigee/var/log/edge-message-processor/messagelogging/baz-prod/'+Ambiente+'/'+Api+'/'+Revision+'/'   
        #Validacion de ruta con un nodo cualquiera
        MP_Onpremise=["10.53.58.105","10.53.58.106","10.53.58.107","10.53.58.108","10.53.58.109","10.53.58.110","10.53.58.111","10.53.58.112","10.53.58.113","10.53.58.114","10.53.58.116","10.53.58.117","10.53.58.118","10.53.58.119","10.80.122.116","10.80.122.117","10.80.122.118","10.80.122.119","10.80.122.120","10.80.122.121","10.80.122.122","10.80.122.123","10.80.122.124","10.80.122.125","10.80.122.126","10.80.122.127","10.80.122.128","10.80.122.129","10.80.122.130"]
        for i in MP_Onpremise:
            Salida=os.popen('sshpass -p "operacionesCLOUD" ssh b1014515@'+i+' "if test -d '+Ruta+'; then echo "OK"; fi"').read().rstrip()
            if Salida:
                print("Conexion "+i)
                os.system('sshpass -p "operacionesCLOUD" ssh -o "StrictHostKeyChecking=no" b1014515@'+i+' cat '+Ruta+'ML-Logging-Archivo-Info/* | egrep -A6 '+Fecha+' > Logs_Info_'+i+'_'+Fecha+'')
                os.system('sshpass -p "operacionesCLOUD" ssh -o "StrictHostKeyChecking=no" b1014515@'+i+' cat '+Ruta+'ML-Logging-Archivo-Error/* | egrep -A6 '+Fecha+' > Logs_Error_'+i+'_'+Fecha+'')
            else:
                print ("Funcion para la validacion de ruta")
                break


    def Log_AWS(self):
        Ambiente=self.Obtener_Datos(self.ent1).replace(" ","")
        Api=self.Obtener_Datos(self.ent2).replace(" ","")
        Revision=self.Obtener_Datos(self.ent3).replace(" ","")
        Fecha=self.Obtener_Datos(self.ent4).replace(" ","")
        Ruta='/opt/apigee/var/log/edge-message-processor/messagelogging/baz-prod/'+Ambiente+'/'+Api+'/'+Revision+'/' 
        MP_AWS=["10.96.65.38","10.96.65.39","10.96.65.40"]
        for i in MP_AWS:
            Salida=os.popen('ssh -i ./APIGEE-PROD-KPS.pem ec2-user@'+i+' "if test -d '+Ruta+'; then echo "OK"; fi"').read().rstrip()
            if Salida:
                os.system('ssh -i ./APIGEE-PROD-KPS.pem ec2-user@'+i+' cat '+Ruta+'ML-Logging-Archivo-Info/* | egrep -A6 '+Fecha+' > Logsaws_Info_'+i+'_'+Fecha+'')
                os.system('ssh -i ./APIGEE-PROD-KPS.pem ec2-user@'+i+' cat '+Ruta+'ML-Logging-Archivo-Error/* | egrep -A6 '+Fecha+' > Logsaws_Error_'+i+'_'+Fecha+'')
            else:
                print ("Funcion para la validacion de ruta")
                break


    def Logs_Tibco(self):
        Ruta=self.Obtener_Datos(self.ent1).replace(" ","")

    
    def Logs_BeneficiosFinancieros(self):
        Microservicio=self.Obtener_Datos(self.ent1).replace(" ","")
        Fecha=self.Obtener_Datos(self.ent2).replace(" ","")


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
            self.Boton=tk.Button(self.vchild,text="Descargar", command=self.Log_AWS)
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
            self.Boton=tk.Button(self.vchild,text="Descargar",command=self.Logs_BeneficiosFinancieros)
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
            self.Boton=tk.Button(self.vchild,text="Descargar",command=self.Logs_Tibco)
            self.Boton.grid(padx=10, pady=10, row=5, column=0) 
               

DescargaLogs()
