import re
with open('input', 'r') as f:
	input = f.read().split('\n\n')

pid_re = re.compile('[0-9]{9}')
hcl_re = re.compile('#([0-9,a-f]){6}')
total_verified = 0
total = 0
for passport in input:
	passlines = passport.split('\n')
	passport_clean = {}
	for line in passlines:
		kv_pairs = line.split(' ')
		for kv in kv_pairs:
			if len(kv) < 2:
				continue
			key, value = kv.split(':')
			passport_clean[key] = value
	req_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
	valid = True
	optional_seen = False
	req_keys_seen = []
	for key in passport_clean:
		if key in req_keys and key not in req_keys_seen:
			req_keys_seen.append(key)
		elif key == 'cid' and not optional_seen:
			optional_seen == True
		else:
			valid = False

		#solution 2 added
		value = passport_clean[key]
		if key == 'byr':
			if int(value) < 1920 or int(value) > 2002:
				valid = False
				print('byr failed')
		elif key == 'iyr':
			if int(value) < 2010 or int(value) > 2020:
				valid = False
				print('iyr failed')
		elif key == 'eyr':
			if int(value) < 2020 or int(value) > 2030:
				valid = False
				print('eyr failed')
		elif key == 'hgt':
			if value.endswith('cm'):
				newvalue = int(value.rstrip('cm'))
				if newvalue < 150 or newvalue > 193:
					valid = False
					print('hgt failed')
			elif value.endswith('in'):
				newvalue = int(value.rstrip('in'))
				if newvalue < 59 or newvalue > 76:
					valid = False
					print('hgt failed')
			else:
				valid = False
				print('hgt failed')
		elif key == 'hcl':
			if not hcl_re.match(value):
				valid = False
				print('hcl failed')
		elif key == "ecl":
			if value not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
				valid = False
				print('ecl failed')
		elif key == "pid":
			if not pid_re.match(value):
				valid = False
				print('pid failed')
		elif key == 'cid':
			pass
		else:
			valid = False
			print(key)
			print(value)
			print('something else went wrong')

	if len(req_keys_seen) != len(req_keys):
		valid = False
	if valid:
		total_verified += 1
		print(passport_clean)
	total += 1
print(f"Total: {total}")
print(f"Total Verified: {total_verified-1}")
