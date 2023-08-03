# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 15:45:52 2023

@author: Alex
"""


import os
import pandas as pd
from os.path import isfile, join

def Rename(NamesPath, FilesPath):
    df = pd.read_csv(NamesPath)
    df['Column1'] = df['Column1'].astype('str')
    
    for i, number in enumerate(df):
        files = [f for f in os.listdir(FilesPath) if isfile(join(FilesPath, f))]
    
    for i, num in enumerate(df['Column1']):
        for j, file in enumerate(files):
            if num in file:
                os.rename(FilesPath + "\\" + file, FilesPath + "\\" + df.Column2[i] + " - task " + num + ".pdf")

