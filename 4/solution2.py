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
		elif key == 'iyr':
			if int(value) < 2010 or int(value) > 2020:
				valid = False
		elif key == 'eyr':
			if int(value) < 2020 or int(value) > 2030:
				valid = False
		elif key == 'hgt':
			if value.endswith('cm'):
				newvalue = value.lstrip('cm')
				if newvalue < 150 or newvalue > 193:
					valid = False
			elif value.endswith('in'):
				newvalue = value.lstrip('in')
				if newvalue < 50 or newvalue > 76:
					valid = False
			else:
				valid = False
		elif key == 'hcl':
			if !hcl_re.match(value):
				valid = False
		elif key == "ecl" and value not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
			valid = False
		elif key == "pid" and not pid_re.match(value):
			valid = False
		elif key == 'cid':
			pass
		else:
			valid = False

	if len(req_keys_seen) != len(req_keys):
		valid = False
	if valid:
		total_verified += 1
	total += 1
print(f"Total: {total}")
print(f"Total Verified: {total_verified}")
