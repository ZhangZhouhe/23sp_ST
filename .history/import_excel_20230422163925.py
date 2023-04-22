import glob
import os
print(os.getcwd())
print(glob.glob(os.path.join(os.getcwd(),"*.csv")))