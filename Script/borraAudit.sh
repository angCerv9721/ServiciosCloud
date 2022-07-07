#!/bin/bash
#===============================================
#     Crontab para la aliminacion de audit
#===============================================
#Con este linea de comando, borramos los audit, dejando unicamente  los tres primeros resgistron
#Verificado
ls /var/log/audit | egrep -v 'audit.log$|audit.log.[1-2]$' | xargs -I '{}' rm -rf /var/log/audit/'{}'


#Formato del crontab
#02 */06 * * * /root/borrarAudit.sh