package main

import (
  "fmt"
  "io/ioutil"
  "strings"
)

func main() {
    data, err := ioutil.ReadFile("/home/henry/Documents/adventOfCode/adventOfCode/day1ButIDoItInGo/input")
    if err != nil {
        fmt.Println("File reading error", err)
        return
    }
    fmt.Println("Contents of file:", strings.Split(string(data), "\n"))
    fmt.Println(data[1])
    for _, value := range data {
        fmt.Println(value)
    }
    
}
