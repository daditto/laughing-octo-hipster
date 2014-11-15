
import re

input = open('school.data')

uci = [
	'uci',
	'university of california irvine',
	'uc irvine',
	'ics',
	'donald bren school of information and computer science',
]

highschool = [
	'northwood',
	'northwood high',
	'northwood high school',
	'troy high school',
	'silverado high school',
	'los alamitos high school',
]

temp = [
	'ucla',
	'ucr',
	'uc riverside',
	'university of california riverside',
	'ucsd',
	'university of california san diego',
	'uc san diego',
	'uc berkeley',
	'university of california berkeley',
	'uniersity of illinois',
	'university of laverne',
]

count = {};


def Main():
	for line in input:
		line = normalize(line)
		if line in uci:
			increment("University of California, Irvine")
		elif line in highschool:
			increment("High School");
		else:
			increment("Other University / College");

	print("UCI: ", count["University of California, Irvine"]);
	print("HS: ", count["High School"]);
	print("Other: ", count["Other University / College"]);
			
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