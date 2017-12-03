package main

import (
	"bufio"
	"fmt"
	"math"
	"net/http"
	"strconv"
	"strings"
)

func PartOne(n float64) int {
	sq := int(math.Ceil(math.Sqrt(n)))
	for i := 0; i < 5; i++ {
		x := sq*sq - i*(sq-1)
		d := math.Abs(float64(x) - n)
		if (float64(sq)-1)/2 >= d {
			return int(sq) - 1 - int(d)
		}
	}

	return -1
}

// Kinda cheating a little. The sequence is available on OEIS https://oeis.org/A141481
func PartTwo(n float64) int {
	res, err := http.Get("https://oeis.org/A141481/b141481.txt")
	if err != nil {
		panic(err)
	}
	defer res.Body.Close()

	scanner := bufio.NewScanner(res.Body)
	for scanner.Scan() {
		l := scanner.Text()
		if l == "" {
			continue
		}

		if string(l[0]) == "#" {
			continue
		}

		x, err := strconv.ParseFloat(strings.Split(l, " ")[1], 64)
		if err != nil {
			panic(err)
		}

		if x > n {
			return int(n)
		}
	}

	return -1
}

func main() {
	n := float64(312051)
	fmt.Printf("Part one: %d\n", PartOne(n))
	fmt.Printf("Part two: %d\n", PartTwo(n))
}
