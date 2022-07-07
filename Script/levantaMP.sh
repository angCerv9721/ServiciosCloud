#==================================================
#            Levanta MP (Mata procesos) 
#==================================================
#Cuando los MP se encuentran abajo y es necesario matar procesos
#Verificado
#!/bin/bash
echo "================================="
echo "           Comenzando            "
echo "================================="
ps -fea |grep '^apigee' | awk '{print $2}' | xargs kill -9
/opt/apigee/apigee-service/bin/apigee-all start
echo ""
echo "================================="
echo "        Estado de los MP         "
echo "================================="
/opt/apigee/apigee-service/bin/apigee-all status
echo ""
echo "================================="
echo "       Estado de la memoria      "
echo "================================="
echo ""
free -h ; sync; echo 3 > /proc/sys/vm/drop_caches; free -h
echo ""
echo "================================="
echo "             Termine             "
echo "================================="