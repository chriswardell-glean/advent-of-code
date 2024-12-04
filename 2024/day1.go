package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	data, err := os.ReadFile("inputs/day1.txt")
	if err != nil {
		panic("Uh oh")
	}
	dataString := string(data)
	locationIdPairs := strings.Split(dataString, "\n")

	var leftHandList []int
	var rightHandList []int

	for i := range locationIdPairs {
		pair := strings.Split(locationIdPairs[i], "   ")
		if len(pair) != 2 {
			fmt.Println("Pair is not length 2", pair)
			continue
		}
		leftHand, err1 := strconv.Atoi(pair[0])
		rightHand, err2 := strconv.Atoi(pair[1])
		if err1 != nil || err2 != nil {
			panic("Problem parsing string to int")
		}
		leftHandList = append(leftHandList, leftHand)
		rightHandList = append(rightHandList, rightHand)
	}

	sort.Ints(leftHandList)
	sort.Ints(rightHandList)

	if len(leftHandList) != len(rightHandList) {
		panic("List lengths not equal")
	}

	total := 0

	for i := range leftHandList {
		leftHand := leftHandList[i]
		rightHand := rightHandList[i]
		difference := rightHand - leftHand
		if difference < 0 {
			difference = difference * -1
		}
		total += difference

	}

	fmt.Println("Difference total:", total)

}
