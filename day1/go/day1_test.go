package main

import "testing"

func TestConvertNums(t *testing.T) {
	var tests = []struct {
		have string
		want string
	}{
		{"44", "44"},
		{"1two3", "12o3"},
		{"eight1t2d", "8t1t2d"},
		{"eightwo", "82o"},
	}
	for _, test := range tests {
		name := test.have
		t.Run(name, func(t *testing.T) {
			r := convertNums(test.have)
			if test.want != r {
				t.Errorf("got %s want %s", r, test.want)
			}
		})
	}
}

func TestCleanNums(t *testing.T) {
	var tests = []struct {
		have string
		want string
	}{
		{"44", "44"},
		{"1two3", "13"},
		{"e1t2d", "12"},
		{"a12e34f", "1234"},
	}
	for _, test := range tests {
		name := test.have
		t.Run(name, func(t *testing.T) {
			r := cleanNums(test.have)
			if test.want != r {
				t.Errorf("got %s want %s", r, test.want)
			}
		})
	}
}

func TestScore(t *testing.T) {
	var tests = []struct {
		have string
		want int
	}{
		{"4", 44},
		{"123", 13},
		{"12345", 15},
	}
	for _, test := range tests {
		name := test.have
		t.Run(name, func(t *testing.T) {
			r := score(test.have)
			if test.want != r {
				t.Errorf("got %d want %d", r, test.want)
			}
		})
	}
}
