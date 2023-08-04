import pandas as pd
import os

date_before = pd.read_csv(os.path.join("Data","calendar",os.listdir('Data/calendar')[1]) ,encoding='big5')
date_df=pd.read_csv(os.path.join("Data","calendar",os.listdir('Data/calendar')[0]) ,encoding='big5')
date_after = pd.read_csv(os.path.join("Data","calendar",os.listdir('Data/calendar')[2]) ,encoding='big5')

date_df = pd.concat([date_before.iloc[-7:],date_df,date_after.iloc[:7]])
date_df.reset_index(drop=True,inplace=True)