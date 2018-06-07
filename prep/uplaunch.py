import boto3
import sys
import uuid
import time
import json

# arn:aws:s3:::raws-builds
stack_prefix = sys.argv[2]
bucketname = "raws-builds"
region = "us-east-2"
template = sys.argv[1]
url = "https://s3.%s.amazonaws.com/%s/%s" % (region,bucketname,template)


def handle_response(robject):
    scode = robject.get("ResponseMetadata").get("HTTPStatusCode")
    if scode != 200:
        print robject 


def cfn_poller(client, stack_name):
    counter =0
    max = 30
    done = False
    while True:
        if counter > max:
            break
        response = client.describe_stacks(
            StackName=stack_name,
        )
        handle_response(response)
        for stack in response.get("Stacks"):
            if stack.get("StackName") == stack_name:
                if stack.get("StackStatus") == "CREATE_COMPLETE":
                    print json.dumps(
                        stack.get("Outputs"),
                        indent=4
                    )
                    try:
                        # grab the pub ip if possible
                        for output in stack.get("Outputs"):
                            if output.get("OutputKey") == "PublicIP":
                                print output.get("OutputValue")
                    except:
                        pass
                    done = True
                    break
                else:
                    print("Status: '%s', Attempt: '%d/%d'" % (stack.get("StackStatus"), counter, max))
        if done:
            break
        time.sleep(10)
        counter += 1



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
client = session.client("cloudformation")
response = client.create_stack(
    StackName=stack_name,
    TemplateURL=url
)
handle_response(response)
print response
cfn_poller(client, stack_name)