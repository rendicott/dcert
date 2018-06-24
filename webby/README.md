# webby

Quick and dirty webserver to act as an endpoint for loadbalancer healthchecks etc.

## Building
To build from windows to linux make a batch file with the following contents

```
set GOARCH=amd64
set GOOS=linux
go tool dist install -v pkg/runtime
go install -v -a std
go build -o webby main.go
```