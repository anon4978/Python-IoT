#!/bin/bash


ssh server@193.0.0.11 rm ./normal_at_client.sh
ssh server@193.0.0.11 rm ./normal_at_server.sh
ssh server@193.0.0.11 rm ./normal_number.py
scp /home/controller/IoT/normal_packet/normal_at_server.sh server@193.0.0.11:normal_at_server.sh
scp /home/controller/IoT/normal_packet/normal_at_client.sh server@193.0.0.11:normal_at_client.sh
scp /home/controller/IoT/normal_packet/normal_number.py server@193.0.0.11:normal_number.py
#scp /home/controller/IoT/normal_packet/normal_number.py server@193.0.0.11:normal_number.py

ssh server@193.0.0.21 rm ./normal_at_client.sh
ssh server@193.0.0.21 rm ./normal_at_server.sh
ssh server@193.0.0.21 rm ./normal_number.py
scp /home/controller/IoT/normal_packet/normal_at_server.sh server@193.0.0.21:normal_at_server.sh
scp /home/controller/IoT/normal_packet/normal_at_client.sh server@193.0.0.21:normal_at_client.sh
scp /home/controller/IoT/normal_packet/normal_number.py server@193.0.0.21:normal_number.py
#scp /home/controller/IoT/normal_packet/normal_number.py server@193.0.0.21:normal_number.py

ssh server@193.0.0.31 rm ./normal_at_client.sh
ssh server@193.0.0.31 rm ./normal_at_server.sh
ssh server@193.0.0.31 rm ./normal_number.py
scp /home/controller/IoT/normal_packet/normal_at_server.sh server@193.0.0.31:normal_at_server.sh
scp /home/controller/IoT/normal_packet/normal_at_client.sh server@193.0.0.31:normal_at_client.sh
scp /home/controller/IoT/normal_packet/normal_number.py server@193.0.0.31:normal_number.py
#scp /home/controller/IoT/normal_packet/normal_number.py server@193.0.0.31:normal_number.py

ssh server@193.0.0.41 rm ./normal_at_client.sh
ssh server@193.0.0.41 rm ./normal_at_server.sh
ssh server@193.0.0.41 rm ./normal_number.py
scp /home/controller/IoT/normal_packet/normal_at_server.sh server@193.0.0.41:normal_at_server.sh
scp /home/controller/IoT/normal_packet/normal_at_client.sh server@193.0.0.41:normal_at_client.sh
scp /home/controller/IoT/normal_packet/normal_number.py server@193.0.0.41:normal_number.py
#scp /home/controller/IoT/normal_packet/normal_number.py server@193.0.0.41:normal_number.py


