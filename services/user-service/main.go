package main

import (
	"encoding/json"
	"net/http"
)

type User struct {
	ID   string `json:"id"`
	Name string `json:"name"`
	Tier string `json:"tier"`
}

func getUser(w http.ResponseWriter, r *http.Request) {
	user := User{
		ID:   "1",
		Name: "Vinod",
		Tier: "gold",
	}
	json.NewEncoder(w).Encode(user)
}

func main() {
	http.HandleFunc("/user", getUser)
	http.ListenAndServe(":8080", nil)
}