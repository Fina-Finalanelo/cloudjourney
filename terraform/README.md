Terraform AWS Infrastructure

This Terraform configuration deploys a complete AWS environment including a custom VPC, public subnet, internet gateway, route table, security group and EC2 web server.

Resources created:
- VPC with CIDR 10.0.0.0/16
- Public subnet in us-east-1a
- Internet gateway
- Route table with internet access
- Security group allowing ports 22, 80 and 443
- EC2 t3.micro Ubuntu web server

How to use:
terraform init
terraform plan
terraform apply
terraform destroy
