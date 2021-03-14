import boto3
import datetime
from prettytable import PrettyTable
p =PrettyTable()

ec2 = boto3.resource('ec2',region_name="us-east-1")
ec2_filter = [{'Name': 'instance-state-name', 'Values': ['stopped']}]

def get_tag(tags, key='Name'):

  if not tags: return ''

  for tag in tags:

    if tag['Key'] == key:
      return tag['Value']

  return ''

p.field_names=["Name","Instance ID","Instance state","Launch date"]
for instance in ec2.instances.filter(Filters=ec2_filter):
    instance_name = get_tag(instance.tags)
    p.add_row([instance_name, instance.id, instance.state['Name'], instance.launch_time])
print(p)

