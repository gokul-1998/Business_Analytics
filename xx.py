import numpy as np

l=np.logspace(-4,0,num=3)
# the above is equivalent to:
# l=np.logspace(-4,0,3) # num=3 is the default value for the parameter num
# here the output is:
# [1.e-04 1.e-02 1.e+00] 
# because the default base is 10 
# 1.e-03 = 1*10^(-3) = 0.001 is not in the range [0.0001, 1] 
# 1.e-02 = 1*10^(-2) = 0.01 is in the range [0.0001, 1]
# 1.e-01 = 1*10^(-1) = 0.1 is in the range [0.0001, 1]
print(l)
# [1.e-04 1.e-02 1.e+00]