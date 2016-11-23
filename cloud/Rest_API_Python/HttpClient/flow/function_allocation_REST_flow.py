'''
Created on Mar 31, 2016

@author: nimdrak
'''
#from HttpClient import flow.function_routing_rule_post_flow
import function_routing_rule_post_flow
import sys
sys.path.append('/home/byounguklee/mininet/con_python/cloud/Rest_API_Python/HttpClient/')
 
import function_allocation_routing_path
import function_routing_rule_post
import function_ovs_translation_from_number_to_id



def function_main(algo_output1,port_output1):    

#    algo_output1 = [] 
#    for a in range(1,len(sys.argv)):
#        algo_output1.append(sys.argv[a])
#    print algo_output1    
#    algo_output1 = ['192.0.0.121/32','2','4','3','192.0.0.130/32']

#########################################################
#####generating routing port accoding to algo_output##### 
#########################################################
    print 'start is input :', algo_output1
    dst_port_list_algo_output=[]
    src_port_list_algo_output=[]

    dst_port_list_algo_output = function_allocation_routing_path.Allocation_routing_dst_port(algo_output1)
    src_port_list_algo_output = function_allocation_routing_path.Allocation_routing_src_port(algo_output1)
 
    print '\n'
    print '##########################'
    print '####routing allocation####'
    print '##########################'
    print 'Result is'
    print 'Source ports are -->',src_port_list_algo_output
    print 'Destination ports are --> ',dst_port_list_algo_output
    

##########################
#####OVSnumber->OVSid#####
##########################
    
    result_translation=[]

    for a in range(1,len(algo_output1)-1):
        result_translation.append('DEFAULT')

    
    for i in range(1,len(algo_output1)-1):
        result_translation[i-1]=function_ovs_translation_from_number_to_id.translation_from_num_to_id(algo_output1[i])

    print '\n'
    print '##########################'
    print '####OVSnumber--->OVSid####'
    print '##########################'
    print result_translation
#    print result_translation[0][1]



############################################################################################
##### Device_id, Priority, Type, Out_port, Src_IP, Dst_IP, ARP_or_IP, ARP_or_IP_Type): #####
############################################################################################

#inputs=["of:000000606eb248fb","1","OUTPUT","1","192.0.0.198/32","192.0.0.202/32","0x0800","ETH_TYPE"] -> exmaple

####################
##### Variable #####
####################

    print '\n'
    print 'Src HOST is',algo_output1[0]
    print 'Dst HOST is',algo_output1[len(algo_output1)-1]
    print '\n'

    for a in range(1,len(algo_output1)-1):
    
        print 'OVS name is',result_translation[a-1][0] # OVS name
        print 'OVS name ID IS',result_translation[a-1][1] # OVS name's ID
        print 'OVS name IP IS',result_translation[a-1][2] # OVS name's IP
        print 'OVS name <-(src)',src_port_list_algo_output[a-1] #OVS name's <-
        print 'OVS name <-(dst)',dst_port_list_algo_output[a-1] #OVS name's ->
        print '\n'

#############################
##### DST FLOW RULE ADD #####
#############################

    for a in range(1,len(algo_output1)-1):
#        flow.function_routing_rule_post_flow.Routing_rule_post_just_ip(result_translation[a-1][1],"10000","OUTPUT",dst_port_list_algo_output[a-1],algo_output1[0],algo_output1[len(algo_output1)-1],port_output1[0],port_output1[1],"0x0800","ETH_TYPE")
        function_routing_rule_post_flow.Routing_rule_post_just_ip(result_translation[a-1][1],"10000","OUTPUT",dst_port_list_algo_output[a-1],algo_output1[0],algo_output1[len(algo_output1)-1],port_output1[0],port_output1[1],"0x0800","ETH_TYPE")
#        flow.function_routing_rule_post_flow.Routing_rule_post_udp_only_dst_port(result_translation[a-1][1],"65260","OUTPUT",dst_port_list_algo_output[a-1],algo_output1[0],algo_output1[len(algo_output1)-1],port_output1[0],port_output1[1],"0x0800","ETH_TYPE")
        function_routing_rule_post_flow.Routing_rule_post_tcp_only_dst_port(result_translation[a-1][1],"65260","OUTPUT",dst_port_list_algo_output[a-1],algo_output1[0],algo_output1[len(algo_output1)-1],port_output1[0],port_output1[1],"0x0800","ETH_TYPE")
        function_routing_rule_post.Routing_rule_post_arp_drop(result_translation[a-1][1], "65250")
    
#############################
##### SRC FLOW RULE ADD #####
#############################

    for a in range(1,len(algo_output1)-1):

        function_routing_rule_post_flow.Routing_rule_post_just_ip(result_translation[a-1][1],"10000","OUTPUT",src_port_list_algo_output[a-1],algo_output1[len(algo_output1)-1],algo_output1[0],port_output1[1],port_output1[0],"0x0800","ETH_TYPE")
#        flow.function_routing_rule_post_flow.Routing_rule_post_udp_only_dst_port(result_translation[a-1][1],"65260","OUTPUT",src_port_list_algo_output[a-1],algo_output1[len(algo_output1)-1],algo_output1[0],port_output1[1],port_output1[0],"0x0800","ETH_TYPE")
        function_routing_rule_post_flow.Routing_rule_post_tcp_only_dst_port(result_translation[a-1][1],"65260","OUTPUT",src_port_list_algo_output[a-1],algo_output1[len(algo_output1)-1],algo_output1[0],port_output1[1],port_output1[0],"0x0800","ETH_TYPE")
        function_routing_rule_post.Routing_rule_post_arp_drop(result_translation[a-1][1], "65250")


#function_main(['192.0.0.120/32','2','4','3','192.0.0.130/32'],['60000','60000'])
#function_main(['192.0.0.11/32','1','2','4','192.0.0.41/32'],['60001','60001'])


#function_routing_rule_post.Routing_rule_post("of:00009cebe831287a","65050","OUTPUT",'2',"192.0.0.100/32","192.0.0.101/32","0x0800","ETH_TYPE")
#function_routing_rule_post.Routing_rule_post(inputs[0],inputs[1],inputs[2],inputs[3],inputs[4],inputs[5],inputs[6],inputs[7])    
#function_routing_rule_post.Routing_rule_post("of:00009cebe831287a","65050","OUTPUT",'2',"192.0.0.100/32","192.0.0.101/32","0x0800","ETH_TYPE")
#function_routing_rule_post.Routing_rule_post("of:00009cebe831287a","65050","OUTPUT",'3',"192.0.0.101/32","192.0.0.100/32","0x0800","ETH_TYPE")
#function_routing_rule_post.Routing_rule_post("of:000000606eb248fb","65050","OUTPUT",'2',"192.0.0.100/32","192.0.0.101/32","0x0800","ETH_TYPE")    
#function_routing_rule_post.Routing_rule_post("of:000000606eb248fb","65050","OUTPUT",'3',"192.0.0.101/32","192.0.0.100/32","0x0800","ETH_TYPE")

  