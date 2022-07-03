===============================================
     Crontab para la aliminacion de audit
===============================================

#!/bin/bash
ls /var/log/audit | egrep -v 'audit.log$|audit.log.[1-2]$' | xargs -I '{}' rm -rf /var/log/audit/'{}'


#Formato del crontab
#02 */06 * * * /root/borrarAudit.sh