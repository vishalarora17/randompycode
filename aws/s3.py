import boto3

import csv

# define variables
s3info=[]
sno=1


# final loop

session = boto3.Session(profile_name='longwalks',region_name='us-east-1')
s3 = session.client('s3')
response = s3.list_buckets()
for bucket in response['Buckets']:
    item={"#": sno, "Bucket Name": bucket['Name']}
    print item
    sno=sno+1
    s3info.append(item)


# Define CSV Columns
csv_columns = ['#','Bucket Name']

# Creating CSV file
try:
    with open('s3info.csv', 'wb') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in s3info:
            writer.writerow(data)

except IOError:
    print("I/O Error")

