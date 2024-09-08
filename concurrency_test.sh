#!/bin/bash

clientes=1
peticiones=50

for j in {1..10}
do
   for i in $(seq 1 $clientes)
   do
      python3 ./simple_client.py $clientes $peticiones $j &
      # sleep 0.5
   done

   wait
done