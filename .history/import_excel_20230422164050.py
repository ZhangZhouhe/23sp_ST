import glob
import os
file_list=glob.glob(os.path.join(os.getcwd(),"*.csv"))
for file in file_list:
    print(file)