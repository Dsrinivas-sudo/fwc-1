import numpy as np
import matplotlib.pyplot as plt

#defining function
def f(x):
	return((x-2)**3)*((x-1)**2);
	
#defining derivative of f(x)
df=lambda x:(x-1)*((x-2)**2)*(5*x-7);

#for maxima using gradient ascent
cur_x1=0.5
previous_step_size1=1
iters1=0
precision=0.000000001
alpha=0.0001
max_iters=100000000

while (previous_step_size1>precision)&(iters1<max_iters):
	prev_x=cur_x1
	cur_x1+=alpha*df(prev_x)
	previous_step_size1=abs(cur_x1-prev_x)
	iters1+=1
max_val=f(cur_x1)
print('maximum value of x is',max_val,"at","x=",cur_x1)

#for minima using gradient ascent
cur_x2=1.5
previous_step_size2=1
iters2=0

while (previous_step_size2>precision)&(iters2<max_iters):
	prev_x=cur_x2
	cur_x2-=alpha*df(prev_x)
	previous_step_size2=abs(cur_x2-prev_x)
	iters2+=1
min_val=f(cur_x2)
print('minimum value of x is',min_val,"at","x=",cur_x2)

#Plotting f(x)
x=np.linspace(0,2,10000)
y=f(x)
label_str = "$((x-2)^3)((x-1)^2)$"
plt.plot(x,y,label=label_str)
#Labelling points
plt.plot(cur_x1,max_val,'.',label='point of maxima')
plt.plot(cur_x2,min_val,'.',label='point of minima')

plt.xlim([0.7,3])
plt.ylim([-2,2])
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
plt.legend()
plt.savefig('op3t.png')
plt.show()
