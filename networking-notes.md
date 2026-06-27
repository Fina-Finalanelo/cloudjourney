# Cloud Networking Concepts

## Core Networking Fundamentals
- IP Address: unique number identifying a device on a network
- IPv4: 32-bit addressing (example: 192.168.1.1)
- IPv6: 128-bit addressing (handles more devices)
- Subnet: smaller section of a larger network for organisation and security
- DNS: translates domain names like google.com into IP addresses
- Port: numbered channel for network services (port 80: HTTP, port 443: HTTPS, port 22: SSH)
- Firewall: monitors and controls incoming and outgoing traffic based on rules

## AWS Cloud Networking

### VPC (Virtual Private Cloud)
Your own private network inside AWS.
All AWS resources live inside a VPC.
Think of it as your private office building inside the AWS cloud.

### Subnets
- Public Subnet: can reach the internet, used for web servers
- Private Subnet: no direct internet access, used for databases

### Internet Gateway
Connects your VPC to the internet.
Without it, nothing in your VPC can send or receive internet traffic.

### Security Groups
AWS version of a firewall attached to individual resources.
Common rules:
- Port 22 from my IP only: SSH access
- Port 80 from anywhere: HTTP web traffic
- Port 443 from anywhere: HTTPS web traffic
- Deny everything else by default

### NAT Gateway
Allows private subnet resources to reach the internet outbound only.
Nothing from the internet can initiate a connection inward.
Used for: downloading updates on a private database server.

### Route Tables
Rules that direct where network traffic should go.
Public subnet route table sends all internet traffic through the Internet Gateway.

### Route 53
AWS DNS service.
Maps your domain name to your server IP address.

### Elastic IP
A static public IP address in AWS.
Attach to an EC2 instance so the IP never changes when you restart the server.

## Classic AWS Architecture Pattern
Internet → Internet Gateway → VPC → Public Subnet (web server) → Private Subnet (database)
