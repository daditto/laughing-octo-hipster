
import re

input = open('iplocation.data')

count = {};


def Main():
	for line in input:
		if re.match('Unknown Location', line):
			increment("Unknown Location")
		elif re.match('.+, CA, .+', line):
			increment("California");
		else:
			increment("Out of State");

	for key in count.keys():
		print(key, ": ", count[key]);
			
	input.close();

def normalize(line):
	line = line.rstrip("\n\r").lower()
	line = re.sub(r'[^\w]+', ' ', line)
	return line;
	
	
def increment(key):
	if key in count:
		count[key] += 1
	else:
		count[key] = 0

Main();