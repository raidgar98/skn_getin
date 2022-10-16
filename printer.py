from sys import argv

DEFAULT_FILE_NAME = 'example.test.txt'
file_name = argv[1] if len(argv) > 1 else DEFAULT_FILE_NAME

with open(file_name, 'r') as file:
	for line in file:
		print(line)
