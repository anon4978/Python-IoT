'''
Created on May 9, 2016

@author: cloud1
'''
'''
Created on May 9, 2016

@author: nimdrak
'''
import operator
import os
import sys


dirname=sys.argv[1] + '/'
#dirname='/home/controller/IoT/normal_packet/output/'        

filenames = os.listdir(dirname)
#for filename in filenames:
#    full_filename=os.path.join(dirname, filename)
#    ext = os.path.splitext(full_filename)[-1]                           
#    if ext == '.txt':
        #print(full_filename)
        
file_name=[]
data_vector=[]
all_data_vector=[]
sum_data_vector=[]
sum_data_average_vector=[]
len_data_vector=[]
time_vector=[]
name_index_vector=[]
data_number=0


for (path, dir, files) in os.walk(dirname):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
#        print filename
        if 'bw' in filename:
######            print("%s %s" % (path, filename));
            

            name_index_vector.append([path,filename])
            file_name.append(filename)

#            print path+'/'+filename
            bw_data=open(path+'/'+file_name[data_number],'r')
            
            
            line=bw_data.readline()
            result=line.split()
            data_vector.append(result)
#            print data_vector
            
            while line:
                line=bw_data.readline()
                result=line.split()
                if result==[]:
                    break
                data_vector.append(result)
                
            data_number=data_number+1    
            #print data_vector
            all_data_vector.append(data_vector)
######            print(len(data_vector))
            data_vector=[]
        
# check empty line and append 0
for i in range(0,len(all_data_vector)):
    len_data_vector.append(len(all_data_vector[i]))
#print len_data_vector
max_length=max(len_data_vector)
print sys.argv[2]
print 'total data size is ', max_length

for i in range(0,len(all_data_vector)):
    while len(all_data_vector[i]) < max_length:
#        print 'someone is', len(all_data_vector[i])
#        print 'that some is ', name_index_vector[i]
        all_data_vector[i].append(['0'])
 #       print len(all_data_vector[i])
 #       print all_data_vector[i]

for i in range(0,max_length):
    sum_data_vector.append(0)
    sum_data_average_vector.append(0)

for j in range(0,max_length):
    for i in range(0,data_number):
        sum_data_average_vector[j]=sum_data_average_vector[j]+(float(all_data_vector[i][j][0]))/5
        sum_data_vector[j]=sum_data_vector[j]+(float(all_data_vector[i][j][0]))


#print sum_data_average_vector;
#print sum_data_vector;



f_sum_result=open(dirname+'/'+'sum_all_average_result.txt','w')
f_sum_result1=open(dirname+'/'+'sum_all_result.txt','w')

for i in range(0,len(all_data_vector[0])):
    data = str(sum_data_average_vector[i]) + '\n'
    f_sum_result.write(data)
    data1 = str(sum_data_vector[i]) + '\n'
    f_sum_result1.write(data1)
    
f_sum_result.close()
f_sum_result1.close()
    