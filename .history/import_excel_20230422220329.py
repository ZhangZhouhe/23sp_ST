import glob
import os
from sqlalchemy import create_engine
import pandas as pd
engine=create_engine('sqlite:///data.db')
file_list=glob.glob(os.path.join(os.getcwd(),"*.csv"))
for file in file_list:
    file_name=os.path.split(file)[1] #drop path
    sql_name=os.path.splitext(file_name)[0] #drop suffix
    df=pd.read_excel(file_name)
    