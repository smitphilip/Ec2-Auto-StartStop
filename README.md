# Ec2-Auto-StartStop
AWS Lambda function to start and stop EC2 instances with a specific tag associated.


# How to deploy
Full write up of the use-case here: http://how2cloud.blog/2019/04/23/auto-start-and-stop-ec2-instances/

- Create a new python2 lambda function (code inline)
- Paste the code to the new function
- Duplicate the code, one for start, one for stop (feature improvement in the works)
- Automate the execution with AWS Cloudwatch

