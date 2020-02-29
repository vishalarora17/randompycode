
import boto3
import csv

# Getting AWS Regions list
session = boto3.Session(profile_name='longwalks',region_name='eu-north-1')
ec2 = session.client('ec2')
response = ec2.describe_regions()
regions=[]
for ft in response['Regions']:
    item=ft['RegionName']
    regions.append(item)

# define variables
ec2info=[]
sno=1

# final loop
for region in regions:
    session = boto3.Session(profile_name='longwalks',region_name=region)
    ec2 = session.client('ec2')
    response = ec2.describe_instances()

    for reserveration in response['Reservations']:
        for inst in reserveration['Instances']:
            item = {"#": sno, "InstanceId": inst['InstanceId'], "InstanceType": inst['InstanceType'], "State": inst['State']['Name'], "AvailabilityZone": inst['Placement']['AvailabilityZone'], "PrivateIpAddress": inst['PrivateIpAddress']}
            sno = 1 + sno
            if inst['Tags'][0]['Key'] == 'Name':
                item["instanceName"] = inst['Tags'][0]['Value']
            else: pass

            ec2info.append(item)

#    print (ec2info)
# Defining csv columns
    csv_columns = ['#','InstanceId','instanceName','InstanceType','State','AvailabilityZone','PrivateIpAddress']
# Creating CSV file
    try:
        with open('ec2info.csv', 'wb') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in ec2info:
                writer.writerow(data)

    except IOError:
        print("I/O Error")




