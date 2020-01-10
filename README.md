# Ec2-Auto-StartStop
AWS Lambda function to start and stop EC2 instances with a specific tag associated.


# How to deploy
Full write up of the use-case here: https://how2cloud.quix.co.za/2019/04/tut-auto-start-stop-ec2/

- Create a new python2 lambda function (code inline)
- Paste the code to the new function
- Amend the mytag variable to match your environment
- Duplicate this tag to your EC2 instances
- Automate the execution with AWS Cloudwatch

NOTE: Any instances tagged with the tag defined in the function will be started when in a stopped state, or stopped when in a started state.
