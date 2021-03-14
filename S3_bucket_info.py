import boto3
from prettytable import PrettyTable
p =PrettyTable()

s3_ob=boto3.resource('s3')
p.field_names=["S3 Bucket Name", "S3 Bucket Region"]
for each_b in s3_ob.buckets.all():
	p.add_row([each_b.name, "us-east-1"])
print(p)

