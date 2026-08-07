AWS IAM - Identity and Access Management

What is IAM?
IAM lets you control who can access your AWS account and what they can do.
Never use the root account for daily work - always use IAM users.

Core Components

| Component | Purpose | Example |
|-----------|---------|---------|
| Users | Individual people needing AWS access | fina-admin |
| Groups | Collections of users with same permissions | developers |
| Policies | Rules defining what is allowed or denied | AdministratorAccess |
| Roles | Permissions attached to services, not people | EC2 can access S3 |

What I Built
- Created a group called: developers
- Attached policy: AdministratorAccess
- Created IAM user: fina-admin
- Added fina-admin to developers group
- Now use fina-admin for all daily AWS work

The Principle of Least Privilege
Give users ONLY the permissions they need - nothing more.
Example:
- Developer: EC2 + S3 access only
- Auditor: Read only access
- Finance: Billing access only
- Nobody: Root account access for daily work

My Account Structure
Root account (emergency use only)
    └── developers group (AdministratorAccess)
            └── fina-admin (daily use)

IAM Sign-in URL
https://702921688176.signin.aws.amazon.com/console

Common Policies
| Policy | What it allows |
|--------|---------------|
| AdministratorAccess | Full access to everything |
| PowerUserAccess | Everything except IAM management |
| ReadOnlyAccess | View everything, change nothing |
| AmazonEC2FullAccess | Full EC2 access only |
| AmazonS3FullAccess | Full S3 access only |

Golden Rules
- Never share your AWS credentials with anyone
- Never commit AWS keys to GitHub
- Always use IAM users, never root for daily work
- Apply least privilege - only give permissions needed
- Enable MFA on root account
