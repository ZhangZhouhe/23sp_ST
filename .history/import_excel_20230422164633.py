import glob
import os
file_list=glob.glob(os.path.join(os.getcwd(),"*.csv"))
for file in file_list:
    #os.system(f"sqlite3 .import {file} {file}")
    print(file)
    print(os.path.splitext(file)[0])