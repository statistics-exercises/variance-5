import matplotlib.pyplot as plt
import numpy as np 

def sample_mean(m) : 
  # Your code to calculate a  sample mean from m 
  # uniform random variables between 0 and 1 goes here
  
  
def variance(n,m) : 
  # Your code to estimate the variance for a set of n 
  # sample means, which are each computed from m 
  # uniform random variables between 0 and 1 goes here.
  
xvals, yvals = np.zeros(200), np.zeros(200) 
for i in range(200) : 
  # Your code to set xvals and yvals as described in the panel
  # on the right goes here
  

# You shouldn't need to modify the code from here onwards
plt.plot( xvals, yvals, 'ko' )
plt.xlabel("Number of variables used to calculate mean")
plt.ylabel("Variance")
plt.savefig("variance_change.png")
