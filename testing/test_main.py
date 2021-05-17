try:
    from AutoFeedback.plotchecks import check_plot
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.plotchecks import check_plot

from AutoFeedback.plotclass import line
from AutoFeedback.randomclass import randomvar
import unittest
from main import *

x, y = np.linspace(1,50,50), []
for i in range(50) : 
    var = randomvar( 0.5, variance=1/12/(i+1), dist="chi2", isinteger=False ) 
line1=line( x, y )

axislabels=["Number of variables used to calculate mean", "Variance"]

class UnitTests(unittest.TestCase) :
    def test_variables(self) :
        assert(check_plot([line1],explabels=axislabels,explegend=False,output=True))
