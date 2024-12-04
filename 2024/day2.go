package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func isReportSafe(report []int) bool {
	increasing := report[0] < report[1]

	previousLevel := report[0]

	for _, level := range report[1:] {
		// Not changing
		if previousLevel == level {
			return false
		}

		difference := level - previousLevel
		absoluteDifference := difference
		if absoluteDifference < 0 {
			absoluteDifference *= -1
		}

		// Increasing/decreasing more than permitted
		if absoluteDifference > 3 {
			return false
		}

		// Was increasing but now decreasing
		if increasing && difference < 0 {
			return false
		}

		// Was decreasing but now increasing
		if !increasing && difference > 0 {
			return false
		}
		previousLevel = level
	}
	return true
}

func dayTwo() {
	data, err := os.ReadFile("inputs/day2.txt")
	if err != nil {
		panic("Uh oh")
	}
	dataString := string(data)
	reportsStrings := strings.Split(dataString, "\n")
	var reports [][]int

	for i := range reportsStrings {
		report := reportsStrings[i]
		if report == "" {
			break
		}
		levelsStringList := strings.Split(report, " ")
		var levels []int
		for j := range levelsStringList {
			level, err := strconv.Atoi(levelsStringList[j])
			if err != nil {
				panic("Not a number!")
			}
			levels = append(levels, level)
		}
		reports = append(reports, levels)
	}

	safeReportCount := 0
	for _, report := range reports {
		reportSafe := isReportSafe(report)
		if reportSafe {
			fmt.Println("SAFE", report)
			safeReportCount++
		} else {
			fmt.Println("Not safe, checking 1 bad level", report)
			// Try dropping level
			for i := range report {
				reportWithoutLevel := make([]int, len(report))
				copy(reportWithoutLevel, report)
				reportWithoutLevel = append(reportWithoutLevel[:i], reportWithoutLevel[i+1:]...)

				reportSafe = isReportSafe(reportWithoutLevel)
				if reportSafe {
					fmt.Println("New report safe", reportWithoutLevel)
					safeReportCount++
					break
				}
			}
		}
	}

	fmt.Println("Safe report count:", safeReportCount)
	fmt.Println("Number of reports", len(reports))
}
