from pathlib import Path
import shutil
import sys

import cli 

def generate_template():
	def _info():
		"""Without commandline arguments"""
		inp = input("What is the path to the input html file?\n>>> ")
		args = ["-o", input("What do you want to call the output file?\n>>> "), 
				"-n", input("What is the name/title of the assignment?\n>>> "),
				"-m", input("What is the contact email?\n>>> "), inp
				]
		return args
	
	if len(sys.argv[1:]) == 0:
		sys.argv[1:] = _info()

	return cli.main(sys.argv[1:])

def place_templates(filename: str, student_dir: str):
	"""TODO: test 
		- exists
		- path to a directory"""
	if args.directory is None:
		student_dir = input("What is the parent directory of the submissions? ")
	student_dir = Path(student_dir)
	filename = Path(filename)

	for subdir in student_dir.glob("*"):
		if subdir.is_dir():
			shutil.copy(filename, subdir / filename)


if __name__ == "__main__":
	args = generate_template()
	if args.input == "test.html":
	    place_templates(args.output, args.directory)

