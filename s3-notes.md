AWS S3 - Simple Storage Service

What is S3?
S3 is AWS object storage. Store any file - images, videos, documents, backups, code.
Think of it as a giant hard drive in the cloud.

Key Terms
- Bucket: Container for files - like a folder
- Object: Any file stored in a bucket
- Key: The file name/path inside the bucket

What I Built
- Created a bucket called: fina-cloud-portfolio
- Enabled static website hosting
- Uploaded index.html portfolio page
- Added bucket policy to allow public read access
- Hosted my portfolio website on S3

My S3 Website URL
http://fina-cloud-portfolio.s3-website-us-east-1.amazonaws.com

Bucket Policy I Used
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::fina-cloud-portfolio/*"
        }
    ]
}

Reading the Policy
- Effect: Allow - permit this action
- Principal: * - everyone/public
- Action: s3:GetObject - read/download objects
- Resource: fina-cloud-portfolio/* - everything in this bucket

EC2 vs S3 Website Hosting
- EC2 + nginx: has a server to manage, hourly cost, best for dynamic apps
- S3 static hosting: no server, pay per GB, best for static websites

Important S3 Facts
- S3 is global - not tied to one region like EC2
- Bucket names must be unique across all of AWS worldwide
- Free tier gives you 5GB storage
- Data is automatically replicated across multiple locations
- Block Public Access must be off for public websites

Common S3 Use Cases
- Host static websites
- Store website images and files
- Database and server backups
- Log file storage
- File sharing

Golden Rules
- Never store sensitive data in a public bucket
- Always check bucket permissions before making public
- Delete buckets you no longer need to avoid charges
- Bucket names cannot be changed after creation
