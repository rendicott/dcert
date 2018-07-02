import boto3

session = boto3.Session()
client = session.client("sqs")

q = "https://sqs.us-east-2.amazonaws.com/514723210267/lets-do-some-lines"

struct = {
	"person" : {
	  "name": "bob",
	  "age": "38"
	}
}

response = client.receive_message(QueueUrl=q)

print response
