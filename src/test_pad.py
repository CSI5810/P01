import numpy as numpy
import pandas as pd
import os

file_name = './bank-additional/bank-additional/bank-additional-full.csv'
df = pd.read_csv(file_name, sep=';')
for column in df.columns:
    df.hist(column=column)