# import relevant libraries
import numpy as np
import pandas as pd

# load in cast_and_crew.csv
cast_and_crew = pd.read_csv('cast_and_crew.csv')

# split the data into two dataframes by rows (first and second half)
first_half = cast_and_crew.iloc[:len(cast_and_crew)//2]
second_half = cast_and_crew.iloc[len(cast_and_crew)//2:]

# save the two dataframes as csv files
first_half.to_csv('cast_and_crew1.csv', index=False)
second_half.to_csv('cast_and_crew2.csv', index=False)