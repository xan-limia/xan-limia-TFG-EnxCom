#!/bin/bash

clientes=5
peticiones=100

for i in $(seq 1 $clientes)
do
    python3 ./context_test.py $clientes $peticiones $i &
    # sleep 0.5
done

wait
