package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func getOrderingRules(input []string) (orderingRules [][]int) {
	for _, line := range input {
		if line == "" {
			break
		}
		orderingRuleString := strings.Split(line, "|")
		a, _ := strconv.Atoi(orderingRuleString[0])
		b, _ := strconv.Atoi(orderingRuleString[1])
		orderingRules = append(orderingRules, []int{a, b})
	}
	return
}

func getUpdates(input []string) (updates [][]int) {
	hitUpdatesSection := false
	for _, line := range input {
		var pageUpdates []int
		if hitUpdatesSection {
			updatePagesList := strings.Split(line, ",")
			for _, pageUpdate := range updatePagesList {
				a, _ := strconv.Atoi(pageUpdate)
				pageUpdates = append(pageUpdates, a)
			}
			updates = append(updates, pageUpdates)

		} else if line == "" {
			hitUpdatesSection = true
		}
	}
	return
}

func validateUpdateList(updateList []int) bool {

}

var pageOrderingRules [][]int

func dayFive() {
	dataRaw, err := os.ReadFile("inputs/day5.txt")
	if err != nil {
		panic("Uh oh")
	}
	lines := strings.Split(string(dataRaw), "\n")

	pageOrderingRules = getOrderingRules(lines)
	updates := getUpdates(lines)

	fmt.Println(pageOrderingRules)
	fmt.Println(updates)

	for _, update := range updates {
		validateUpdateList(update)
	}

}
