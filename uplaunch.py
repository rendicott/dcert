import boto3
import sys
import uuid

# arn:aws:s3:::raws-builds
stack_prefix = "rpers-testing-"
bucketname = "raws-builds"
region = "us-east-2"
template = sys.argv[1]
url = "https://s3.%s.amazonaws.com/%s/%s" % (region,bucketname,template)


def handle_response(robject):
    scode = robject.get("ResponseMetadata").get("HTTPStatusCode")
    if scode != 200:
        print robject 


session = boto3.Session()
client = session.client("s3")
with open(template, 'rb') as f:
    response = client.put_object(
        Bucket=bucketname,
        Body=f,
        Key=template
    )
    handle_response(response)
    
stack_name = stack_prefix + str(uuid.uuid1())
print("Attempting to create '%s' using template '%s'" % (stack_name, url))
session = boto3.Session()
client = session.client("cloudformation")
response = client.create_stack(
    StackName=stack_name,
    TemplateURL=url
)
handle_response(response)
print response