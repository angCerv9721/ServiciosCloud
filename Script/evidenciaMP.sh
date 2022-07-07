#==================================================
#            Sacar evidencia
#==================================================
#Cuando se cae un MP sacamos evidencia, este script saca
#la evidencia solicitada en el momento
#!/bin/bash
echo ""
echo "Saquemos evidencia --------------------------------------------------"
sudo -u apigee jcmd $(cat /opt/apigee/var/run/edge-message-processor/edge-message-processor.pid) Thread.print > /tmp/thread_print_$(hostname)-$(date +%Y.%m.%d_%H.%M.%S).tdump
top -H -bn5 > /tmp/top_out_$(hostname)-$(date +%Y.%m.%d_%H.%M.%S).txt
echo ""
echo "Evidencia Lista -----------------------------------------------------"
