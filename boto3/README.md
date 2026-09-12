Python Boto3 AWS Automation Scripts

Scripts that automate AWS operations using Python and Boto3.

list_resources.py
Lists all EC2 instances, S3 buckets and VPCs in your AWS account.
Run: python3 list_resources.py

stop_instances.py
Finds and stops all running EC2 instances automatically.
Use case: scheduled to run nightly to save costs on dev servers.
Run: python3 stop_instances.py

s3_upload.py
Uploads a file to an S3 bucket.
Use case: deploy updated portfolio page to S3 with one command.
Run: python3 s3_upload.py
