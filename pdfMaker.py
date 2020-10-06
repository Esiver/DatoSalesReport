import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
import datetime

import csv
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.image('datologo.png',10,10,30,30) #logo
        self.set_font('Arial','B',16) #Arial bold size 16
        self.cell(80) #transform cell 80
        self.cell(30,10,'I am Title',1,0,'C')
        self.ln(50)
    
    def figure(self, mig):
        self.ln(30)
        # Logo
        self.image(mig, 10, 8, 33)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, 'Title', 1, 0, 'C')
        # Line break
        self.ln(20)
    
    def table(self, dfile):
        self.cell(30,10,dfile)
        self.ln(10)
        self.set_font('Courier','',size=12)
        with open(dfile, newline='') as f:
            data = csv.reader(f)
            th = self.font_size
            page_width = self.w - 2 * self.l_margin
            col_width = page_width/8
            
            for row in data:
                for column in row:
                    self.cell(col_width,th,column, border=1, align='C')
                    
                #self.cell(col_width,th,column[row],border=1,align='C')
                #self.cell(col_width,th,row[0], border=1, align='C')
                #self.cell(col_width,th,row[1], border=1,align='C')
                #self.cell(col_width,th,row[2], border=1,align='C')
                #self.cell(col_width,th,row[3], border=1,align='C')
                #self.cell(col_width,th,row[4], border=1,align='C')
                #self.cell(col_width,th,row[5], border=1,align='C')

                self.ln(th)
        self.ln(th*2)
    def maker(self,fig,csvfile):
        #self.add_page()
        #self.header()
        #self.figure(fig)
        self.table(csvfile)


def reporter(datafile):
    pdf = PDF()
    print('Im the reporter, look at me!')
    pdf.add_page()
    for x in datafile:
        pdf.maker('datologo.png',x)
    pdf.output('newMan.pdf', 'F')