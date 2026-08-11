# Cloud Engineering Portfolio
### Fina Finalanelo | Johannesburg, South Africa

Hands-on cloud engineering portfolio documenting real AWS infrastructure builds, Linux system administration, and automation projects. Built while self-studying toward a Junior Cloud Engineer role.

Contact: finalenelo@gmail.com
LinkedIn: linkedin.com/in/fina-phele
Portfolio: http://fina-cloud-portfolio.s3-website-us-east-1.amazonaws.com

---

## Skills Demonstrated in This Repository

- Linux system administration on Ubuntu 24.04
- AWS infrastructure: EC2, S3, IAM, VPC, RDS, Lambda, Auto Scaling
- Cloud networking: VPC, subnets, internet gateway, security groups, route tables
- Infrastructure as Code with Terraform
- Python automation with Boto3
- Containerisation with Docker
- CI/CD pipelines with GitHub Actions
- Git version control and documentation

---

## Repository Contents

linux-commands.md
Comprehensive Linux command reference covering navigation, permissions, users, SSH, package management, processes, services and log files. Built from hands-on practice on a real Ubuntu server.

server-setup.md
Step by step guide to setting up a fresh Ubuntu server as a production-ready web server. Documents the exact process used when provisioning real AWS EC2 instances.

networking-notes.md
Cloud networking concepts covering VPC architecture, subnets, internet gateways, security groups, NAT gateways, route tables, Route 53 and Elastic IPs. Applied directly to real AWS builds.

iam-notes.md
AWS IAM documentation covering users, groups, policies, roles and the principle of least privilege. Includes real account structure built on AWS.

s3-notes.md
AWS S3 documentation covering bucket creation, static website hosting, bucket policies and public access configuration. Includes live hosted portfolio website.

rds-notes.md
AWS RDS documentation covering MySQL database creation in a private subnet, DB subnet groups, and secure architecture patterns.

autoscaling-notes.md
Auto Scaling and Load Balancing documentation covering launch templates, Auto Scaling Groups, target tracking policies and load balancer configuration.

lambda-notes.md
AWS Lambda documentation covering serverless functions, Python runtime, triggers, and execution results.

webproject-index.html
Portfolio webpage served live via both EC2 nginx and S3 static hosting.

---

## AWS Architecture Built

Internet
    |
Internet Gateway
    |
Custom VPC (10.0.0.0/16)
    |
    Public Subnet (10.0.0.0/20) - us-east-1a
    └── EC2 t3.micro (Ubuntu 24.04, nginx)
        Security Group: ports 22, 80, 443
    |
    Private Subnet (10.0.128.0/20) - us-east-1a
    └── RDS MySQL db.t4g.micro
        Security Group: port 3306 from public subnet only

Auto Scaling Group: min 1, desired 1, max 3 instances
Scaling Policy: add capacity when CPU exceeds 50%

---

## Projects

Phase 1: Linux Server Setup
Built and documented a complete Ubuntu server setup including nginx web server, user management, SSH keys, file permissions and service management. Served a live portfolio webpage from the local nginx server.

Phase 2: AWS Cloud Infrastructure
Built a complete AWS environment including custom VPC, EC2 web server, S3 static website, IAM security setup, RDS MySQL database, Auto Scaling Group and Lambda function. All resources built hands-on from scratch.

Phase 3: Infrastructure as Code and Automation
Deployed complete AWS environments using Terraform. Automated cloud resource management with Python and Boto3. Containerised applications with Docker. Built CI/CD pipelines with GitHub Actions for automatic deployment to AWS.

---

## Education

Bachelor of Science in Information Technology
Richfield Graduate Institute of Technology, Johannesburg
Expected 2027 | Current aggregate: 78%

---

## Certifications

- AWS Certified Cloud Practitioner
- AWS Certified Solutions Architect Associate
- Cisco Networking Basics
