# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 14:45:56 2023

@author: Alex
"""

import os
import pandas as pd
from os.path import isfile, join
import shutil


def Rename(KeyPath, FolderPath, DestPath):
    df = pd.read_csv(KeyPath)
    df['Sjob'] = df['Sjob'].astype('str')
    df['Item'] = df['Item'].astype('str')
    
    df['TaskCard'] = df['TaskCard'].str.slice(0, 12)
    folders = os.listdir(FolderPath)
    
    FilesList = []
    
    for i, folder in enumerate(folders):
        for j, number in enumerate(df['Sjob']):
            path = FolderPath + "\\" + folders[i] + "\\"
            if folders[i] == df.Sjob[j]:
                filesTemp = [path + f for f in os.listdir(path) if isfile(join(path, f))]
        FilesList = FilesList + filesTemp
    
    for f, file in enumerate(FilesList):
        
        for l, line in df.iterrows():
            fpath = FolderPath + "\\" + df.Sjob[l] + "\\" + df.Item[l] + ".pdf"
            if file == fpath:
                shutil.copyfile(fpath, DestPath + "\\" + df.TaskCard[l] + " - Sjob " + df.Sjob[l] + " - Item " + df.Item[l] + ".pdf")
