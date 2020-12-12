
def get_move(line, heading):
	line = list(line)
	dir = line.pop(0)
	line.reverse()
	number = sum([10**x * int(line[x]) for x in range(len(line))])
	directions = ["E", "S", "W", "N"]
	if dir == 'N':
		heading[1] += number
	elif dir == 'S':
		heading[1] -= number
	elif dir == 'E':
		heading[0] += number
	elif dir == 'W':
		heading[0] -= number
	elif dir == 'L':
		heading[2] = int((heading[2] - (number/90)) % 4)
	elif dir == 'R':
		heading[2] = int((heading[2] + (number/90)) % 4)
	elif dir == 'F':
		dir = directions[heading[2]]
		get_move((dir,number), heading)
	else:
		print("Something went Wrong!!!")
	return

def main():
	with open('input', 'r') as f:
		input = f.read().splitlines()
	heading = [0,0,0]
	for line in input:
		get_move(line, heading)
	answer = abs(heading[0]) + abs(heading[1])
	print(f"Heading: {heading}")
	print(f"Answer: {answer}")

if __name__=="__main__":
	main()
