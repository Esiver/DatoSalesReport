import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import datetime

import weekgroup, daygroup, pdfMaker#, write_html, dftopdf

def getSalesData(file):
    sales_data = pd.read_csv(file, sep='\t')#, sep='\t'
    try:
        sales_data['date'] = pd.to_datetime(sales_data['date'], errors='coerce') #make a 'date'-column in datetime format
    except:
        print('Error found, trying different seperator.')
        sales_data = pd.read_csv(file, sep=',', engine='c')#, sep='\t'
        sales_data['date'] = pd.to_datetime(sales_data['date'], errors='coerce') #make a 'date'-column in datetime format
    
    return sales_data 

#sales_data.columns['date','units','sales','spend','Acos','CPC']


def weekData(datafile):
    getSalesData(datafile)
    week = weekgroup.main(datafile) #Data by week
    week_stats = weekgroup.stats(week) #dive into the stats for week    
    weekgroup.makeCsv(week) #make csv file with week dataframe
    weekgroup.plot(week, week_stats) #make plot, saves a file but doesn't plt.plot()
    #weekgroup.makeReport() #make a report in .pdf

def dayData(datafile):
    day = daygroup.main(datafile) #day data
    day_stats = daygroup.stats(day) #day statistics
    daygroup.makeCsv(day) #csv for day dataframe
    daygroup.plot(day, day_stats) #make plot for days(-data)


def formatMain(mainFile):
    csv_df = mainFile.to_csv()
    mainFile.to_csv(r'all_data.csv')
    print('formatted main data')
    return csv_df

sales_data = getSalesData('clean_data.csv')
formatMain(sales_data) #format my original data into a dataframe friendly csv
print(formatMain(sales_data))
files_to_read = ['week_max5.csv','week_min5.csv','all_data.csv']

pdfMaker.reporter(files_to_read)

#weekgroup.reporter(files_to_read)