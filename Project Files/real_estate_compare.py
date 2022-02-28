'''
Name of file: real_estate_compare.py
Date created: September 25, 2018
Date last updated: September 25, 2018
Created by: James Ingram
Purpose of Program: Compare house pricing statistics between various cities in Upstate, NY based on real estate data collected from zillow.com
'''
import datetime
import os
import logging
import pandas as pd 
import numpy as np 
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# create date format for filename
now = datetime.datetime.today().strftime("%m%d%y")

# kills running analyzer program
import subprocess as sp
extProc1 = sp.Popen(['python', 'real_estate_scraper.py'])
extProc2 = sp.Popen(['python', 'real_estate_analyzer.py'])
sp.Popen.terminate(extProc1)
sp.Popen.terminate(extProc2)
# clears console (Windows or Linux)
try:
    os.system('cls')
except:
    os.system('clear')

# reads .csv file created by real_estate_scraper.py and creates Pandas dataframes
try:
    df1 = pd.read_csv("properties-albany-" + now + ".csv")
    df2 = pd.read_csv("properties-binghamton-" + now + ".csv")
    df3 = pd.read_csv("properties-buffalo-" + now + ".csv")
    df4 = pd.read_csv("properties-syracuse-" + now + ".csv")
except:
    print("Unable to load files")
    quit()
# extracts data where title is "House For Sale"
df1 = df1[df1['title']=="House For Sale"]
# sets column names, removes null values, and stores as new dataframe
df1 = df1[['title', 'address','city','state','zip_code','beds','baths','area','price', 'region']].dropna()
# removes outliers from dataframe
df1 = df1[(np.abs(stats.zscore(df1["price"])) < 3)]
df1 = df1[(np.abs(stats.zscore(df1["beds"])) < 3)]
df1 = df1[(np.abs(stats.zscore(df1["baths"])) < 3)]
df1 = df1[(np.abs(stats.zscore(df1["area"])) < 3)]
# extracts data where title is "House For Sale"
df2 = df2[df2['title']=="House For Sale"]
# sets column names, removes null values, and stores as new dataframe
df2 = df2[['title', 'address','city','state','zip_code','beds','baths','area','price', 'region']].dropna()
# removes outliers from dataframe
df2 = df2[(np.abs(stats.zscore(df2["price"])) < 3)]
df2 = df2[(np.abs(stats.zscore(df2["beds"])) < 3)]
df2 = df2[(np.abs(stats.zscore(df2["baths"])) < 3)]
df2 = df2[(np.abs(stats.zscore(df2["area"])) < 3)]
# extracts data where title is "House For Sale"
df3 = df3[df3['title']=="House For Sale"]
# sets column names, removes null values, and stores as new dataframe
df3 = df3[['title', 'address','city','state','zip_code','beds','baths','area','price', 'region']].dropna()
# removes outliers from dataframe
df3 = df3[(np.abs(stats.zscore(df3["price"])) < 3)]
df3 = df3[(np.abs(stats.zscore(df3["beds"])) < 3)]
df3 = df3[(np.abs(stats.zscore(df3["baths"])) < 3)]
df3 = df3[(np.abs(stats.zscore(df3["area"])) < 3)]
# extracts data where title is "House For Sale"
df4 = df4[df4['title']=="House For Sale"]
# sets column names, removes null values, and stores as new dataframe
df4 = df4[['title', 'address','city','state','zip_code','beds','baths','area','price', 'region']].dropna()
# removes outliers from dataframe
df4 = df4[(np.abs(stats.zscore(df4["price"])) < 3)]
df4 = df4[(np.abs(stats.zscore(df4["beds"])) < 3)]
df4 = df4[(np.abs(stats.zscore(df4["baths"])) < 3)]
df4 = df4[(np.abs(stats.zscore(df4["area"])) < 3)]
# concatenates dataframes
frames = [df1, df2, df3, df4]
result = pd.concat(frames)

# Displays menu and prompts user for input
print("Compare All City Real Estate Data\n")
def options():
    def menu(list,question):
        for item in list:
            print(1 + list.index(item), item)
        return input(question)
    while True:
        items = ["Display Pricing Data", "Display Bedroom Data", "Display Bathroom Data", "Display Area Data", "Exit"]
        choice = menu(items,"\nPlease make a selection from the list above:\n>")
        try:
            choice = int(choice)
            break
        except:
            print("\nInvalid selection, please try again\n")
            continue
    print("")
    # user makes a selection
    if choice == 1:
        try:
            os.system('cls')
        except:
            os.system('clear')
        # creates figure displaying price data
        f, ax = plt.subplots(1, figsize=(10,8))
        sns.set_style("whitegrid")
        ax = sns.boxplot(x="region", y="price", data = result, palette="Set3")
        plt.show()
        f.savefig('price_compare.png', bbox_inches='tight')
        input("Press <enter> to return to menu:\n>")
        options()
    elif choice == 2:
        try:
            os.system('cls')
        except:
            os.system('clear')
        # creates figure displaying bedroom data
        f, ax = plt.subplots(1, figsize=(10,8))
        sns.set_style("whitegrid")
        ax = sns.boxplot(x="region", y="beds", data = result, palette="Set3")
        plt.show()
        f.savefig('beds_compare.png', bbox_inches='tight')
        input("Press <enter> to return to menu:\n>")
        options()
    elif choice == 3:
        try:
            os.system('cls')
        except:
            os.system('clear')
        # creates figure displaying bathroom data
        f, ax = plt.subplots(1, figsize=(10,8))
        sns.set_style("whitegrid")
        ax = sns.boxplot(x="region", y="baths", data = result, palette="Set3")
        plt.show()
        f.savefig('baths_compare.png', bbox_inches='tight')
        input("Press <enter> to return to menu:\n>")
        options()
    elif choice == 4:
        try:
            os.system('cls')
        except:
            os.system('clear')
        # creates figure displaying area data
        f, ax = plt.subplots(1, figsize=(10,8))
        sns.set_style("whitegrid")
        ax = sns.boxplot(x="region", y="area", data = result, palette="Set3")
        plt.show()
        f.savefig('area_compare.png', bbox_inches='tight')
        input("Press <enter> to return to menu:\n>")
        options()
    elif choice == 5:
        try:
            os.system('cls')
        except:
            os.system('clear')
        print("Goodbye!")
        quit()
    else:
        print("Invalid selection, please try again\n")
        options()
options()
