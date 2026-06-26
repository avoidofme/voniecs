// Package von
package von

import (
	"log"
	"net/http"

	"github.com/gin-gonic/gin"
)

func Start() {
	r := gin.Default()
	v1 := r.Group("api/v1")
	{
		v1.GET("/hw", handleHw)
	}

	if err := r.Run("0.0.0.0:8080"); err != nil {
		log.Fatal("fail to run vonapi")
	}
}

func handleHw(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, gin.H{"message": "hellow orld"})
}
