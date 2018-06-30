package main

import (
	"fmt"
	"net/http"

	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/ec2metadata"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/dynamodb"
)

var version string

func HandlerRoot(w http.ResponseWriter, r *http.Request) {
	msg := "i am groot " + version
	fmt.Fprintf(w, msg)
}
func HandlerHealthcheck(w http.ResponseWriter, r *http.Request) {
	msg := "bealthy " + version + "\n"
	fmt.Fprintf(w, msg)
	svc := ec2metadata.New(session.New(), aws.NewConfig())
	iden, err := svc.GetInstanceIdentityDocument()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}
	fmt.Fprintf(w, "%s\n", iden.InstanceID)
}

func HandlerData(w http.ResponseWriter, r *http.Request) {
	svc := dynamodb.New(session.New(), &aws.Config{Region: aws.String("us-east-2")})
	tableName := "gdata"
	query := dynamodb.ScanInput{
		TableName: &tableName,
	}
	output, err := svc.Scan(&query)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}
	for _, item := range output.Items {
		fmt.Fprintf(w, "%s\n", *item["color"].S)
	}
	msg := "\nbealthy " + version
	fmt.Fprintf(w, msg)
}

func main() {
	http.HandleFunc(fmt.Sprintf("/healthcheck"), HandlerHealthcheck)
	http.HandleFunc(fmt.Sprintf("/"), HandlerRoot)
	http.HandleFunc(fmt.Sprintf("/data"), HandlerData)
	listenString := "0.0.0.0" + ":" + "5000"
	// precompile some regexes
	http.ListenAndServe(listenString, nil)
}
