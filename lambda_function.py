import boto3

# Definitions
region = 'eu-west-1'
mytag = 'Cust1-SPB'
ec2 = boto3.client('ec2', region_name=region)


def lambda_handler(event, context):
    
    deviceFilters=[
        {
            'Name': 'tag:DeviceCategory',
            'Values': [
                mytag,
                ]
        },
    ]
    
    instance_ids = []
    ec2Reservations = ec2.describe_instances(Filters=deviceFilters)['Reservations']
    
    for reservation in ec2Reservations:
          ec2Instances = reservation['Instances']
          for instance in ec2Instances:
              instance_ids.append(instance['InstanceId'])
              
    print("Starting instance: {}".format(','.join(instance_ids)))
    ec2.start_instances(InstanceIds=instance_ids)
    
