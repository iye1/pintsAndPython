##############################################
#Description:
# This file will plot data 
# 
##Goals#
#  open file for reading
#  read data 
#  format data from string to float
#  invert the data to most recent on top(?) 
#  plot datas
##############################################

import csv 
from matplotlib import pyplot as plt

def plot_stocks(stock):
     file = stock + "parsedStockData.txt"


     with open (file) as csvfile:
          readcsv =csv.reader(csvfile,delimiter=',')
          Dates=[]
          Prices=[]
          n=0
          
          #for loop starts here
          for row in readcsv:
               #gets the date from Row 7 and price from Row 5
               PriceStr = row[7]
               Price = float(PriceStr)
               DateStr = row[5]
               Date = float(DateStr)
		
		        #appends Price and date to the lists
               Dates.append(Date)
               Prices.append(Price)		     
               
               #for loop control:		     
               n=n+1
               print (n)
               
               if n >390:
                    break

     #print (Dates)
     #print (Prices)

     RoughGriaffe = plt.plot(Prices)
     #plt.show()
     
     return(Prices)
     
