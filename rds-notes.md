AWS RDS - Relational Database Service

What is RDS?
RDS is AWS's managed database service.
Instead of installing and managing a database yourself on an EC2 server,
AWS handles backups, updates, hardware failures and scaling for you.

What I Built
- Created a MySQL database called: my-first-db
- Instance type: db.t4g.micro (free tier)
- Storage: 20 GiB
- VPC: my-custom-vpc-vpc
- Public access: No (private - only EC2 can reach it)
- Master username: admin
- Endpoint: my-first-db.curo0ga8qv27.us-east-1.rds.amazonaws.com

How EC2 Connects to RDS
From the EC2 server you would run:
mysql -h my-first-db.curo0ga8qv27.us-east-1.rds.amazonaws.com -u admin -p

Full Architecture
Internet
    |
Internet Gateway
    |
my-custom-vpc (10.0.0.0/16)
    |
    Public Subnet (us-east-1a)
    └── EC2 web server (nginx) - public IP accessible
    |
    Private Subnets (us-east-1a + us-east-1b)
    └── RDS MySQL database - no public access

Why Private Subnet for Database?
- Database contains sensitive data
- Should never be directly accessible from internet
- Only the EC2 web server can talk to it
- This is the standard secure architecture pattern

DB Subnet Group
RDS requires subnets in at least 2 Availability Zones for redundancy.
Created subnet group covering us-east-1a and us-east-1b.

Databases RDS Supports
- MySQL
- PostgreSQL
- MariaDB
- Oracle
- Microsoft SQL Server
- Amazon Aurora (AWS's own high-performance database)

Golden Rules
- Always put databases in private subnets
- Never give databases public access unless absolutely necessary
- Always stop RDS instances when not in use to save free tier hours
- Save your endpoint and credentials securely
- RDS free tier: 750 hours per month of db.t4g.micro
