package main

import (
  "fmt"
  "io/ioutil"
)

func main() {
  var data, err = ioutil.ByteReader("/home/henry/Documents/adventOfCode/adventOfCode/day1ButIDoItInGo/input")
  fmt.Println(err)
  fmt.Println(data)
}
