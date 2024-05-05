package main

import (
	"fmt"
	"log"
	"net/http"
)

func main() {
	fmt.Printf("Server launched\n\n")
	fmt.Printf("Veuillez vous rendre sur l'adresse : \"http://localhost:8080\"\n")

	fs := http.FileServer(http.Dir("../appMedicFront/dist/app-medic-front/browser"))

	http.Handle("/", fs)

	log.Fatal(http.ListenAndServe(":8080", nil))
}
