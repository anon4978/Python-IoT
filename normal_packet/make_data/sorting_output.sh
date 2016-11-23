#!/bin/bash

#################################################

IFS=',' read -r -a input_length_path <<< $(cat /home/byounguklee/mininet/con_python/output_txt/output_link_length.txt)

echo "length_path"
echo ${input_length_path[@]}
echo "number line"
echo ${#input_length_path[@]}
number_line=${#input_length_path[@]} 


###########################################
################# ip_mean ################# 
p=0
while read line
do

p=$(expr $p + 1)
IFS=',' read -r -a array_$p <<< "$line"

done < /home/byounguklee/mininet/con_python/output_txt/output_ip_mean.txt



echo "array ip_mean result"

for ((s=1; s<=number_line ;s++))
do
eval a='$'{array_$s[@]}
echo $a

done

################################################## 
################# ip_port ################# 
p=0
while read line
do

p=$(expr $p + 1)
IFS=',' read -r -a port_$p <<< "$line"

done < /home/byounguklee/mininet/con_python/output_txt/output_port.txt



echo "array ip_mean result"

for ((s=1; s<=number_line ;s++))
do
eval a='$'{port_$s[@]}
echo $a

done

############################################ 
#################  ip_link ################# 
 
p=0
while read line
do

p=$(expr $p + 1)
IFS=',' read -r -a array_link_$p <<< "$line"

done < /home/byounguklee/mininet/con_python/output_txt/output_ip_link.txt


echo "array ip_link result"

for ((s=1; s<=number_line ;s++))
do
eval a='$'{array_link_$s[@]}
echo $a

done




##################################################
###########sorting accroding to link ############# 

	

for ((s=1; s<=number_line ;s++))
do
e=$(expr ${s} - 1)

eval d='$'{input_length_path[$e]}

	for ((p=2; p<=$(expr ${d} + 1) ;p++))
	do

	eval a='$'{array_$s[0]}
	eval b='$'{array_$s[1]}
	eval c='$'{array_link_$s[$p]}
	eval e='$'{port_$s[0]}
	eval f='$'{port_$s[1]}

	mkdir /home/byounguklee/mininet/con_python/normal_packet/output/$c/
	cat /home/byounguklee/mininet/con_python/normal_packet/output/output_servers_${a}_${b}_${e}_${f}.txt >> /home/byounguklee/mininet/con_python/normal_packet/output/$c/output_servers_${a}_${b}_${e}_${f}.txt
	cat /home/byounguklee/mininet/con_python/normal_packet/output/output_clients_${a}_${b}_${e}_${f}.txt >> /home/byounguklee/mininet/con_python/normal_packet/output/$c/output_clients_${a}_${b}_${e}_${f}.txt


	done

done


#delete previous existing data

mkdir /home/byounguklee/mininet/con_python/normal_packet/output/original/
mv /home/byounguklee/mininet/con_python/normal_packet/output/*.txt /home/byounguklee/mininet/con_python/normal_packet/output/original/
