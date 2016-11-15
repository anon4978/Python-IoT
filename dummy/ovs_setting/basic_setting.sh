#!/bin/bash
sudo ovs-vsctl del-br br
sudo ovs-vsctl add-br br
sudo ovs-vsctl set bridge br other-config:hwaddr=00:25:90:06:79:8c
sudo ifconfig br up

sudo ifconfig eth0 up
sudo ifconfig eth1 up
sudo ifconfig eth2 up
sudo ifconfig eth3 up
sudo ifconfig rename3 up




sudo ifconfig eth0 0
sudo ifconfig eth1 0
sudo ifconfig eth2 0
sudo ifconfig eth3 0
sudo ifconfig rename3 0


sudo ifconfig ovs-system 0 

sudo ovs-vsctl add-port br eth0
sudo ovs-vsctl add-port br eth1
sudo ovs-vsctl add-port br eth2
sudo ovs-vsctl add-port br eth3
sudo ovs-vsctl add-port br rename3


sudo ifconfig br 192.0.0.1/24

#sudo route add default gw 192.0.0.1 dev br

#sudo ovs-vsctl set-controller br tcp:192.0.0.200:6633

