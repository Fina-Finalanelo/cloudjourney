# Server Architecture

## Phase 1 Local Setup
WSL2 Ubuntu 24.04

│

├── /home/fina/

│   ├── cloudjourney/      (Git repository - this project)

│   ├── webproject/        (web project directory)

│   │   └── index.html

│   └── .ssh/

│       ├── id_rsa         (private key - 600)

│       └── id_rsa.pub     (public key - 644)

│

└── Services Running

└── nginx (active, enabled on boot)

## Users and Permissions
- fina: primary user, sudo group member
- teammate: secondary user, sudo group member
- clouduser: test user, sudo group member

## File Permissions Applied
- webproject/ : 755 (rwxr-xr-x)
- index.html  : 644 (rw-r--r--)
- id_rsa      : 600 (rw-------)
- id_rsa.pub  : 644 (rw-r--r--)

## Phase 2 Target Architecture (AWS)
Internet
    │
Internet Gateway
    │
VPC (10.0.0.0/16)
    ├── Public Subnet (10.0.1.0/24)
    │   └── EC2 Instance (nginx web server)
    │       Security Group: allow 80, 443, 22
    │
    └── Private Subnet (10.0.2.0/24)
        └── RDS Database
            Security Group: allow 3306 from public subnet only
