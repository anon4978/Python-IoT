#!/bin/bash

rm /home/byounguklee/mininet/con_python/normal_packet/output/output_servers_.txt
/home/byounguklee/mininet/con_python/normal_packet/make_data/making_data.sh
cp /home/byounguklee/mininet/con_python/output_txt/config/* /home/byounguklee/mininet/con_python/normal_packet/output/
mkdir /home/byounguklee/mininet/con_python/normal_packet/output/information/
cp /home/byounguklee/mininet/con_python/output_txt/* /home/byounguklee/mininet/con_python/normal_packet/output/information/



#It makes sum of the rates for each link
#and sum of the rates for all link. argument is time_slot_length
##/home/controller/IoT/normal_packet/output/Asum_make.sh 10

#It add the time index to above results.
#If you want, you can change time_length in this shall script.
#Default is 10
##/home/controller/IoT/normal_packet/output/add_time_script.sh



#/home/controller/IoT/normal_packet/output/pwdpwd.sh

