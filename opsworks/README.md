# opsworks
Just some notes from messing around with OpsWorks

## Setup
Built a stack like this:
```
russell@rinux:~/source/dcert/opsworks$ aws opsworks create-stack --default-subnet-id subnet-ba9ec9f7 --name oopsworks --default-os "Ubuntu 16.04 LTS" --hostname-theme Wild_Cats --default-ssh-key-name rperse-o-2 --service-role-arn arn:aws:iam::514723210267:role/aws-opsworks-service-role --default-instance-profile-arn arn:aws:iam::514723210267:instance-profile/aws-opsworks-ec2-role --stack-region us-east-2 --configuration-manager Name=Chef,Version=12 --vpc-id vpc-de5c6db7
{
    "StackId": "19b67417-20f1-444a-80a7-1d19fd1f14b3"
}
```

Then creating a layer
```
russell@rinux:~/source/dcert/opsworks$ aws opsworks create-layer --stack-id 19b67417-20f1-444a-80a7-1d19fd1f14b3 --name web-layer --custom-instance-profile-arn arn:aws:iam::514723210267:instance-profile/dynamoreader --no-auto-assign-public-ips --no-auto-assign-elastic-ips --install-updates-on-boot --shortname web-layer-sn --type custom
{
    "LayerId": "2729711c-7c44-488f-bbcc-e3138f9c63e5"
}
```

Then I made an ELB using my mouse (eww) and attached
```
russell@rinux:~/source/dcert/opsworks$ aws opsworks attach-elastic-load-balancer --elastic-load-balancer-name oopsworks --layer-id 2729711c-7c44-488f-bbcc-e3138f9c63e5
russell@rinux:~/source/dcert/opsworks$ 
```


After I created an app and added a recipe/cookbook repo I could update custom cookbooks with this command
```
russell@rinux:~/source/dcert/opsworks$ aws opsworks create-deployment --app-id 69f5a94e-3ed7-45dd-af36-a210c038871e --stack-id 19b67417-20f1-444a-80a7-1d19fd1f14b3 --command "{\"Name\":\"update_custom_cookbooks\"}"
{
    "DeploymentId": "517e8f0c-dd0d-4e31-9dd3-a76d2de12986"
}
```
