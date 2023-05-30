#!/usr/bin/env bash

nohup python /app/dbase/prepara_banco.py >/dev/null 2>&1 &

sleep 5

nohup python /app/filmoteca/filmoteca.py >/dev/null 2>&1 &
