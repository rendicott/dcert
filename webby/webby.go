package main

import (
	"net/http"
	"fmt"
)

var (
	version = "0.1"
)
func HandlerHealthcheck(w http.ResponseWriter, r *http.Request) {
	msg := "healthy " + version
	fmt.Fprintf(w, msg)
}

func main() {
	http.HandleFunc(fmt.Sprintf("/healthcheck"), HandlerHealthcheck)
	listenString := "0.0.0.0" + ":" + "80"
	// precompile some regexes
	http.ListenAndServe(listenString, nil)
}