# -*- coding: utf-8 -*-
"""
Created on Mon May 14 12:47:53 2018

@author: Tais Grippa
"""

# Import libraries
import os
import pandas as pd
import numpy as np

# User input
filepath="Data/RF_prob_results.csv"
sep=","
prob_columns=['ACS','BARE','PLAN','UNPLAN','VEG']

# Open the csv in a dataframe
input_df=pd.read_csv(filepath, delimiter=sep)
print list(input_df.keys())

# Keep only columns of interest
df=input_df[prob_columns]
print df.head()

## Get a new dataframe with the maximum and second maximum column
# Trick was found here: https://stackoverflow.com/questions/26015489/pandas-second-largest-values-column-name?noredirect=1&lq=1
#df=df.set_index("cat")
arank=df.apply(np.argsort, axis=1)
ranked_cols=df.columns.to_series()[arank.values[:,::-1][:,:2]]
label_frame=pd.DataFrame(ranked_cols, index=df.index)
label_frame.columns=['first_label','second_label']
# Trick was found here: https://stackoverflow.com/questions/39066260/get-first-and-second-highest-values-in-pandas-columns
prop_frame_1=pd.DataFrame(np.sort(df.values)[:,-1:], columns=['first_prop'])
prop_frame_2=pd.DataFrame(np.sort(df.values)[:,-2:-1], columns=['second_prop'])

## Final join
output_df=pd.concat([input_df, label_frame, prop_frame_1, prop_frame_2], axis=1)
output_df['uncert_level']=output_df['first_prop']-output_df['second_prop']

## Export
path,extension=os.path.splitext(filepath)
output_path=path+"_uncertainty"+extension
output_df.to_csv(output_path , sep=sep,  index=False)