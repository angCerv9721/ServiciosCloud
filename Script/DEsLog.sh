#!/bin/bash
#Lista de message
MP[1]='10.53.58.105'
MP[2]='10.53.58.106'
MP[3]='10.53.58.107'
MP[4]='10.53.58.108'
MP[5]='10.53.58.109'
MP[6]='10.53.58.110'
MP[7]='10.53.58.111'
MP[8]='10.53.58.112'
MP[9]='10.53.58.113'
MP[10]='10.53.58.114'
MP[11]='10.53.58.116'
MP[12]='10.53.58.117'
MP[13]='10.53.58.118'
MP[14]='10.53.58.119'
MP[15]='10.80.122.116'
MP[16]='10.80.122.117'
MP[17]='10.80.122.118'
MP[18]='10.80.122.119'
MP[19]='10.80.122.120'
MP[20]='10.80.122.121'
MP[21]='10.80.122.122'
MP[22]='10.80.122.123'
MP[23]='10.80.122.124'
MP[24]='10.80.122.125'
MP[25]='10.80.122.126'
MP[26]='10.80.122.127'
MP[27]='10.80.122.128'
MP[28]='10.80.122.129'
MP[29]='10.80.122.130'

#Menu para la lectura de campos
echo "============================================"
echo "            Descarga Logs                   "
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

#Validamos la ruta antes de la descarga de logs
valida_ruta(){
    echo `sshpass -p "operacionesCLOUD" ssh  -o "StrictHostKeyChecking=no" b1014515@$1 "if test -d $Ruta; then echo "OK"; fi"` 
}

#Comando para la descarga de logs
Descarga_Logs(){
    sshpass -p "operacionesCLOUD" ssh -o "StrictHostKeyChecking=no" b1014515@$1 "cat $Ruta/ML-Logging-Archivo-Error/* | egrep -A6 $Fecha" > ./LogsDescargos_$Api/Logs_Error_$Ambiente\_$Fecha\_$1.txt
    sshpass -p "operacionesCLOUD" ssh -o "StrictHostKeyChecking=no" b1014515@$1 "cat $Ruta/ML-Logging-Archivo-Info/* | egrep -A6 $Fecha" > ./LogsDescargos_$Api/Logs_Info_$Ambiente\_$Fecha\_$1.txt
}

#Creacion de directorio donde se alojan los logs
Crea_Dir(){
    if test -d ./LogsDescargos_$Api/
    then
        rm -rf LogsDescargos_$Api/*
    else
        mkdir  LogsDescargos_$Api
    fi
}

main (){
    for i in `seq  1 ${#MP[@]}`
    do
        echo "Conexion ${MP[$i]}"
        if [ `valida_ruta "${MP[$i]}"` ]
        then
            Descarga_Logs "${MP[$i]}"
        else
            echo  "Valida la ruta: $Ruta"
        fi 
    done
}

Crea_Dir
main