import subprocess

f=open("list.in")
files=f.readlines ()
f.close()
r_list=[]

for line in files:
 a=line.rstrip('\n')
 r_list.append(f' INITIAL_CONDITION_SEED ={a}')



wq = open("run")
filess = wq.readlines()
wq.close()
A = []

for line in filess:
	a = line.rstrip('\n')
	A.append(a)


print(A)

run = 'run'

def writer(run,A):
	ws = open(run, 'w')
	for i in range(2):
		print(A[i],file=ws)
	ws.close()

for i in range(1,51):
	A[0]=f'cd G-CTMQC_{i}/g-ctmqc-master/tests/Tully1/'
	A[1]=f"sed -i '20s/.*/{r_list[i-1]}/' input.in"
	writer(run,A)
	a='./run'
	subprocess.call([a],shell=True)

