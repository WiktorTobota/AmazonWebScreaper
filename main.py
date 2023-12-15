from DownloadingData import Download_data


URL = 'https://www.amazon.co.uk/Amazon-Essentials-Relaxed-fit-Short-Sleeve-Crewneck/dp/B07XLLKRWH/ref=sr_1_1_ffob_sspa?crid=2EHOLBP25D34V&keywords=t-shirts&qid=1702564666&sprefix=t%2Bs%2Caps%2C120&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1&psc=1'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

title = Download_data(URL, headers)[0]
price = Download_data(URL, headers)[1]

#deleting \n and empty spaces
price.strip()
pattern = r'£\d+\.\d{2}'
out = findall(pattern, price)
price = out[0]
price = price[1:] 
title = title.strip()
