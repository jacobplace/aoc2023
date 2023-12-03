package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func convertNums(l string) string {
	r := strings.NewReplacer("one", "1e", "two", "2o", "three", "3e", "four", "4r", "five", "5e", "six", "6x", "seven", "7n", "eight", "8t", "nine", "9e")
	for {
		if l == r.Replace(l) {
			break
		}
		l = r.Replace(l)
	}
	return l
}

func cleanNums(l string) string {
	re := regexp.MustCompile(`[0-9]+`)
	x := re.FindAllString(l, -1)
	return strings.Join(x, "")
}

func score(l string) int {
	var s []string
	s = append(s, string(l[0]))
	s = append(s, string(l[len(l)-1]))
	l = strings.Join(s, "")
	i, err := strconv.Atoi(l)
	if err != nil {
		panic(err)
	}
	return i
}

func main() {
	t1 := 0
	t2 := 0
	f, err := os.Open("../input.1")
	if err != nil {
		panic(err)
	}
	defer f.Close()
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		l := scanner.Text()
		fmt.Println(l)
		t1 += score(cleanNums(l))
		t2 += score(cleanNums(convertNums(l)))
	}
	fmt.Printf("P1:%d\tP2:%d\n", t1, t2)
	if scanner.Err() != nil {
		panic(scanner.Err())
	}
}
