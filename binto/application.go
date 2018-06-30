package main

import (
	"fmt"
	"net/http"
)

var (
	version = "0.1"
)

func HandlerRoot(w http.ResponseWriter, r *http.Request) {
	msg := "i am groot " + version
	fmt.Fprintf(w, msg)
}
func HandlerHealthcheck(w http.ResponseWriter, r *http.Request) {
	msg := "bealthy " + version
	fmt.Fprintf(w, msg
}

func main() {
	http.HandleFunc(fmt.Sprintf("/healthcheck"), HandlerHealthcheck)
	http.HandleFunc(fmt.Sprintf("/"), HandlerRoot)
	listenString := "0.0.0.0" + ":" + "5000"
	// precompile some regexes
	http.ListenAndServe(listenString, nil)
}
