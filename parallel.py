import os
parentFolder = '/home/shravan/FIFTYFOLDER/fifty1/'

T = 25;

Total_files = 50;

count = 1;

while(count<Total_files):

   for i in range(T):
           location = parentFolder + 'G-CTMQC_' + str(count) + '/g-ctmqc-master/tests/Tully1'
           os.chdir(location)
           command = 'cd' + location 
           os.system('pwd')
           command1 = 'qsub sub.sh'
           os.system(command)
           os.system('pwd')
           os.system(command1)
           count = count + 1 
           os.chdir('../../../../')
           os.system('pwd')

