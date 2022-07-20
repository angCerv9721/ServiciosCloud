#!/bin/bash
#Funciona para la descarga de logs de los MP_AWS 
#Lista de message para la conexion
MP_AWS[1]='10.96.65.38'
MP_AWS[2]='10.96.65.39'
MP_AWS[3]='10.96.65.40'
PEM=`find . -name APIGEE-PROD-KPS.pem`


#Funcion para la validacion de la ruta antes de la descarga
valida_ruta_AWS(){
    echo `ssh -i $PEM ec2-user@$1 "if test -d $Ruta; then echo "OK";  fi"` 
}

#Funcion para la descarga de logs
Descarga_Logs_AWS(){
    ssh -i $PEM ec2-user@$1 "cat $Ruta/ML-Logging-Archivo-Error/* | egrep -A6 $Fecha" > /home/$user/Log_$Api\_$Ambiente/Logs_Error_$Ambiente\_$Fecha\_$1.txt
    ssh -i $PEM ec2-user@$1 "cat $Ruta/ML-Logging-Archivo-Info/* | egrep -A6 $Fecha" > /home/$user/Log_$Api\_$Ambiente/Logs_Info_$Ambiente\_$Fecha\_$1.txt
}

#Funcion para la lectura del arreglo
Read_Array(){
    for i in `seq  1 ${#MP_AWS[@]}`
    do
        echo "=============================="
        echo "   Conexion ${MP_AWS[$i]}"
        echo "=============================="
        echo ""
        if [ `valida_ruta_AWS "${MP_AWS[$i]}"` ]
        then
            Descarga_Logs_AWS "${MP_AWS[$i]}"
        else
            echo ""
            echo "Valida la ruta: $Ruta"
            echo ""
        fi 
    done
}

#Crea un directorio en tu home
Directorio(){
    user=`whoami`
    rm -rf /home/$user//Log_$Api\_$Ambiente/
    mkdir /home/$user//Log_$Api\_$Ambiente/
    PEM=`find /home/$user/ -name APIGEE-PROD-KPS.pem`
}

#Menu principal e interactivo
main (){
    echo "============================================"
    echo "             Descarga Logs                  "
    echo "============================================"
    echo ""
    echo -n "Ambiente (prod-int / prod-ext): "
    read Ambiente
    echo -n "Api: "
    read Api
    echo -n "Revision: "
    read Revision
    echo -n "Fecha (aaaa-mm-dd): "
    read Fecha
    echo ""
    Api=`echo $Api | tr -d [:blank:]`
    Revision=`echo $Revision | tr -d [:blank:]`
    Ambiente=`echo $Ambiente | tr -d [:blank:]`
    Fecha=`echo $Fecha | tr -d [:blank:]`
    Ruta=/opt/apigee/var/log/edge-message-processor/messagelogging/baz-prod/$Ambiente/$Api/$Revision 
    Directorio
    Read_Array
}
main