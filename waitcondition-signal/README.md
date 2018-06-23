# waitcondition-signal
CloudFormation testing for spinning up an ec2 instance with userdata that runs ansible-pull and sends a custom waitcondition signal when the playbook is done. 

Usage:
```
python uplaunch.py ./waitcondition-signal/ud-only.json
```

Will result in a `/var/lib/cloud/instance/scripts/part-001` script that looks something like this:
```
#!/bin/bash -xe
export WAITHANDLE='https://cloudformation-waitcondition-us-east-2.s3.us-east-2.amazonaws.com/arn%3Aaws%3Acloudformation%3Aus-east-2%3A514723210267%3Astack/rpers-testing-254964c0-6694-11e8-901d-d0577bb471fb/256e51e0-6694-11e8-8bd0-50faf8bc7cae/ApplicationWaitHandle?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20180602T183833Z&X-Amz-SignedHeaders=host&X-Amz-Expires=86399&X-Amz-Credential=AKIAI722P7Q4X76EQLQA%2F20180602%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Signature=1392d0c9ffc810f1b85451761cb60d2483519aec3d51898b1fd80f77796b8cd1'
yum install python-pip -y
yum install git -y
pip install ansible
/usr/local/bin/ansible-pull -U https://github.com/rendicott/dcert ./waitcondition-signal/play.yml
```
