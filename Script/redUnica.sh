#!/bin/bash 
echo ""
echo "=================================================="
echo "                   RED UNICA                      "
echo ""
echo "solo necesitamos el path de desarrollo"
echo "=================================================="
echo ""
echo -n "Reposiroio desarrollo:"
read dev 
dev=`echo $dev | tr -d [:blank:]`
prod=`echo $dev | sed 's/registry.redunica.rke.dev.corp/registry.baz.redunica.rke.corp/g'`
prod=`echo $prod | sed 's/redunica-front-preprod/redunica-front/g'`
echo ""
echo "Descargando en desarrollo"
echo "----------------------------------------------"
docker pull $dev
docker tag $dev $prod
echo ""
echo "Subiendo en produccion"
echo "----------------------------------------------"
docker push $prod
echo ""
echo "Imagen en Desarrollo: $dev"
echo "Imagen en Produccion: $prod"
echo ""