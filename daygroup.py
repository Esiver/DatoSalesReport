import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
import datetime
import logging
import matplotlib.ticker as ticker

import csv
from fpdf import FPDF



def main(sales_data):
    #sales_data = pd.read_csv(r'clean_data.csv', engine='c',sep='\t')#, sep='\t')
    sales_data['date'] = pd.to_datetime(sales_data['date'], errors='coerce') #make a 'date'-column in datetime format

    day_data = sales_data
    
    day_data = day_data[['units','sales','spend']].groupby(day_data['date']).sum().reset_index() #sum
    day_data['ROI'] = (day_data['sales'] - day_data['spend'])/day_data['spend'] # calculate new ROI column for week df
    day_data['ACOS'] = (day_data['spend']/day_data['sales'])
    
    day_data = day_data.round(3)

    print('----------------------- DATA GROUPED BY DAY ------------')
    day_data.columns= ['date','units','sales','spend','ROI','ACOS']
    print(day_data)
    return day_data

def makeReport():
    with open('day_csv.csv', newline='') as f:
        reader = csv.reader(f)
        
        pdf = FPDF()
        pdf.add_page()
        page_width = pdf.w - 2 * pdf.l_margin
            
        pdf.set_font('Times','B',14.0) 
        pdf.cell(page_width, 0.0, 'Data Analysis', align='C')
        pdf.ln(10)

        pdf.cell(50)

        pdf.set_font('Courier', '', 12)
        col_width = page_width/6
        
        
        img_height = 100
        img_width = 125

        pdf.image('day_plot.png', x=0, y=0, w=img_width, h=img_height)

        pdf.ln(100)
        
        th = pdf.font_size
        
        for row in reader:
            #print(row)
            #pdf.cell(col_width, th, str(row[0]), border=1)
            pdf.cell(col_width, th, row[1], border=1, align='C')
            pdf.cell(col_width, th, row[2], border=1, align='C')
            pdf.cell(col_width, th, row[3], border=1, align='C')
            pdf.cell(col_width, th, row[4], border=1, align='C')
            pdf.cell(col_width, th, row[5], border=1, align='C')
            pdf.cell(col_width, th, row[6], border=1,align='C')

            pdf.ln(th)
            
        pdf.ln(10)
        
        pdf.set_font('Times','',10.0) 
        pdf.cell(page_width, 0.0, '- end of report -', align='C')
        
        pdf.output('Day_DataAnalysis.pdf', 'F')

def makeCsv (df):
    csv_df = df.to_csv
    df.to_csv(r'day_csv.csv')
    logging.info('daygroup made csv')
    return csv_df

def stats(x):
    day_sales_max = x.nlargest(5,'sales')
    day_sales_min = x.nsmallest(5,'sales')
    day_ROI_max = x.nlargest(5,'ROI')
    day_ROI_min = x.nsmallest(5,'ROI')
    mean_day_sales = x['sales'].mean(skipna= True)
    #mean_sales = sales_data['sales'].mean(skipna = True)

    return mean_day_sales


def plot(d, s):
    plt.xticks(rotation=45, ha='right')
    d.plot(x='date', y=['sales', 'spend'], kind = 'bar') #plot our (d)ate
    plt.axhline(y=s, color='r', linestyle='dotted') # plot (s)th as an horizontal line
    ax = d['ROI'].plot(secondary_y=True) #make secondart y-plot

    tick_spacing =19 #x-axis tick frequency
    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing)) #x-axis frequency adjust

    #todo: rotate ticks, dates too long to make sense.

    ax.set_ylabel('ROI') #set y-axis label
    #plt.show() #show?
    plt.savefig('day_plot.png') #save it for report
####nice plot
#sales_data.plot(x ='date', y=['sales', 'spend'], kind = 'line')
#plt.axhline(y=mean_sales, color='r', linestyle='dotted')
#ax = sales_data['ROI'].plot(secondary_y=True)
#ax.set_ylabel('ROI')
#plt.show() 
