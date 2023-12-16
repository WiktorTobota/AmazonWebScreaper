import csv 
def create_csv(title, price, date):
    header = ['Title ', ' Price', 'Date']
    data = [title, price, date]

    with open('AmazonProducts.csv', 'w', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(data)
