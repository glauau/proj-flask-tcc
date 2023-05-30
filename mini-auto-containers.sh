#!/usr/bin/env bash

echo -e "
Menu:

[ 1 ] - Build da imagem
[ 2 ] - Roda o container
[ 3 ] - Remove containers parados
[ 4 ] - Remove imagem criada
Digite: 
"; read OPC

case $OPC in 
1) nohup docker build -q -t app-teste . > temp 2>&1 && egrep "sha256:" temp | sed 's/s.*://' > image ;; 
2) IMAGEM="$(cat image)" && docker run -p 5000:5000 $IMAGEM ;;
3) docker container prune -f ;;
4) IMAGEM="$(cat image)" && docker image rmi -f $IMAGEM ;;
esac
