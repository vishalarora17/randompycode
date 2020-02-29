import boto3
import datetime
import csv
import xlwt
'''
session = boto3.Session(profile_name='longwalks',region_name='us-east-1')

def default(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()

ec2  = session.client('ec2')

response = ec2.describe_instances()
ec2info = json.dumps(response, default=default)
print ec2info
'''

session = boto3.Session(profile_name='longwalks',region_name='us-east-1')
ec2  = session.client('ec2')

# Retrieves all regions/endpoints that work with EC2
response = ec2.describe_regions()
#print(response['Regions']['RegionName'])
#print response
list=[]
for ft in response['Regions']:
    item=ft['RegionName']

    list.append(item)

print list

'''
region_list=[]
s_no=1
for ft in response['Regions']:
    item = {"#": s_no, "Endpoint": ft['Endpoint'], "RegionName": ft['RegionName']}
    s_no = s_no + 1

    region_list.append(item)

print region_list

csv_columns = ['#', 'Endpoint', 'RegionName']

try:
    with open('region.csv', 'wb') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in region_list:
            writer.writerow(data)

except IOError:
    print("I/O Error")
'''
# Retrieves availability zones only for region of the ec2 object
#response = ec2.describe_availability_zones()
#print('Availability Zones:', response['AvailabilityZones'])