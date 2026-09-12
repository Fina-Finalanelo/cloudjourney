import boto3

def stop_running_instances():
    print("CHECKING FOR RUNNING INSTANCES")
    ec2 = boto3.client('ec2', region_name='us-east-1')
    
    response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'instance-state-name',
                'Values': ['running']
            }
        ]
    )

    running_ids = []

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            name = "Unnamed"
            if 'Tags' in instance:
                for tag in instance['Tags']:
                    if tag['Key'] == 'Name':
                        name = tag['Value']
            print(f"Found running instance: {name} ({instance['InstanceId']})")
            running_ids.append(instance['InstanceId'])

    if not running_ids:
        print("No running instances found. Nothing to stop.")
    else:
        print(f"\nStopping {len(running_ids)} instance(s)...")
        ec2.stop_instances(InstanceIds=running_ids)
        print("Done. All instances stopped.")

if __name__ == "__main__":
    stop_running_instances()
