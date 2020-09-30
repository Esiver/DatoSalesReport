import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
import datetime

import csv
from fpdf import FPDF

sales_data = pd.read_csv(r'clean_data.csv', engine='c', sep='\t')
sales_data['date'] = pd.to_datetime(sales_data['date'], errors='coerce') #make a 'date'-column in datetime format

def main():
    
    week_data = sales_data
    week_data['week'] = week_data['date'].dt.week #make week column, just in case...
    week_data = week_data[['units','sales','spend']].groupby(week_data['date'].dt.week).sum().reset_index() #sum columns grouped by date
    week_data['ROI'] = (week_data['sales'] - week_data['spend'])/week_data['spend'] # calculate new ROI column for week df
    week_data['ACOS'] = (week_data['spend']/week_data['sales']) #and calculate ACOS just because....
    
    week_data = week_data.round(3)

    print('----------------------- DATA GROUPED BY WEEK ------------')
    week_data.columns= ['week','units','sales','spend','ROI','ACOS']
    print(week_data)

    return week_data

def makeHtml (df):
    html_df = df.to_html
    print('made html-----------------------------------')
    print(html_df)
    print('made html-----------------------------------')
    return html_df

def makeCsv (df):
    csv_df = df.to_csv
    print('made csv----------------------------------')
    print(csv_df)
    print('made html-----------------------------------')
    df.to_csv(r'week_csv.csv')
    return csv_df


def makeReport():
    with open('week_csv.csv', newline='') as f:
        reader = csv.reader(f)
        
        pdf = FPDF()
        pdf.add_page()
        page_width = pdf.w - 2 * pdf.l_margin
            
        pdf.set_font('Times','B',14.0) 
        pdf.cell(page_width, 0.0, 'Data Analysis', align='C')
        pdf.ln(15)

        pdf.set_font('Courier', '', 12)
        col_width = page_width/8
        
        img_height = 100
        img_width = 125

        pdf.image('week_plot.png', x=0, y=0, w=img_width, h=img_height)

        pdf.ln(100)

        pdf.cell(page_width, 0.0, 'Lowest 5 Sales', align='C')

        with open('week_min5.csv', newline='') as i:
            extra = csv.reader(i)
            th = pdf.font_size
            col_width = page_width/10
            for row in extra:
                
                
                pdf.cell(col_width, th, str(row[0]), border=1)
                pdf.cell(col_width, th, row[0], border=1, align='C')
                pdf.cell(col_width, th, row[1], border=1, align='C')
                pdf.cell(col_width, th, row[2], border=1, align='C')
                pdf.cell(col_width, th, row[3], border=1, align='C')
                pdf.cell(col_width, th, row[4], border=1, align='C')
                pdf.cell(col_width, th, row[5], border=1, align='C')
                pdf.cell(col_width, th, row[6], border=1, align='C')

                pdf.ln(th)

        pdf.cell(page_width, 0.0, 'Top 5 Sales', align='C')

        with open('week_max5.csv', newline='') as a:
            extra = csv.reader(a)
            th = pdf.font_size
            col_width = page_width/6
            for row in extra:
                
                pdf.cell(col_width, th, str(row[0]), border=1)
                pdf.cell(col_width/2, th, row[1], border=1, align='C')
                pdf.cell(col_width/2, th, row[2], border=1, align='C')
                pdf.cell(col_width/2, th, row[3], border=1, align='C')
                pdf.cell(col_width, th, row[4], border=1, align='C')
                pdf.cell(col_width, th, row[5], border=1, align='C')
                pdf.cell(col_width, th, row[6], border=1, align='C')

                pdf.ln(th)
    
        pdf.multi_cell(page_width,0.0,chr(10))
        pdf.cell(page_width,0.0,'All data', align='C')

        th = pdf.font_size
        
        for row in reader:
     
            pdf.cell(col_width, th, str(row[0]), border=1)
            pdf.cell(col_width, th, row[1], border=1, align='C')
            pdf.cell(col_width, th, row[2], border=1, align='C')
            pdf.cell(col_width, th, row[3], border=1, align='C')
            pdf.cell(col_width, th, row[4], border=1, align='C')
            pdf.cell(col_width, th, row[5], border=1, align='C')
            pdf.cell(col_width, th, row[6], border=1, align='C')

            pdf.ln(th)
            
        pdf.ln(10)

        pdf.set_font('Times','',10.0) 
        pdf.cell(page_width, 0.0, '- end of report -', align='C')
        
        pdf.output('DataAnalysis.pdf', 'F')

def stats(x):
    week_sales_max = x.nlargest(5,'sales')
    week_sales_min = x.nsmallest(5,'sales')
    
    #print('HEYYYYYYYYYYYYYYYYY DUDE')
    #print(week_sales_max,week_sales_min)
    #minmax_sales = week_sales_max.merge(week_sales_min, how='outer')

    week_ROI_max = x.nlargest(5,'ROI')
    week_ROI_min = x.nsmallest(5,'ROI')
    mean_week_sales = x['sales'].mean(skipna= True)
    #mean_sales = sales_data['sales'].mean(skipna = True)

    week_sales_min.to_csv(r'week_min5.csv')
    week_sales_max.to_csv(r'week_max5.csv')
    return mean_week_sales

def plot(d, s):
    mean = s
    d.plot(x='week', y=['sales', 'spend'], kind = 'bar')
    plt.axhline(y=s, color='r', linestyle='dotted')
    ax = d['ROI'].plot(secondary_y=True)
    ax.set_ylabel('ROI')
    #plt.show()
    plt.savefig('week_plot.png')

    
