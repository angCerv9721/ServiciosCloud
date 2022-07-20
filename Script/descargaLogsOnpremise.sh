#!/bin/bash
#Funciona para la descarga de logs de los MP_Onp 
#Lista de message para la conexion
#Nodos para Onpremise
MP_Onp[1]='10.53.58.105'
MP_Onp[2]='10.53.58.106'
MP_Onp[3]='10.53.58.107'
MP_Onp[4]='10.53.58.108'
MP_Onp[5]='10.53.58.109'
MP_Onp[6]='10.53.58.110'
MP_Onp[7]='10.53.58.111'
MP_Onp[8]='10.53.58.112'
MP_Onp[9]='10.53.58.113'
MP_Onp[10]='10.53.58.114'
MP_Onp[11]='10.53.58.116'
MP_Onp[12]='10.53.58.117'
MP_Onp[13]='10.53.58.118'
MP_Onp[14]='10.53.58.119'
MP_Onp[15]='10.80.122.116'
MP_Onp[16]='10.80.122.117'
MP_Onp[17]='10.80.122.118'
MP_Onp[18]='10.80.122.119'
MP_Onp[19]='10.80.122.120'
MP_Onp[20]='10.80.122.121'
MP_Onp[21]='10.80.122.122'
MP_Onp[22]='10.80.122.123'
MP_Onp[23]='10.80.122.124'
MP_Onp[24]='10.80.122.125'
MP_Onp[25]='10.80.122.126'
MP_Onp[26]='10.80.122.127'
MP_Onp[27]='10.80.122.128'
MP_Onp[28]='10.80.122.129'
MP_Onp[29]='10.80.122.130'
#Nodos para AWS
MP_AWS[1]='10.96.65.38'
MP_AWS[2]='10.96.65.39'
MP_AWS[3]='10.96.65.40'


#Funcion para la validacion de la ruta antes de la descarga
valida_ruta_Onp(){
    echo `sshpass -p "operacionesCLOUD" ssh  -o "StrictHostKeyChecking=no" b1014515@$1 "if test -d $Ruta; then echo "OK"; fi"` 
}
valida_ruta_AWS(){
    PEM=`find /home/$user/ -name APIGEE-PROD-KPS.pem`
    echo `ssh -i $PEM ec2-user@$1 "if test -d $Ruta; then echo "OK";  fi"` 
}

#Funcion para la descarga de logs
Descarga_Logs_Onpremise(){
    sshpass -p "operacionesCLOUD" ssh -o "StrictHostKeyChecking=no" b1014515@$1 "cat $Ruta/ML-Logging-Archivo-Error/* | egrep -A6 $Fecha" > /home/$user/Log_$Api\_$Ambiente/Logs_Error_$Ambiente\_$Fecha\_$1.txt
    sshpass -p "operacionesCLOUD" ssh -o "StrictHostKeyChecking=no" b1014515@$1 "cat $Ruta/ML-Logging-Archivo-Info/* | egrep -A6 $Fecha" > /home/$user/Log_$Api\_$Ambiente/Logs_Info_$Ambiente\_$Fecha\_$1.txt
}
Descarga_Logs_AWS(){
    ssh -i $PEM ec2-user@$1 "cat $Ruta/ML-Logging-Archivo-Error/* | egrep -A6 $Fecha" > /home/$user/Log_$Api\_$Ambiente/Logs_Error_$Ambiente\_$Fecha\_$1.txt
    ssh -i $PEM ec2-user@$1 "cat $Ruta/ML-Logging-Archivo-Info/* | egrep -A6 $Fecha" > /home/$user/Log_$Api\_$Ambiente/Logs_Info_$Ambiente\_$Fecha\_$1.txt
}


#Funcion para la lectura del arreglo
Read_Array_Onp(){
    for i in `seq  1 ${#MP_Onp[@]}`
    do
        echo "=============================="
        echo "   Conexion ${MP_Onp[$i]}"
        echo "=============================="
        echo ""
        if [ `valida_ruta_Onp "${MP_Onp[$i]}"` ]
        then
            Descarga_Logs_Onpremise "${MP_Onp[$i]}"
        else
            echo ""
            echo "$(tput setaf 1)Valida la ruta: $Ruta"
            echo ""
        fi 
    done
}

Read_Array_AWS(){
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
            echo "$(tput setaf 1)Valida la ruta: $Ruta"
            echo ""
        fi 
    done
}

#Crea un directorio en tu home
Directorio(){
    user=`whoami`
    rm -rf /home/$user//Log_$Api\_$Ambiente/
    mkdir /home/$user//Log_$Api\_$Ambiente/
}

#Menu principal e interactivo
main (){
    #Modo interactivo con el ususario
    echo "============================================"
    echo "             Descarga Logs                  "
    echo "============================================"
    echo ""
    echo -n "Planeta (aws/onp): "
    read Planeta
    echo -n "Ambiente (prod-int/prod-ext): "
    read Ambiente
    echo -n "Api: "
    read Api
    echo -n "Revision: "
    read Revision
    echo -n "Fecha (aaaa-mm-dd): "
    read Fecha
    echo ""
    
    #Formacion de datos
    Planeta=`echo $Planeta | tr -d [:blank:]`
    Api=`echo $Api | tr -d [:blank:]`
    Revision=`echo $Revision | tr -d [:blank:]`
    Ambiente=`echo $Ambiente | tr -d [:blank:]`
    Fecha=`echo $Fecha | tr -d [:blank:]`
    Ruta=/opt/apigee/var/log/edge-message-processor/messagelogging/baz-prod/$Ambiente/$Api/$Revision  
    
    #Validacion de planeta
    Directorio
    case $Planeta in
        aws) Read_Array_AWS;;
        onp) Read_Array_Onp;;
        *) echo "Opcion invalida: \"$Planeta\""
    esac
}
main