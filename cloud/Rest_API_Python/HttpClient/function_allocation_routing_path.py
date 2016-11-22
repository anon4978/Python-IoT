'''
Created on Mar 30, 2016

@author: nimdrak
'''


def Allocation_routing_dst_port(algo_output = [], *args):
 
####################
###Initialization###
####################
    
    dst_port_list = []
    current = 0
    after = 0

    for a in range(1,len(algo_output)-1):
        dst_port_list.append('DEFAULT')

    
######################################
###giving a value to current, after###
######################################
    
    for x in range(1,len(algo_output)-1):
 
        current = algo_output[x]
        after = algo_output[x+1]
        print '\n'
        print 'current:',current,',after:',after
        
##############################################
###allocate routing dst port from OVS Table###
##############################################

        f = open("/home/byounguklee/mininet/con_python/cloud/Rest_API_Python/HttpClient/table/"+"OVS"+current+".txt",'r')
        line=f.readline()

        while line:
            result=line.split()
            line=f.readline()
            if not line:
                break
            print result
            
            if result[0]==after:
                dst_port_list[x-1] =result[2]
                print 'According to after table','current OVS',current,'AND must have dst port :',dst_port_list[x-1]
                break
            
            
              
###############################    
### dealing with host case ####
###############################    
    
    
    for x in range(1,len(algo_output)-1):

        current = algo_output[x]
        after = algo_output[x+1]
    

        f = open("/home/byounguklee/mininet/con_python/cloud/Rest_API_Python/HttpClient/table/"+"OVS"+current+".txt",'r')
        line=f.readline()

        if dst_port_list[x-1] =='DEFAULT': #because vector notation start at 0, x-1
            while line:
                line=f.readline()
                result=line.split()           
                if not line:
                    break

                if result[0]=='HOST':
                    dst_port_list[x-1] = result[2]
                    print 'According to after table','current OVS',current,'AND',after,'IS HOST.','so dst port :',dst_port_list[x-1]
                    break                
    
    print '\n'
    print dst_port_list
    
    return dst_port_list


def Allocation_routing_src_port(algo_output = [], *args):

####################
###Initialization###
####################
      
    src_port_list = []
    current = 0
    ahead = 0

    for a in range(1,len(algo_output)-1):
        src_port_list.append('DEFAULT')

    
######################################
###giving a value to current, after###
######################################

    for x in range(1,len(algo_output)-1):
 
        current = algo_output[x]
        ahead = algo_output[x-1]
        print '\n'
        print 'current:',current,',ahead:',ahead

##############################################
###allocate routing dst port from OVS Table###
##############################################

        f = open("/home/byounguklee/mininet/con_python/cloud/Rest_API_Python/HttpClient/table/"+"OVS"+current+".txt",'r')
        line=f.readline()

        while line:
            result=line.split()
            line=f.readline()
            print result
            if not line:
                break
            
            if result[0]==ahead:
                src_port_list[x-1] =result[2]
                print 'According to after table','current OVS',current,'AND must have dst port :',src_port_list[x-1]
                break
  
###############################    
### dealing with host case ####
###############################    
    
        
    for x in range(1,len(algo_output)-1):

        current = algo_output[x]
        ahead = algo_output[x-1]
    

        f = open("/home/byounguklee/mininet/con_python/cloud/Rest_API_Python/HttpClient/table/"+"OVS"+current+".txt",'r')
        line=f.readline()

        if src_port_list[x-1] =='DEFAULT':
            if ahead == '192.0.0.200/32':
                src_port_list[x-1] = '3'
                print 'Controller case so First src port is 3'
                break
            
            while line:
                line=f.readline()
                result=line.split()

                if result[0]=='HOST':
                    src_port_list[x-1] = result[2]
                    print 'According to after table','current OVS',current,'AND',ahead,'IS HOST.','so dst port :',src_port_list[x-1]
                    break 
                    
    print '\n'
    print src_port_list
    
    return src_port_list


#['192.0.0.200/32','2', '1', '3']
def Allocation_routing_dst_port_ovs(algo_output = [], *args):
 
####################
###Initialization###
####################
    
    dst_port_list = []
    current = 0
    after = 0

    for a in range(1,len(algo_output)):
        dst_port_list.append('DEFAULT')
    print dst_port_list

    
######################################
###giving a value to current, after###
######################################
    
    for x in range(1,len(algo_output)-1):
 
        current = algo_output[x]
        after = algo_output[x+1]
        print '\n'
        print 'current:',current,',after:',after
        
##############################################
###allocate routing dst port from OVS Table###
##############################################

        f = open("/home/byounguklee/mininet/con_python/cloud/Rest_API_Python/HttpClient/table/"+"OVS"+current+".txt",'r')
        line=f.readline()

        while line:
            result=line.split()
            line=f.readline()
            if not line:
                break
            print result
            
            if result[0]==after:
                dst_port_list[x-1] =result[2]
                print 'According to after table','current OVS',current,'AND must have dst port :',dst_port_list[x-1]
                break
            
            
              
###############################    
### dealing with host case ####
###############################    
    
    current=algo_output[len(algo_output)-1]
    print current,len(algo_output)
    
    f = open("/home/byounguklee/mininet/con_python/cloud/Rest_API_Python/HttpClient/table/"+"OVS"+current+".txt",'r')
    line=f.readline()
    
    
    if dst_port_list[len(dst_port_list)-1]  =='DEFAULT': #because vector notation start at 0, x-1
        while line:
            line=f.readline()
            result=line.split()           
            if not line:
                break

            if result[0]==current:
                dst_port_list[len(dst_port_list)-1] = result[2]
                print 'According to after table','current OVS',current,'AND',after,'IS OVS.','so dst port :',dst_port_list[len(dst_port_list)-1]
                break                
       

    print '\n'
    print dst_port_list
    
    return dst_port_list




#Allocation_routing_dst_port_ovs(['192.0.0.200/32','2', '1', '3'])
#Allocation_routing_dst_port(['192.0.0.124/32', '2', '1', '3', '192.0.0.134/32'])
#Allocation_routing_src_port(['192.0.0.124/32', '2', '1', '3', '192.0.0.133/32'])

            