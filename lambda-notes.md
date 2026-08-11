AWS Lambda - Serverless Computing

What is Lambda?
Lambda lets you run code without managing servers.
You write a function, upload it, and it only runs when triggered.
You pay only for the milliseconds it actually runs.

Traditional vs Serverless
Traditional EC2: server running 24/7, paying 24/7
Lambda: function runs only when needed, paying only when it runs

What I Built
- Created a Python Lambda function called: my-first-function
- Modified it to return a custom message
- Tested it successfully

My Function
def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Fina in Johannesburg!')
    }

Function Execution Results
- Status: Succeeded
- Duration: 1.79 ms
- Billed Duration: 72 ms
- Memory used: 37 MB of 128 MB

Key Concepts
- Function: your code that Lambda runs
- Trigger: what causes your function to run
- Runtime: the language your code runs in (Python, Node.js, etc.)
- Handler: the entry point function Lambda calls
- Execution role: IAM role giving your function permissions
- Event: data passed to your function when triggered

Common Lambda Triggers
- API Gateway: run function when an API receives a request
- S3: run function when a file is uploaded
- CloudWatch Events: run function on a schedule
- DynamoDB: run function when database changes
- SNS/SQS: run function when a message is received

Real World Use Cases
- Resize images automatically when uploaded to S3
- Process data from a form submission
- Run scheduled cleanup tasks
- Handle API requests without a server
- Automate AWS tasks

Lambda Free Tier
- 1 million free requests per month
- 400,000 GB-seconds of compute time per month
- Free tier does not expire after 12 months

Golden Rules
- Lambda functions must complete within 15 minutes maximum
- Keep functions small and focused on one task
- Use environment variables for configuration
- Always assign least privilege IAM roles
- Monitor execution duration and memory usage
