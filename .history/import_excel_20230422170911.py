import glob
import os
import sqlite3
file_list=glob.glob(os.path.join(os.getcwd(),"*.csv"))
for file in file_list:
    file_name=os.path.split(file)[1] #drop path
    sql_name=os.path.splitext(file_name)[0] #drop suffix
    os.system(f"sqlite3 .import {file_name} {sql_name}")