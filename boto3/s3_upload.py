import boto3
import os

def upload_to_s3(file_path, bucket_name, s3_key):
    print(f"UPLOADING TO S3")
    
    s3 = boto3.client('s3')
    
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found")
        return
    
    print(f"Uploading {file_path} to s3://{bucket_name}/{s3_key}")
    
    s3.upload_file(file_path, bucket_name, s3_key)
    
    print(f"Upload complete!")
    print(f"URL: http://{bucket_name}.s3-website-us-east-1.amazonaws.com/{s3_key}")

if __name__ == "__main__":
    upload_to_s3(
        file_path="/home/fina/cloudjourney/webproject-index.html",
        bucket_name="fina-cloud-portfolio",
        s3_key="index.html"
    )
