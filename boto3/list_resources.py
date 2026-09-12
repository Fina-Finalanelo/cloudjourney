import boto3

def list_ec2_instances():
    print("EC2 INSTANCES")
    ec2 = boto3.client('ec2', region_name='us-east-1')
    response = ec2.describe_instances()

    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances.append(instance)

    if not instances:
        print("No instances found")
    else:
        for instance in instances:
            name = "Unnamed"
            if 'Tags' in instance:
                for tag in instance['Tags']:
                    if tag['Key'] == 'Name':
                        name = tag['Value']

            print(f"Name: {name}")
            print(f"ID: {instance['InstanceId']}")
            print(f"State: {instance['State']['Name']}")
            print(f"Type: {instance['InstanceType']}")
            print("---")

def list_s3_buckets():
    print("S3 BUCKETS")
    s3 = boto3.client('s3')
    response = s3.list_buckets()

    if not response['Buckets']:
        print("No buckets found")
    else:
        for bucket in response['Buckets']:
            print(f"Bucket: {bucket['Name']}")
            print(f"Created: {bucket['CreationDate']}")
            print("---")

def list_vpcs():
    print("VPCS")
    ec2 = boto3.client('ec2', region_name='us-east-1')
    response = ec2.describe_vpcs()

    for vpc in response['Vpcs']:
        name = "Unnamed"
        if 'Tags' in vpc:
            for tag in vpc['Tags']:
                if tag['Key'] == 'Name':
                    name = tag['Value']

        print(f"Name: {name}")
        print(f"ID: {vpc['VpcId']}")
        print(f"CIDR: {vpc['CidrBlock']}")
        print(f"Default: {vpc['IsDefault']}")
        print("---")

if __name__ == "__main__":
    list_s3_buckets()
    print()
    list_vpcs()
    print()
    list_ec2_instances()
