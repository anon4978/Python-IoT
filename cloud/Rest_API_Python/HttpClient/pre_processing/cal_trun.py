import math
from scipy.stats import norm
import sys

import function_string_to_list


#######################
#### load two file ####
#######################
f_mean = open("/home/byounguklee/mininet/con_python/input_mean.txt",'r')


line2=f_mean.readline()
result=line2.split()


mean=float(result[0])
std_dev=float(result[1])


alpha=(-1)*(mean/std_dev)
alpha_tilt_phi=norm.pdf(alpha)
alpha_phi=norm.cdf(alpha)


trun_mean=mean+(std_dev)*(alpha_tilt_phi)/(1-alpha_phi)
trun_var=pow(std_dev,2) * (1+ (alpha)*(alpha_tilt_phi)/(1-alpha_phi) - pow((alpha_tilt_phi)/(1-alpha_phi),2))

result[0]=round(trun_mean,4)
result[1]=round(math.sqrt(trun_var),4)


#### first line case
final_output=[]
output=[]

output.append(result[0])
output.append(result[1])       
final_output.append(output)

print output
#### after first line
while line2:
    output=[]

    line2=f_mean.readline()
    result=line2.split()

    if result ==[]:
        break
    
    mean=float(result[0])
    std_dev=float(result[1])
    
    
    alpha=(-1)*(mean/std_dev)
    alpha_tilt_phi=norm.pdf(alpha)
    alpha_phi=norm.cdf(alpha)
    
    
    trun_mean=mean+(std_dev)*(alpha_tilt_phi)/(1-alpha_phi)
    trun_var=pow(std_dev,2) * (1+ (alpha)*(alpha_tilt_phi)/(1-alpha_phi) - pow((alpha_tilt_phi)/(1-alpha_phi),2))
    
    result[0]=round(trun_mean,4)
    result[1]=round(math.sqrt(trun_var),4)
    

    
    output.append(result[0])
    output.append(result[1])    
    
    print output
    final_output.append(output)
    output=[]
    

    
print final_output

f_allo_result=open("/home/byounguklee/mininet/con_python/input_mean_trun.txt",'w')
for i in range(0,len(final_output)):
    data = str(final_output[i][0]) + '\t'
    f_allo_result.write(data)
    
    
    data = str(final_output[i][1]) + '\n'
    f_allo_result.write(data)
    
f_allo_result.close()

