import numpy as np 
import cython as cy 
from timeit import default_timer as timer


def fraction_sum(n):
    
    k = 0
    start = timer()
    for l in range (1, 501):
        for i in range (1, n+1) :
            k = k + float (1)/pow(i,2)
        k = 0 
    
    end = timer()
    print (end - start)
    return k 

s = fraction_sum(10000)
print s

############# HOW TO #########################

# 1. Create setup.py file 

	# from distutils.core 
	# import setupfrom Cython.Build 
	# import cythonize
	# setup(
	#	ext_modules = cythonize("fraction_sum.pyx")
	# )

	
# 2. Run from the command line

	# $ python setup.py build_ext --inplace
	
# 3. Start the python console 
	
	# >>> import fraction_sum

############### END ##########################

