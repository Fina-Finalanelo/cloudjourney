AWS Auto Scaling and Load Balancing

What is Auto Scaling?
Auto Scaling automatically adds or removes EC2 servers based on demand.
You define minimum, desired and maximum number of servers.
AWS handles everything else automatically.

What is a Load Balancer?
A load balancer sits in front of your servers and distributes incoming traffic evenly across them.
No single server gets overwhelmed.

How They Work Together
Traffic spikes → Auto Scaling adds servers → Load Balancer distributes traffic
Traffic drops → Auto Scaling removes servers → Load Balancer adjusts

What I Built
- Created a Launch Template: my-web-server-template
- Ubuntu 24.04, t3.micro, my-first-server-key
- Created an Auto Scaling Group: my-web-server-asg
- Desired capacity: 1 server
- Minimum: 1 server
- Maximum: 3 servers
- Scaling policy: add servers when CPU exceeds 50%
- VPC: my-custom-vpc-vpc

Launch Template
A saved configuration that tells Auto Scaling what kind of server to launch.
Includes: AMI, instance type, key pair, security group.
Auto Scaling uses this template every time it needs to launch a new server.

Auto Scaling Group Settings
- Desired capacity: how many servers you want running normally
- Minimum: never go below this number
- Maximum: never exceed this number
- Target tracking policy: automatically scale based on a metric like CPU usage

Real World Use Case
Normal traffic: 1 server running
Traffic spike: CPU hits 50%, Auto Scaling launches 2 more servers
Traffic drops: Auto Scaling terminates extra servers
You only pay for what you use

Golden Rules
- Always set a maximum capacity to control costs
- Delete Auto Scaling groups when not in use - they keep launching instances
- Use launch templates not launch configurations (newer and better)
- Target tracking policies are the simplest scaling approach
- Load balancers require subnets in at least 2 Availability Zones
