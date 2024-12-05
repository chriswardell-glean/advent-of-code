package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func isValidDoBuffer(buffer string) (valid bool, complete bool, operation string) {
	valid = true
	validDo := "do()"
	validDont := "don't()"
	fullValidDoLength := len(validDo)
	fullValidDontLength := len(validDont)

	// Get valid prefix for length
	var doLengthToUse int
	if len(buffer) > len(validDo) {
		doLengthToUse = len(validDo)
	} else {
		doLengthToUse = len(buffer)
	}

	var dontLengthToUse int
	if len(buffer) > len(validDont) {
		dontLengthToUse = len(validDont)
	} else {
		dontLengthToUse = len(buffer)
	}

	// Trim down validPrefix if buffer is too short
	validDo = validDo[0:doLengthToUse]
	validDont = validDont[0:dontLengthToUse]

	if buffer != validDo && buffer != validDont {
		fmt.Println(buffer, valid)
		valid = false
	} else {
		if len(validDo) == fullValidDoLength && buffer == validDo {
			complete = true
			operation = "do"
		} else if len(validDont) == fullValidDontLength && buffer == validDont {
			complete = true
			operation = "don't"
		}
	}
	return
}

func isValidMulBuffer(buffer string) (valid bool, complete bool, operation string) {
	valid = true
	validPrefix := "mul("
	fullValidPrefixLength := len(validPrefix)

	// Get valid prefix for length
	var prefixLengthToUse int
	if len(buffer) > len(validPrefix) {
		prefixLengthToUse = len(validPrefix)
	} else {
		prefixLengthToUse = len(buffer)
	}

	// Trim down validPrefix if buffer is too short
	validPrefix = validPrefix[0:prefixLengthToUse]

	if !strings.HasPrefix(buffer, validPrefix) {
		valid = false
		return
	}

	// check numbers
	if len(buffer) > fullValidPrefixLength {
		bufferWithNoPrefix := buffer[fullValidPrefixLength:]
		numberBeforeComma := false
		processedComma := false
		numberAfterComma := false
		for _, rune := range bufferWithNoPrefix {
			char := string(rune)
			_, err := strconv.Atoi(char)
			// must be comma or closing bracket, otherwise invalid
			if err != nil {
				if numberBeforeComma && char == "," && !processedComma {
					// process one and only one comma
					processedComma = true
					continue
				} else if numberBeforeComma && processedComma && numberAfterComma && char == ")" {
					// closing bracket, has a comma before it and a number after that comma
					complete = true
					return
				} else {
					valid = false
					return
				}
			} else {
				// Already seen a comma and it is a number, set condition there is a number after the comma
				if processedComma {
					numberAfterComma = true
				} else {
					// Not seen comma so must be first number still
					numberBeforeComma = true
				}
			}
		}
	}

	return
}

func isValidBuffer(buffer string) (valid bool, complete bool, operation string) {
	if buffer[0] == 'm' {
		return isValidMulBuffer(buffer)
	} else if buffer[0] == 'd' {
		return isValidDoBuffer(buffer)
	} else {
		return false, false, ""
	}

}

func dayThree() {
	dataRaw, err := os.ReadFile("inputs/day3.txt")
	if err != nil {
		panic("Uh oh")
	}
	data := string(dataRaw)

	var validFunctions []string

	var buffer string
	do := true
	for _, rune := range data {
		// if i == 40 {
		// 	panic("uh")
		// }
		letter := string(rune)
		buffer += letter

		valid, complete, operation := isValidBuffer(buffer)
		if operation == "do" {
			fmt.Println("DO")
			do = true
		} else if operation == "don't" {
			fmt.Println("DONT")
			do = false
		}
		fmt.Println(buffer, valid, complete, operation, do)

		// add valid function to list then reset buffer
		if complete && do && operation == "" {
			validFunctions = append(validFunctions, buffer)
		}
		if complete {
			buffer = ""
		}
		// invalid so reset buffer
		if !valid {
			buffer = ""
		}

	}
	fmt.Println("Valid functions", validFunctions)

	total := 0
	for _, validFunction := range validFunctions {
		splitFunction := strings.Split(validFunction, ",")
		firstNumber, err1 := strconv.Atoi(strings.Replace(splitFunction[0], "mul(", "", 1))
		secondNumber, err2 := strconv.Atoi(strings.Replace(splitFunction[1], ")", "", 1))
		if err1 != nil || err2 != nil {
			panic("Something not numbers!")
		}
		total += firstNumber * secondNumber

	}
	fmt.Println(total)
}
