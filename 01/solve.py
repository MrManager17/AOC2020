#!/usr/bin/python3

input = []
with open("input", 'r') as f:
	x = f.readlines();
	for line in x:
		input.append(int(line.strip()))

for i in input:
	for j in input:
		for k in input:
			if i + j + k == 2020:
				print(str(i*j*k))
				break
