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
update_stack = ""
try:
    update_stack = sys.argv[3]
except:
    update_stack = ""

url = "https://s3.%s.amazonaws.com/%s/%s" % (region,bucketname,template)


def handle_response(robject):
    scode = robject.get("ResponseMetadata").get("HTTPStatusCode")
    if scode != 200:
        print robject 


def cfn_poller(client, stack_name):
    counter =0
    max = 30
    done = False
    time.sleep(5)
    while True:
        if counter > max:
            break
        response = client.describe_stacks(
            StackName=stack_name,
        )
        handle_response(response)
        for stack in response.get("Stacks"):
            if stack.get("StackName") == stack_name:
                stack_status = stack.get("StackStatus") 
                if (stack_status == "ROLLBACK_COMPLETE" or 
                    stack_status == "UPDATE_ROLLBACK_COMPLETE" or 
                    stack_status == "CREATE_FAILED"):
                    done=True
                    break
                if (stack_status == "CREATE_COMPLETE" or
                    stack_status == "UPDATE_COMPLETE"):
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
if update_stack == "":
    stack_name = stack_prefix + str(uuid.uuid1())
else:
    stack_name = update_stack
print("Attempting to create '%s' using template '%s'" % (stack_name, url))
client = session.client("cloudformation")
if update_stack == "":
    response = client.create_stack(
        StackName=stack_name,
        TemplateURL=url,
        Capabilities=[
            "CAPABILITY_NAMED_IAM"
        ]
    )
else:
    response = client.update_stack(
        StackName=update_stack,
        TemplateURL=url,
        Capabilities=[
            "CAPABILITY_NAMED_IAM"
        ]
    )
handle_response(response)
print response
cfn_poller(client, stack_name)