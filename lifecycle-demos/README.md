# LifeCycle Demos

Cloudformation template and supporting files to build a web tier of ec2 instances in an autoscaling group behind an ELB. If the ASG ever terminates one of its instances it will send a lifecycle hook to an SNS topic that will execute a lambda that will execute an SSM RunCommand that will cause the instance to create a tarball of /var/log and upload to s3 for forensics.

## To Deploy

1. Zip up the `lambda-function.py` and upload to a bucket in your account. Take note of the bucket name and key path to the zip so you can enter it into the cloudformation template parameters.
1. Update the ansible playbook `play.yml` to make sure it's installing something that will listen on `0.0.0.0:80` on the ec2 instances. In my case I just made a quick and dirty golang web app that runs as a service in Amazon Linux. 
1. In the cloudformation template `lc.yml` look for the UserData script in the LaunchConfiguration and update the github playbook path.
1. If you want to use the uploader script to deploy the template then update details in the top of the `uplaunch.py` script (e.g., bucket name for CloudFormation template) and then run `python uplaunch.py <template-file> <stack-prefix>` like `python uplaunch.py lc.yml lifecycle-testing-` and it will create a stack with the prefix followed by a guid string. 
1. Alternatively, if you don't want to mess with the uploader script just launch the stack through the console and upload `lc.yml` in the browser. 