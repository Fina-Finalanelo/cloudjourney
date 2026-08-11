# Cloud Engineering Journey

A portfolio documenting my hands-on learning path toward becoming a Junior Cloud Engineer, built on Ubuntu Linux, Git, and AWS.

## About Me
Junior Cloud Engineer in training based in Johannesburg, South Africa.
Targeting AWS cloud roles with hands-on skills in Linux, networking, and cloud infrastructure.
Currently self-studying toward AWS Cloud Practitioner certification.

## Phase 1: Foundations (Complete)

Linux System Administration
- File system navigation and management
- File permissions with chmod and chown
- User and group management
- SSH key generation and remote access
- Package management with apt
- Process management
- Service management with systemctl
- Deployed and managed nginx web server
- Completed full server setup mini project

Networking
- IPv4 and IPv6 addressing
- Subnetting and DNS
- Ports and protocols
- Firewalls and routing
- AWS VPC, subnets, security groups, NAT gateway, route tables

Git and GitHub
- Repository management
- Branching and merging
- Documentation with Markdown

## Phase 2: AWS Core Cloud Skills (Complete)

EC2 - Elastic Compute Cloud
- Launched Ubuntu EC2 instances on AWS
- Connected via SSH from Johannesburg to Virginia
- Installed and configured nginx web server
- Served live portfolio page to the internet
- Launched EC2 inside custom VPC

IAM - Identity and Access Management
- Created IAM users and groups
- Attached policies following least privilege principle
- Created dedicated admin user for daily AWS work
- Stopped using root account for daily tasks

S3 - Simple Storage Service
- Created S3 bucket with static website hosting
- Configured bucket policy for public access
- Hosted portfolio webpage on S3
- Live at: http://fina-cloud-portfolio.s3-website-us-east-1.amazonaws.com

VPC - Virtual Private Cloud
- Built custom VPC with 10.0.0.0/16 CIDR
- Created public and private subnets
- Configured internet gateway and route tables
- Launched EC2 instance inside custom VPC
- Confirmed nginx serving from custom VPC server

RDS - Relational Database Service
- Created MySQL database in private subnet
- Configured DB subnet group across multiple AZs
- Applied secure architecture: database not publicly accessible

Auto Scaling and Load Balancing
- Created launch template for Ubuntu nginx server
- Configured Auto Scaling Group with min 1, max 3 instances
- Set target tracking policy: scale when CPU exceeds 50%

Lambda - Serverless Computing
- Created Python Lambda function
- Deployed and tested successfully
- Executed in 1.79ms with zero server management

## Phase 3: Automation and Modern Tools (In Progress)
- Terraform
- Python and Boto3
- Docker
- CI/CD with GitHub Actions

## Repository Structure
- linux-commands.md: Linux command reference guide
- server-setup.md: Step by step Ubuntu server setup guide
- networking-notes.md: Cloud networking concepts
- iam-notes.md: AWS IAM documentation
- s3-notes.md: AWS S3 and static hosting documentation
- rds-notes.md: AWS RDS database documentation
- autoscaling-notes.md: Auto Scaling and Load Balancing documentation
- lambda-notes.md: AWS Lambda serverless documentation
- notes.txt: Personal learning notes

## Tools and Technologies
- Ubuntu 24.04 LTS on WSL2
- Git 2.43
- nginx
- AWS: EC2, IAM, S3, VPC, RDS, Auto Scaling, Lambda
- Python 3.12
- Terraform (Phase 3 - upcoming)
- Docker (Phase 3 - upcoming)

## Certifications
- Cisco Networking Basics (complete)
- AWS Cloud Practitioner (upcoming)
- AWS Solutions Architect Associate (planned)
