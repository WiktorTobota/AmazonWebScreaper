from DownloadingData import Download_data
from Create_csv import create_csv
import datetime
import csv
import pandas as pd
import re
URL = 'https://www.amazon.co.uk/Amazon-Essentials-Relaxed-fit-Short-Sleeve-Crewneck/dp/B07XLLKRWH/ref=sr_1_1_ffob_sspa?crid=2EHOLBP25D34V&keywords=t-shirts&qid=1702564666&sprefix=t%2Bs%2Caps%2C120&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1&psc=1'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

title = Download_data(URL, headers)[0]
price = Download_data(URL, headers)[1]

#deleting \n and empty spaces
price.strip()
pattern = r'£\d+\.\d{2}'
out = re.findall(pattern, price)
price = out[0]
price = price[1:] 
title = title.strip()

#getting todays date
today = datetime.date.today()

#creating new csv file -> do only once! 
#create_csv(title, price, today)

#writing a func that will check price of a product and add a record to a csv -> without creating a new one
def check_price(title, price, date):
    header = ['Title ', ' Price', 'Date']
    data = [title, price, date]
    return data
    
with open('AmazonProducts.csv', 'a+', newline='', encoding='UTF8') as f:
  writer = csv.writer(f)
  writer.writerow(check_price(title, price, today))
    
#calling out a func
check_price(title, price, today)

#printing out a data fron a file
df = pd.read_csv(r'C:\Users\Wiktor\AmazonProducts.csv')
print(df)
#seen output:                                    Title    Price        Date
#0   Amazon Essentials Women's Classic-Fit 100% Cot...    18.6  2023-12-15

