AWS VPC - Virtual Private Cloud

What is a VPC?
A VPC is your own private, isolated network inside AWS.
All AWS resources live inside a VPC.
Think of it as your private gated estate inside the AWS cloud.

What I Built
- Created a custom VPC called: my-custom-vpc
- IP range: 10.0.0.0/16 (65,536 possible IP addresses)
- Created a public subnet: 10.0.0.0/20
- Created a private subnet
- Internet Gateway attached to connect VPC to internet
- Two route tables: one for public, one for private subnet
- Security group allowing ports 22, 80, 443
- Launched EC2 instance inside the public subnet
- SSHed into server and confirmed nginx serving a webpage

My Custom VPC Architecture
Internet
    |
Internet Gateway
    |
my-custom-vpc (10.0.0.0/16)
    |
Public Subnet (10.0.0.0/20)
    |
EC2 instance (private IP: 10.0.3.129)
Security Group: allow port 22, 80, 443

Key Components

VPC
Your private network inside AWS.
Nobody else on AWS can access your resources unless you allow it.

Subnets
Public subnet: internet can reach it, used for web servers.
Private subnet: no direct internet access, used for databases.

Internet Gateway
Connects your VPC to the internet.
Without it, nothing in your VPC can send or receive internet traffic.

Route Tables
Rules that direct where network traffic goes.
Public subnet route table sends all internet traffic through the Internet Gateway.
Private subnet route table keeps traffic internal only.

Security Groups
Firewall rules attached to individual EC2 instances.
My security group rules:
- Port 22: SSH access from anywhere
- Port 80: HTTP web traffic from anywhere
- Port 443: HTTPS web traffic from anywhere
- Everything else: blocked by default

Key Concepts
- VPC CIDR /16 gives 65,536 IP addresses
- Subnet CIDR /24 gives 256 IP addresses
- Private IPs in range 10.0.0.0 are inside the VPC
- Public IP is what the internet uses to reach your server
- Always stop EC2 instances when not in use to avoid charges

Golden Rules
- Never put a database in a public subnet
- Always use security groups to restrict access
- Use private subnets for anything that should not be internet-facing
- One internet gateway per VPC
- Route tables control where traffic flows
