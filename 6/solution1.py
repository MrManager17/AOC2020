with open('input', 'r') as f:
	input = f.read()

groups = input.split('\n\n')

total = 0
for group in groups:
	group_answers = set()
	people = group.split('\n')
	for person in people:
		person = person.strip()
		for answer in person:
			group_answers.add(answer)
	total += len(group_answers)

print(f"Answer: {total}")
