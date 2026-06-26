package main

import (
	"log"
	"net/http"

	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()
	r.GET("/", handleRoot)
	if err := r.Run("localhost:8080"); err != nil {
		log.Fatal("failed to run vonapi")
	}
}

func handleRoot(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, gin.H{"message": "hellow orld"})
}
