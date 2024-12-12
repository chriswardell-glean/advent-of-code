package main

import (
	"fmt"
	"os"
	"slices"
	"strings"
)

var grid [][]string
var gridWidth int
var gridHeight int

func getMasCoordinates(startX int, startY int) (wordCoordinates [][][]int) {
	// Gets diagonals in one direction (i.e. not the same coordinates in reverse)
	startOffsets := [][]int{{-1, -1}, {-1, 1}}
	for _, offset := range startOffsets {
		var coordinates [][]int

		for i := 1; i > -2; i-- {
			xCoord := startX + (offset[0] * i)
			yCoord := startY + (offset[1] * i)

			if xCoord < 0 || xCoord >= gridWidth {
				break
			}
			if yCoord < 0 || yCoord >= gridHeight {
				break
			}
			coordinates = append(coordinates, []int{xCoord, yCoord})
		}
		if len(coordinates) == 3 {
			wordCoordinates = append(wordCoordinates, coordinates)
		}
	}
	return wordCoordinates

}

func getRadialCoordinates(startX int, startY int, radius int) (wordCoordinates [][][]int) {
	// Return value stores list of set of x,y coordinates of the full word
	// E.g. two words of length 2: [[[0, 1], [0,2]], [[5, 1], [5,2]]]

	radialPermutationMultipler := [][]int{{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}}
	for _, radialPermutation := range radialPermutationMultipler {
		var coordinates [][]int
		// Start furthest away so we can break if it goes out of the grid
		for i := radius - 1; i > 0; i-- {
			xCoord := startX + (radialPermutation[0] * i)
			yCoord := startY + (radialPermutation[1] * i)

			if xCoord < 0 || xCoord >= gridWidth {
				break
			}
			if yCoord < 0 || yCoord >= gridHeight {
				break
			}
			coordinates = append(coordinates, []int{xCoord, yCoord})
		}
		if len(coordinates) == radius-1 {
			coordinates = append(coordinates, []int{startX, startY})
			slices.Reverse(coordinates)
			wordCoordinates = append(wordCoordinates, coordinates)
		}
	}
	return wordCoordinates

}

func getWordWithCoordinates(coords [][]int) string {
	word := ""
	for _, coord := range coords {
		word += grid[coord[1]][coord[0]]
	}

	return word
}

func dayFour() {
	dataRaw, err := os.ReadFile("inputs/day4.txt")
	if err != nil {
		panic("Uh oh")
	}
	data := string(dataRaw)

	for _, row := range strings.Split(data, "\n") {
		grid = append(grid, strings.Split(row, ""))
	}
	gridWidth = len(grid[0])
	gridHeight = len(grid)

	xmasCount := 0

	for y := 0; y < gridHeight; y++ {
		for x := 0; x < gridWidth; x++ {
			possibleWordCoordinates := getRadialCoordinates(x, y, 4)
			for _, wordCoordinates := range possibleWordCoordinates {
				word := getWordWithCoordinates(wordCoordinates)
				if word == "XMAS" {
					xmasCount++
				}
			}
		}
	}

	fmt.Println("Count:", xmasCount)

	xmasCount = 0

	for y := 0; y < gridHeight; y++ {
		for x := 0; x < gridWidth; x++ {
			masCount := 0
			possibleMasCoordinates := getMasCoordinates(x, y)
			for _, wordCoordinates := range possibleMasCoordinates {
				word := getWordWithCoordinates(wordCoordinates)
				if word == "MAS" || word == "SAM" {
					masCount++
				}
			}
			if masCount == 2 {
				xmasCount++
				continue
			}
		}
	}

	fmt.Println("Actual Xmas count:", xmasCount)

}

// O X O
// O O O
// O O O
