# Ubuntu Server Setup Guide

A step by step guide to setting up a fresh Ubuntu server as a web server.
This simulates what a junior cloud engineer does when given a new AWS EC2 instance.

## Prerequisites
- Ubuntu 24.04 LTS
- sudo access
- SSH key pair

## Step 1 - Update the Server
Always the first command on any new server.
```bash
sudo apt update
```

## Step 2 - Install nginx Web Server
```bash
sudo apt install nginx -y
sudo systemctl enable nginx
sudo systemctl start nginx
sudo systemctl status nginx
```
Expected output: Active: active (running)

## Step 3 - Create a New User
```bash
sudo adduser teammate
sudo usermod -aG sudo teammate
groups teammate
```

## Step 4 - Set Up Project Directory
```bash
mkdir ~/webproject
touch ~/webproject/index.html
chmod 755 ~/webproject
chmod 644 ~/webproject/index.html
ls -la ~/webproject/
```

## Step 5 - Verify SSH Keys
```bash
ls -la ~/.ssh/
```
Expected output:
- id_rsa with permissions 600 (private key - owner only)
- id_rsa.pub with permissions 644 (public key - readable)

## Step 6 - Confirm Services are Running
```bash
sudo systemctl status nginx
```

## Key Concepts
- Always run apt update before installing anything
- nginx enables automatically on boot after systemctl enable
- Private SSH keys must have 600 permissions or AWS will reject them
- New users need sudo group membership for admin tasks
