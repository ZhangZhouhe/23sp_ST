import glob
import os
file_list=glob.glob(os.path.join(os.getcwd(),"*.csv"))
for file in file_list:
    #os.system(f"sqlite3 .import {file} {file}")
    file_name=os.path.split(file)[1] #drop path
    sql_name=os.path.splitext(file_name)[0] #drop suffix
    print(os.system("sqlite3").read())
    #os.system(f"sqlite ")