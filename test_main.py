import unittest
import scipy.stats as st
from main import *

class UnitTests(unittest.TestCase) :
    def test_xplot(self): 
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        self.assertTrue( len(this_x)==200, "you have plotted the wrong number of coordinates in your graph" )
        for i in range( len(this_x) ) :
            self.assertTrue( np.abs(i + 1 - this_x[i])<1e-7, "the x-coordinates in your graph are incorrect" )
            
    def test_xplot(self): 
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)

        for k in [5,10,15,20] : 
            samples = 100*[0]
            for i in range(100) : 
                for j in range(10) :
                    myvar = (sum( np.random.uniform(0,1, size=k) ) / k ) - 0.5
                    samples[i] = samples[i] + myvar*myvar 
                samples[i] = samples[i] / 10
    
            samples.sort()
            self.assertTrue( this_y[k-1]>samples[1] and this_y[k-1]<samples[98], "the y-coordinates in your graph appear to be incorrect" )
