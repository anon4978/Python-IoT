'''
Created on Mar 31, 2016

@author: nimdrak
'''

def translation_from_num_to_id(ovs_number):

    f = open("/home/byounguklee/mininet/con_python/cloud/Rest_API_Python/HttpClient/table/OVS_ID_TABLE.txt",'r')
    line=f.readline()

    while line:
        result=line.split()
        line=f.readline()
        
        if not line:
            break

        if result[0]==(ovs_number):
            return result




#print translation_from_num_to_id('1')