import pandas as pd
import os
import shutil

#Input file structure: "url" - "screenshot code" - brand"
df = pd.read_excel("input.xlsx")

#Create directories in home folder
folders_name = set()

#Get folders' names
for i in len(df):
    folders_name.add(df.loc[i,2])

#Create Folders
for brand in folders_name:
    os.mkdir(brand)

#Sorting
for i in len(df):
    screenshot = df.loc[i,1]
    destination = df.loc[i,2]
    shutil.move(screenshot, destination)
