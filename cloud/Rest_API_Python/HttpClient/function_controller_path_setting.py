'''
Created on May 3, 2016

@author: cloud1
'''

def controller_path_setting(number_of_ovs):

    all_that_controller=[]

    for x in range(0,number_of_ovs):
        f_cont = open("/home/byounguklee/mininet/con_python/cloud/Rest_API_Python/HttpClient/server_table/"+"OVS"+str(x+1)+".txt",'r')
        line_cont=f_cont.readline()
        controller=[]
        all_controller = []                
        while line_cont:
            result_cont=line_cont.split()

            line_cont=f_cont.readline()
    
            controller.append('10.123.123.1/32')

            for y in range(1,x+2):
                controller.append(str(y))
       
            controller.append(result_cont[1])


            all_controller.append(controller)
            controller=[]
    
        all_that_controller.append(all_controller)
    
#    print all_that_controller
    return all_that_controller

a=controller_path_setting(4)
print a

#for y in range(0,len(a)):
#    for x in range(0,len(a[0])):
#        print a[y][x]