#!/bin/bash


a=$(pwd)
b=$1 # all data number
echo $a
echo $b
#python /home/byounguklee/mininet/con_python/cloud/Rest_API_Python/HttpClient/post_processing/data_searching_and_sum_back_up.py $a $b
python /home/byounguklee/mininet/con_python/cloud/Rest_API_Python/HttpClient/post_processing/data_searching_and_sum_back_up_link.py $a $b
