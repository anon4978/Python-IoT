#!/bin/bash

#ssh pi@$1 wget https://iperf.fr/download/source/iperf-2.0.8-source.tar.gz
#ssh pi@$1 tar -xvf iperf-2.0.8-source.tar.gz
#ssh pi@$1 cd iperf-2.0.8

#ssh pi@$1 cd iperf-2.0.8; ./configure
#ssh pi@$1 cd iperf-2.0.8; make
#ssh pi@$1 cd iperf-2.0.8; sudo make install

echo "$1"
ssh pi@$1 iperf -v 
