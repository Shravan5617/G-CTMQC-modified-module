import numpy as np
import os
import shutil



def file_copy(i):
	matrix=np.loadtxt('BO_population_' + str(i))
	return matrix

mat=np.zeros((601,5))


for i in range(1,51):
	#command = echo '"$(tail -n +2 BO_population_' + str(i))+'" > BO_population_' + str(i))
        #os.system('echo "$(tail -n +2 BO_population_'+str(i)+')" > BO_population_'+str(i))
        mat=mat+file_copy(i)
   
	
mat=mat/50

file2=open('Final.out',"w")
np.savetxt(file2,mat)
file2.close()


