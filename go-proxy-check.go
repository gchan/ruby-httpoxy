package main

import (
	"fmt"
	"net/http"
)

func main() {
	req, _ := http.NewRequest("GET", "http://example.com", nil)
	url, _ := http.ProxyFromEnvironment(req)

	fmt.Println("In Go Land (using net/http)")

	if url == nil {
		fmt.Println("No proxy")
	} else {
		fmt.Println("Proxy: " + url.String())
	}
}
