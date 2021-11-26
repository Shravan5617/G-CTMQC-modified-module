import os
parentFolder = '/home/shravan/FIFTYFOLDER/fifty1/'

T = 25;

Total_files = 50;

count = 1;

while(count<Total_files):

   for i in range(T):
           location = parentFolder + 'G-CTMQC_' + str(count) + '/g-ctmqc-master/tests/Tully1'
           os.chdir(location)
           os.system('pwd') 
          # command1 = 'cp BO_population.dat BO_population_' + str (count) 
           #os.system(command1)
           #command2 = 'cp BO_population_' + str (count) + ' /home/shravan/FIFTYFOlDER/outputfile'
           command2 = 'cp BO_population_' + str (count) + ' ../../../../outputfile'
           os.system('pwd')
           os.system(command2)
           count = count + 1 
           os.chdir('../../../../')
           os.system('pwd')


 
