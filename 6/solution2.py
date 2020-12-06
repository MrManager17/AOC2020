with open('input', 'r') as f:
	input = f.read()

groups = input.split('\n\n')

total = 0
for group in groups:
	group_answers = set()
	people = group.split('\n')
	for i, person in enumerate(people):
		person = person.strip()
		person_answers = set([x for x in person])
		if i == 0:
			group_answers = person_answers
		else:
			group_answers = group_answers.intersection(person_answers)
	total += len(group_answers)

print(f"Answer: {total}")
