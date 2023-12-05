

# Optimizing costs by converting EBS volume types from GP2 to GP3 using Lambda and CloudWatch

As a Cloud Engineering team we take care of the AWS environment and make sure it is in compliance with the organizational policies.
We use AWS cloud watch in combination with AWS Lambda to govern the resources according to the policies.
For example, we Trigger a Lambda function when an Amazon Elastic Block Store (EBS) volume is created. We use Amazon CloudWatch Events. CloudWatch Events that allows us to monitor and respond to EBS volumes that are of type GP2 and convert them to type GP3.

## Follow below steps to complete this project
1. Go to lambda create lambda function give any name select runtime python 3.10 and create.
2.  Lambda is an event drive program to trigger event we need to create event in Cloudwatch so Go to Cloudwatch 
```bash
CLOUDWATCH Rules Steps under events create rules

  event source : AWS Services
  AWS Services : EC2
  Event Type : EBS Volume Notification
  Event type specification 1 -> specific event : createvolume
  Target : Lambda function
  function : select lambda function you have created erlier.
  click on create.
```
3. Now we need to verify when EBS Volume created lambda will trigger Cloudwatch so go to Cloudwatch click on log groups check the latest log see if lambda got triggered.

4. In lambda function there is one default lambda function will there know as lambda handler that's the one got triggered as soon as lambda called.      

(event,context) now event and context are needs to provided by invoking resource. now in our case we are invoking via Cloudwatch.

as cloud engineer you can use the event deatils to write the lambda function .

5. Now delete the EBS volume and create GP2 volume also go to lambda add 
```bash
  print(event)
```
now go to Cloudwatch log groups check the recent log now you will the complete deatils of volume copy that and go to web JSON formatter.

6. now paste the JSON output from the web to our lambda function for our reference 

```bash
event = {paste JSON code} 
```

7. now refer pyhon code file for lambda function copy the complete code and paste in the lambda code. we are using boto3 module here 

8. now we need to add IAM role permission in lambda to access the Cloudwatch Service and trigger our function.
go to configration / permission
```
IAM role permissions :
describeVolume
ModifyVolume
```

now craete EBS volume GP2 and refresh the page if volume automatically chnaged to GP3 that means you have successfully completed this project.


Project: Optimizing Costs through EBS Volume Type Conversion

Description:

Implemented a cost optimization initiative by converting Amazon Elastic Block Store (EBS) volume types from GP2 to GP3 using serverless architecture.

Key Achievements:

Utilized AWS Lambda functions to automate the conversion process, enhancing operational efficiency.
Implemented event-driven triggers using AWS CloudWatch to initiate volume type conversions based on predefined criteria.
Achieved a [insert percentage]% reduction in storage costs by migrating to the more cost-effective GP3 volume type.
Ensured minimal impact on system performance and availability during the transition.
Technologies Used:

AWS Lambda
Amazon EBS (GP2 and GP3)
AWS CloudWatch
Serverless architecture

THANK YOU 
