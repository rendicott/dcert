oldnum=`cut -d ',' -f2 bversion` 
newnum=`expr $oldnum + 1`
sed -i "s/$oldnum\$/$newnum/g" bversion 
go get -u github.com/aws/aws-sdk-go/aws
go build \
    -ldflags "-X main.version=1.0.$newnum" \
    -o bin/application application.go 