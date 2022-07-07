#!/bin/bash
#Realiza pruebas deconexion por nc mediand el ssh
#Verificado
> Salida_Nutanix_zonaB.txt
for i in `cat ./NODOS.txt`
do
    echo "======================================================================" >> Salida_Nutanix_zonaB.txt
    echo "             Nodo $i                             " >> Salida_Nutanix_zonaB.txt
    echo "=======================================================================" >> Salida_Nutanix_zonaB.txt
    echo "" >> Salida_Nutanix_zonaB.txt
    echo "Conexion al Nodo $i"
    timeout 40 sshpass -p 'operacionesCLOUD' ssh -o "StrictHostKeyChecking=no" b181656@$i "date" &>> Salida_Nutanix_zonaB.txt
    echo ""
    echo "CONEXION">> Salida_Nutanix_zonaB.txt
    timeout 40 sshpass -p 'operacionesCLOUD' ssh -o "StrictHostKeyChecking=no" b181656@$i "nc -zv 10.53.21.136 123" &>> Salida_Nutanix_zonaB.txt
    echo "" >> Salida_Nutanix_zonaB.txt
done 
sed -i '/+---- WARNING - WARNING - WARNING - WARNING - WARNING - WARNING - WARNING -----+/d' Salida_Nutanix_zonaB.txt
sed -i '/|                                                                              |/d' Salida_Nutanix_zonaB.txt 
sed -i '/|                Sistema operativo protegido y monitoreado por                 |/d' Salida_Nutanix_zonaB.txt 
sed -i '/|                  Seguridad y Cumplimiento de Banco Azteca.                   |/d' Salida_Nutanix_zonaB.txt 
sed -i '/|          Este es un equipo restringido, cualquier mal uso del mismo          |/d' Salida_Nutanix_zonaB.txt 
sed -i '/|                 sera reportado a las autoridades competentes                 |/d' Salida_Nutanix_zonaB.txt 
sed -i '/|                                                                              |/d' Salida_Nutanix_zonaB.txt 
sed -i '/+---- WARNING - WARNING - WARNING - WARNING - WARNING - WARNING - WARNING -----+/d' Salida_Nutanix_zonaB.txt 
