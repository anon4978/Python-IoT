#!/bin/bash

for a in {1..100};do

	ssh pi@192.0.0.111 echo "fuck $a" &

done
