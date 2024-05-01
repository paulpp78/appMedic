package main

import (
	"fmt"
	"log"
	"net/http"
)

func main() {
	fmt.Printf("Server launched\n")

	fs := http.FileServer(http.Dir("../appMedicFront/dist/app-medic-front"))

	http.Handle("/", fs)

	log.Fatal(http.ListenAndServe(":8080", nil))
}

// go run
// go build main.go -o name.exe
