# dcert
Practice for AWS DevOps Professional Exam

# Study Notes

## READING
Thoroughly Understand Blue/Green vs A/B Testing
Lifecycle hooks (AutoScaling), Lifecycle Events (OpsWorks), and Lifecycle Policies (S3)!
DynamoDB partitions and performance
BeanStalk and OpsWorks

Play with SQS and SNS
Read about EBS Snapshots

DataPipeline and Cognito

## EXERCISES
Make a Lambda function that is a Custom Resource in a CloudFormation template
Deploy an application using Elastic Beanstalk
Setup CloudWatch logs agent on a few EC2 instances


# Notes
* beanstalk .ebextensions are applied in alphabetical order
   * manual modifications will not be overridden by config files or saved configurations
* opsworks
   * Stacks > Layers > Instances
* dynamo
   * local secondary indexes use same partition key but give you another sort key
   * LSI consumes the same r/w throughput from original table
   * LSI is max 5 per table and has to be specified at creation
   * LSI sort key has to be scalar so no json blobs, etc
   * global secondary indexes give diff partition key and diff sort key
   * GSI has its own r/w throughput specified at creation time
   * throughput
      * 1 RCU is 1 read per second up to 4kb, 1 WCU is 1 write per second up to 1kb
      * e.g., want to read 80 3kb things per seconds so need 80 RCU for strong consistent reads or 40 RCU for eventual consistent read